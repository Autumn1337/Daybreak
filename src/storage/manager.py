"""Storage manager for configuration and state persistence."""

import json
import shutil
from pathlib import Path

from ..models import Config


class StorageManager:
    """Manages file-based storage for configuration and state."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.config_path = self.data_dir / "config.json"
        self.summaries_dir = self.data_dir / "summaries"

        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.summaries_dir.mkdir(parents=True, exist_ok=True)

    def load_config(self) -> Config:
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}\n"
                f"Please create it based on the template in README.md"
            )

        with open(self.config_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return Config.model_validate(data)

    def save_config(self, config: Config, backup: bool = True) -> Path:
        """Save configuration to config.json, optionally backing up the existing file.

        Args:
            config: The Config object to save.
            backup: If True and config.json exists, copy it to config.json.bak first.

        Returns:
            Path to the saved config file.
        """
        if backup and self.config_path.exists():
            shutil.copy2(self.config_path, self.config_path.with_suffix(".json.bak"))

        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(config.model_dump(mode="json"), f, indent=2, ensure_ascii=False)
            f.write("\n")

        return self.config_path

    def save_daily_summary(self, date: str, markdown: str, language: str = "en") -> Path:
        filename = f"daybreak-{date}-{language}.md"
        filepath = self.summaries_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

        return filepath

    def save_docs_post(self, date: str, summary: str, language: str = "en") -> Path:
        """Save summary as a Jekyll post to docs/_posts/.

        Adds Jekyll front matter and strips the leading H1 to avoid
        duplication with the Jekyll-generated title.

        Args:
            date: Date string (YYYY-MM-DD).
            summary: Markdown summary content.
            language: Language code.

        Returns:
            Path to the written file.
        """
        posts_dir = Path("docs/_posts")
        posts_dir.mkdir(parents=True, exist_ok=True)

        front_matter = (
            "---\n"
            "layout: default\n"
            f"title: \"Daybreak Summary: {date} ({language.upper()})\"\n"
            f"date: {date}\n"
            f"lang: {language}\n"
            "---\n\n"
        )

        # Strip leading H1 header to avoid duplication with Jekyll title
        content = summary
        first_line = content.strip().split("\n")[0]
        if first_line.startswith("# "):
            parts = content.split("\n", 1)
            if len(parts) > 1:
                content = parts[1].strip()

        dest = posts_dir / f"{date}-summary-{language}.md"
        dest.write_text(front_matter + content, encoding="utf-8")
        return dest

    def load_subscribers(self) -> list:
        """Loads the list of email subscribers."""
        subscribers_path = self.data_dir / "subscribers.json"
        if not subscribers_path.exists():
            return []

        try:
            with open(subscribers_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def add_subscriber(self, email_addr: str):
        """Adds a new subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr not in subscribers:
            subscribers.append(email_addr)
            self._save_subscribers(subscribers)

    def remove_subscriber(self, email_addr: str):
        """Removes a subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr in subscribers:
            subscribers.remove(email_addr)
            self._save_subscribers(subscribers)

    def _save_subscribers(self, subscribers: list):
        """Helper to save subscribers list."""
        subscribers_path = self.data_dir / "subscribers.json"
        with open(subscribers_path, "w", encoding="utf-8") as f:
            json.dump(subscribers, f, indent=2)
