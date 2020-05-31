"""Unit tests for the message module."""

from hypothesis import example, given
from hypothesis.strategies import text

from irc.messages import IRCMessage


@given(text())
@example(":alex!alex@local PRIVMSG bot :Hello, world!")
def test_parse(raw_message: str) -> None:
    """
    Ensure that the message parser returns a properly parsed message.

    Also fuzz the method by exploring paths using a coverage-based approach.
    """
    message = IRCMessage.parse(raw_message)
    if message is not None:
        assert message.message == "Hello, world!"  # nosec
