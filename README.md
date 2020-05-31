# Python IRC Connector
### A dependency free, easy-to-use and highly extensible IRC connector for Python 3
***

### Setting up

##### Quickstart

First, simply copy the the `irc` directory into your project. You can then use the connector like so:

```Python
from irc import IRC

# Create an IRC instance
irc = IRC("irc.example.com", 6697, "test-user", "test-user")

# Connect to the server
irc.connect()

# Read the first message
print(next(irc.messages))

# Send a message
irc.send_message("#bot-test", "Hello, world!")
```

### Documentation

##### Features

* Easy to use
* Highly extensible
* Thread safe
* Supports TLS
* Zero dependencies
* Low-level socket API built for speed and efficiency
* Uses typing
* Handles message splitting etc. automatically

##### Examples

There are multiple examples available in the `examples` directory. To run one of them, simply execute the following command:

```shell
python3 -m examples.ping --server irc.example.com --user test --nick test
```

### Contributing

Any contribution is welcome. If you're not able to code it yourself, perhaps someone else is - so post an issue if there's anything on your mind.

###### Development

Clone the repository:
```shell
git clone https://github.com/AlexGustafsson/irc-python
```

Setup a virtual environment and dependencies:
```shell
make setup
```

Write code and commit it.

Follow the conventions enforced:
```shell
make static-analysis
```

Test the project:
```shell
make test
```

### Disclaimer

_Although the project is very capable, it is not built with production in mind. Therefore there might be complications when trying to use the connector for large-scale projects meant for the public. The bot was created to easily connect to IRC and as such it might not promote best practices nor be performant._
