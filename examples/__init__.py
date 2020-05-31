"""Examples for the IRC connector."""

from argparse import ArgumentParser

__package__ = "examples"

# Create an argument parser for parsing CLI arguments
parser = ArgumentParser(description="An example application")

# Add parameters for the server connection
parser.add_argument("-s", "--server", required=True, type=str, help="The server to connect to")
# Add optional parameters for the server connection
parser.add_argument("-p", "--port", default=6697, type=int, help="The port to connect to")
parser.add_argument("--use-tls", default=True, type=bool, help="Whether or not to use TLS")
parser.add_argument("-t", "--timeout", default=1, type=float, help="Connection timeout in seconds")

# Add optional parameters for authentication
parser.add_argument("-u", "--user", required=True, help="Username to use when connecting to the IRC server")
parser.add_argument("-n", "--nick", required=True, help="Nick to use when connecting to the IRC server")
parser.add_argument("-g", "--gecos", help="Gecos to use when connecting to the IRC server")
parser.add_argument("--password", help="Password for the specified user")

# Parse the arguments and execute the chosen command
options = parser.parse_args()
