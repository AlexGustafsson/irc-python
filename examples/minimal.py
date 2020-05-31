"""Example module for the IRC connector."""

# Import the parsed CLI options for the example module
from examples import options

# Import the IRC class
from irc import IRC


def main() -> None:
    """Main entrypoint of the minimal example."""
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

    # Read the first message
    print(next(irc.messages))


if __name__ == "__main__":
    main()
