'''
Example 13 — Logging Decorator
'''
import logging
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Starting %s", func.__name__)

        try:
            result = func(*args, **kwargs)
        except Exception:
            logger.exception("Failed %s", func.__name__)
            raise

        logger.info("Completed %s", func.__name__)
        return result

    return wrapper

@log_execution
def divide(a, b):
    return a / b

print(divide(20, 5))