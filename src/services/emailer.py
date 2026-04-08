"""Email service for handling subscriptions and sending summaries."""

import imaplib
import smtplib
import socket as _socket_mod
import email
import os
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import parseaddr
from typing import List, Optional
from urllib.parse import urlparse

try:
    import markdown
except ImportError:
    markdown = None

from contextlib import contextmanager

from ..models import EmailConfig

logger = logging.getLogger(__name__)


@contextmanager
def _proxy_socket():
    """Temporarily route all sockets through HTTP CONNECT proxy if env vars are set."""
    proxy_url = os.environ.get("HTTPS_PROXY") or os.environ.get("HTTP_PROXY")
    if not proxy_url:
        yield
        return

    try:
        import socks
    except ImportError:
        logger.warning("PySocks not installed — cannot route SMTP through proxy")
        yield
        return

    parsed = urlparse(proxy_url)
    original = _socket_mod.socket
    socks.set_default_proxy(socks.HTTP, parsed.hostname, parsed.port)
    _socket_mod.socket = socks.socksocket
    try:
        yield
    finally:
        _socket_mod.socket = original


class EmailManager:
    """Manages email subscriptions and sending summaries."""

    def __init__(self, config: EmailConfig, console=None):
        self.config = config
        self.pwd = os.getenv(self.config.password_env)
        if console is None:
            try:
                from rich.console import Console
                self.console = Console()
            except ImportError:
                class DummyConsole:
                    def print(self, *args, **kwargs):
                        print(*args, **kwargs)
                self.console = DummyConsole()
        else:
            self.console = console

        if not self.pwd and self.config.enabled:
            logger.warning(
                f"Environment variable {self.config.password_env} not set. Email features may fail."
            )
            self.console.print(f"[yellow]Warning: Environment variable {self.config.password_env} not set. Email features may fail.[/yellow]")


    def check_subscriptions(self, storage_manager):
        """Checks inbox for subscription requests and updates subscriber list."""
        if not self.config.enabled:
            return

        try:
            # Connect to IMAP
            mail = imaplib.IMAP4_SSL(self.config.imap_server, self.config.imap_port)
            mail.login(self.config.email_address, self.pwd)
            mail.select("INBOX")

            # 1. Process Subscriptions
            keyword = self.config.subscribe_keyword
            # We search ALL messages with SUBSCRIBE because sometimes clients
            # (like your phone/web) mark incoming emails as read before the script catches them.
            search_crit = f'(UNSEEN SUBJECT "{keyword}")'

            status, messages = mail.search(None, search_crit)

            if status == "OK" and messages[0]:
                email_ids = messages[0].split()
                subscribers = storage_manager.load_subscribers()

                for e_id in email_ids:
                    # Fetch the email
                    _, msg_data = mail.fetch(e_id, "(RFC822)")
                    for response_part in msg_data:
                        if isinstance(response_part, tuple):
                            msg = email.message_from_bytes(response_part[1])

                            subject = str(msg.get("Subject") or "").strip()
                            if subject.upper() != keyword.upper():
                                continue

                            sender = msg.get("From")

                            if sender:
                                _, email_addr = parseaddr(sender)
                                if email_addr and "@" in email_addr:
                                    if "noreply" in email_addr.lower() or "no-reply" in email_addr.lower():
                                        continue

                                    if email_addr not in subscribers:
                                        storage_manager.add_subscriber(email_addr)
                                        # Reload list to keep it fresh
                                        subscribers = storage_manager.load_subscribers()
                                        self._send_reply(
                                            email_addr,
                                            "Subscribed to Daybreak",
                                            "You have been successfully subscribed to Daybreak daily summaries.",
                                        )
                                        logger.info(f"Added subscriber: {email_addr}")
                                    else:
                                        logger.info(f"Already subscribed: {email_addr}")

            # 2. Process Unsubscriptions
            unsub_keyword = self.config.unsubscribe_keyword
            search_crit_unsub = f'(UNSEEN SUBJECT "{unsub_keyword}")'

            status, messages = mail.search(None, search_crit_unsub)

            if status == "OK" and messages[0]:
                email_ids = messages[0].split()
                subscribers = storage_manager.load_subscribers()

                for e_id in email_ids:
                    _, msg_data = mail.fetch(e_id, "(RFC822)")
                    for response_part in msg_data:
                        if isinstance(response_part, tuple):
                            msg = email.message_from_bytes(response_part[1])

                            subject = str(msg.get("Subject") or "").strip()
                            if subject.upper() != unsub_keyword.upper():
                                continue

                            sender = msg.get("From")

                            if sender:
                                _, email_addr = parseaddr(sender)
                                if email_addr and "@" in email_addr:
                                    if "noreply" in email_addr.lower() or "no-reply" in email_addr.lower():
                                        continue

                                    if email_addr in subscribers:
                                        storage_manager.remove_subscriber(email_addr)
                                        subscribers = storage_manager.load_subscribers()
                                        self._send_reply(
                                            email_addr,
                                            "Unsubscribed from Daybreak",
                                            "You have been successfully unsubscribed from Daybreak daily summaries.",
                                        )
                                        logger.info(f"Removed subscriber: {email_addr}")
                                    else:
                                        logger.info(f"Not subscribed: {email_addr}")

            mail.close()
            mail.logout()

        except Exception as e:
            logger.error(f"Error checking subscriptions: {e}")

    def send_daily_summary(
        self, summary_md: str, subject: str, subscribers: List[str],
        newspaper_image: Optional[bytes] = None,
    ):
        """Sends the daily summary to all subscribers.

        If newspaper_image (PNG bytes) is provided, it is embedded inline
        at the top of the HTML email via CID reference.
        """
        if not self.config.enabled or not subscribers:
            return

        html_content = (
            markdown.markdown(summary_md)
            if markdown
            else f"<pre>{summary_md}</pre>"
        )

        newspaper_html = ""
        if newspaper_image:
            newspaper_html = (
                '<div style="text-align:center; margin-bottom:20px;">'
                '<img src="cid:newspaper" style="max-width:100%; height:auto;" '
                'alt="Daybreak Daily">'
                '</div>'
                '<hr style="margin:20px 0;">'
            )

        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
                h1, h2, h3 {{ color: #2c3e50; }}
                code {{ background-color: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: monospace; }}
                pre {{ background-color: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
                blockquote {{ border-left: 4px solid #ddd; padding-left: 15px; color: #777; }}
                .footer {{ margin-top: 40px; font-size: 12px; color: #888; text-align: center; border-top: 1px solid #eee; padding-top: 20px; }}
            </style>
        </head>
        <body>
            {newspaper_html}
            {html_content}
            <div class="footer">
                <p>Sent by {self.config.sender_name}</p>
                <p>To unsubscribe, please reply with "{self.config.unsubscribe_keyword}"</p>
            </div>
        </body>
        </html>
        """

        try:
            with _proxy_socket(), smtplib.SMTP_SSL(
                self.config.smtp_server, self.config.smtp_port
            ) as server:
                server.login(self.config.email_address, self.pwd)

                for subscriber in subscribers:
                    if newspaper_image:
                        msg = MIMEMultipart("related")
                        alt = MIMEMultipart("alternative")
                        alt.attach(MIMEText(summary_md, "plain"))
                        alt.attach(MIMEText(html_body, "html"))
                        msg.attach(alt)
                        img_part = MIMEImage(newspaper_image, _subtype="png")
                        img_part.add_header("Content-ID", "<newspaper>")
                        img_part.add_header(
                            "Content-Disposition", "inline", filename="daybreak.png"
                        )
                        msg.attach(img_part)
                    else:
                        msg = MIMEMultipart("alternative")
                        msg.attach(MIMEText(summary_md, "plain"))
                        msg.attach(MIMEText(html_body, "html"))

                    msg["Subject"] = subject
                    msg["From"] = f"{self.config.sender_name} <{self.config.email_address}>"
                    msg["To"] = subscriber

                    try:
                        server.send_message(msg)
                        logger.info(f"Sent summary to {subscriber}")
                    except Exception as e:
                        logger.error(f"Failed to send to {subscriber}: {e}")

        except Exception as e:
            logger.error(f"SMTP Error: {e}")

    def _send_reply(self, to_email: str, subject: str, body: str):
        """Helper to send a simple reply."""
        try:
            with _proxy_socket(), smtplib.SMTP_SSL(
                self.config.smtp_server, self.config.smtp_port
            ) as server:
                server.login(self.config.email_address, self.pwd)

                msg = MIMEText(body)
                msg["Subject"] = subject
                msg["From"] = f"{self.config.sender_name} <{self.config.email_address}>"
                msg["To"] = to_email

                server.send_message(msg)
        except Exception as e:
            logger.error(f"Failed to send reply to {to_email}: {e}")
