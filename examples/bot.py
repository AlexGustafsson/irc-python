"""Example module for the IRC connector."""

import logging
import random
import re
from datetime import datetime

# Import the parsed CLI options for the example module
from examples import options

# Import the IRC class and the message type
from irc import IRC
from irc.messages import IRCMessage


def main() -> None:
    """Main entrypoint of the bot example."""
    # Log at INFO level or higher
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Create an IRC instance
    irc = IRC(
        options.server,
        options.port,
        options.user,
        options.nick,
        logger=logger,
        timeout=options.timeout,
        use_tls=options.use_tls
    )

    # Connect to the server
    irc.connect()

    # Join a channel
    irc.join("#bot-test")

    # Loop through all messages - current and future
    for message in irc.messages:
        # If someone's sent a message
        if isinstance(message, IRCMessage):
            # Get the target of the message. If the target is the bot directly,
            # send the message to the author - else send it to the channel the message
            # was directed to
            target = message.author if message.target == "test" else message.target

            # Match commands targeted to our bot
            match = re.match("bot: ([^ ]+)( (.*))?", message.message)
            if not match:
                continue

            # Extract command and optional parameters from the message
            command, _, parameter = match.groups()
            if command == "about":
                # Send about message
                irc.send_message(target, "I'm a simple example bot.")
                irc.send_message(target, "Read more about me on https://github.com/AlexGustafsson/irc-python.")
            elif command == "help":
                # Send help message
                irc.send_message(target, "You invoke me by sending 'bot: <command> <parameters>'")
            elif command == "torvalds":
                quotes = [
                    "Talk is cheap. Show me the code.",
                    "Intelligence is the ability to avoid doing work, yet getting the work done.",
                    "Given enough eyeballs, all bugs are shallow."
                ]
                # Send a random Linus Torvalds quote
                irc.send_message(target, random.choice(quotes))  # nosec
            elif command == "time":
                # Send the local time
                irc.send_message(target, datetime.now().strftime("%H:%M:%S"))
            elif command == "sum":
                # Calculate the sum of the parameters
                try:
                    result = sum([int(number) for number in parameter.split(" ")])
                    irc.send_message(target, str(result))
                except ValueError:
                    logger.error("Got bad parameters for sum: %s", parameter)
                    irc.send_message(target, "Unable to sum the parameters")
            else:
                # Handle unknown commands
                irc.send_message(target, "Sorry, I'm not sure what you want me to do")


if __name__ == "__main__":
    main()
