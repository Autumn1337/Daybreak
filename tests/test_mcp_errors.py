from src.mcp.errors import DaybreakMcpError


def test_daybreak_mcp_error_string_representation() -> None:
    err = DaybreakMcpError(code="E_TEST", message="boom", details={"k": "v"})

    assert str(err) == "E_TEST: boom"
    assert err.details == {"k": "v"}
