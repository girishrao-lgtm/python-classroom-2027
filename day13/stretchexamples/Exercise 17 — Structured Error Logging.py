'''
Exercise 17 — Structured Error Logging
'''
import json
import logging
from datetime import UTC, datetime

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def log_error(error, request_id):
    record = {
        "timestamp": datetime.now(
            UTC
        ).isoformat(),
        "request_id": request_id,
        "error_type": type(error).__name__,
        "message": str(error)
    }

    logger.error(json.dumps(record))


def process_payment(amount):
    if amount <= 0:
        raise ValueError("Invalid payment amount")

    return "Payment successful"


try:
    process_payment(-100)

except ValueError as error:
    log_error(error, "REQ-1001")