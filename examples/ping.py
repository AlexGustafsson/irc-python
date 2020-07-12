"""Example module for the IRC connector."""

# Import the parsed CLI options for the example module
from examples import options

# Import the IRC class and the message type
from irc import IRC
from irc.messages import IRCMessage


def main() -> None:
    """Main entrypoint of the ping example."""
    # Create an IRC instance
    irc = IRC(
        options.server,
        options.port,
        options.user,
        options.nick,
        timeout=options.timeout,
        use_tls=options.use_tls
    )

    # Connect to the server
    irc.connect()

    # Join a channel
    irc.join("#bot-test")

    # Loop through all messages - current and future
    for message in irc.messages:
        # If someone's sent a message "ping"
        if isinstance(message, IRCMessage) and message.message == "ping":
            # Get the target of the message. If the target is the bot directly,
            # send the message to the author - else send it to the channel the message
            # was directed to
            target = message.author if message.target == "test" else message.target
            # Send "pong"
            irc.send_message(target, "pong")


if __name__ == "__main__":
    main()
