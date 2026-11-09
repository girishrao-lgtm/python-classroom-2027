'''
Exercise 20 — Complete Fault-Tolerant Batch Processing Pipeline
'''

import logging
from contextlib import contextmanager
from dataclasses import dataclass
from time import perf_counter

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class ProcessingError(Exception):
    pass


class ValidationError(ProcessingError):
    pass


@dataclass(frozen=True)
class Transaction:
    transaction_id: int
    amount: float


@contextmanager
def monitor(label):
    start = perf_counter()

    logger.info("%s started", label)

    try:
        yield

    except Exception:
        logger.exception("%s failed", label)
        raise

    finally:
        elapsed = perf_counter() - start
        logger.info(
            "%s completed in %.6f seconds",
            label,
            elapsed
        )


class TransactionProcessor:

    def validate(self, transaction):
        if transaction.amount <= 0:
            raise ValidationError("Invalid amount")

    def process(self, transaction):
        self.validate(transaction)

        return {
            "transaction_id": transaction.transaction_id,
            "tax": round(transaction.amount * 0.18, 2),
            "total": round(transaction.amount * 1.18, 2)
        }


class BatchProcessor:

    def __init__(self, processor):
        self.processor = processor

    def execute(self, transactions):
        successful = []
        failed = []

        with monitor("Batch processing"):
            for transaction in transactions:
                try:
                    result = self.processor.process(transaction)
                    successful.append(result)

                except ProcessingError as error:
                    failed.append({
                        "transaction_id": transaction.transaction_id,
                        "error": str(error)
                    })

        return successful, failed


transactions = [
    Transaction(101, 1000),
    Transaction(102, -200),
    Transaction(103, 2500),
    Transaction(104, 0),
    Transaction(105, 500)
]

batch = BatchProcessor(TransactionProcessor())

successful, failed = batch.execute(transactions)

print("Successful:")
for item in successful:
    print(item)

print("Failed:")
for item in failed:
    print(item)