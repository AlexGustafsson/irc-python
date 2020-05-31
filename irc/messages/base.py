"""IRC base message."""

from typing import Optional


class IRCBaseMessage():
    """IRC message base class."""

    @staticmethod
    def parse(line: str) -> Optional["IRCBaseMessage"]:
        """Parse a message."""
