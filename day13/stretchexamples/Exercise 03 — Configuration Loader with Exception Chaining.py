'''
Exercise 03 — Configuration Loader with Exception Chaining
'''
class ConfigurationError(Exception):
    pass


def load_configuration(config):
    try:
        host = config["host"]
        port = int(config["port"])
        timeout = float(config["timeout"])

    except (KeyError, ValueError, TypeError) as error:
        raise ConfigurationError(
            "Invalid application configuration"
        ) from error

    if not 1 <= port <= 65535:
        raise ConfigurationError("Port outside valid range")

    if timeout <= 0:
        raise ConfigurationError("Timeout must be positive")

    return {
        "host": host,
        "port": port,
        "timeout": timeout
    }


configs = [
    {"host": "localhost", "port": "8000", "timeout": "5"},
    {"host": "localhost", "port": "abc", "timeout": "5"},
    {"host": "localhost", "port": "9000"}
]

for config in configs:
    try:
        print(load_configuration(config))

    except ConfigurationError as error:
        print(error)
        print("Cause:", repr(error.__cause__))