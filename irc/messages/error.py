"""IRC error message."""

import re
from typing import Optional

from irc.messages.base import IRCBaseMessage

# Regex for matching the individual parts of an IRC message
error_message_regex = re.compile("^:([^ ]+) ([^ ]+) ([^ ]+) ([^ ]+) :(.*)")


class IRCErrorMessage(IRCBaseMessage):
    """IRC error message base class."""

    def __init__(  # pylint: disable=too-many-arguments
            self,
            server: str,
            code: str,
            target: str,
            author: str,
            message: str
    ) -> None:
        self.__server = server
        self.__code = code
        self.__target = target
        self.__author = author
        self.__message = message

    @property
    def server(self) -> str:
        """The server the message originated from."""
        return self.__server

    @property
    def code(self) -> str:
        """The error message's code."""
        return self.__code

    @property
    def target(self) -> str:
        """The error message's target."""
        return self.__target

    @property
    def author(self) -> str:
        """The error message's author."""
        return self.__author

    @property
    def message(self) -> str:
        """The message itself."""
        return self.__message

    @staticmethod
    def parse(line: str) -> Optional["IRCErrorMessage"]:
        """Parse a message."""
        match = error_message_regex.match(line)
        if not match:
            return None

        server, code, target, author, message = match.groups()
        return IRCErrorMessage(server, code, target, author, message)
