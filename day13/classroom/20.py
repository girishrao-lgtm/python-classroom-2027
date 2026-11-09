'''
Example 20 — Production-Oriented Error Handling with Logging
'''
import logging
from functools import wraps

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


class ApplicationError(Exception):
    pass


class ValidationError(ApplicationError):
    pass


class ProcessingError(ApplicationError):
    pass


def log_errors(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ApplicationError:
            logger.exception(
                "Application error in %s",
                func.__name__
            )
            raise

        except Exception:
            logger.exception(
                "Unexpected error in %s",
                func.__name__
            )
            raise

    return wrapper


@log_errors
def process_order(amount):
    if amount <= 0:
        raise ValidationError("Invalid order amount")

    if amount > 100000:
        raise ProcessingError("Order limit exceeded")

    return f"Order processed: {amount}"


for amount in [1000, -50, 200000]:
    try:
        print(process_order(amount))

    except ApplicationError as error:
        print("Request failed:", error)