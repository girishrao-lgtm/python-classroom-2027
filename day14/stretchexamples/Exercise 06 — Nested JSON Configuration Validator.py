'''

Exercise 06 — Nested JSON Configuration Validator
'''
import json


class ConfigurationError(Exception):
    pass


def validate(config):
    try:
        database = config["database"]
        host = database["host"]
        port = database["port"]
        timeout = config["timeout"]

    except (KeyError, TypeError) as error:
        raise ConfigurationError(
            "Missing configuration field"
        ) from error

    if not isinstance(host, str) or not host:
        raise ConfigurationError("Invalid host")

    if type(port) is not int or not 1 <= port <= 65535:
        raise ConfigurationError("Invalid port")

    if type(timeout) not in (int, float) or timeout <= 0:
        raise ConfigurationError("Invalid timeout")

    return True


config = {
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "timeout": 30
}

json_text = json.dumps(config)

loaded = json.loads(json_text)

try:
    print(validate(loaded))
except ConfigurationError as error:
    print(error)