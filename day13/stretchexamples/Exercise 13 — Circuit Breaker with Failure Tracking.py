'''
Exercise 13 — Circuit Breaker with Failure Tracking
'''

from time import monotonic


class CircuitBreaker:

    def __init__(self, threshold=3, timeout=5):
        self.threshold = threshold
        self.timeout = timeout
        self.failures = 0
        self.opened_at = None

    def execute(self, operation):
        now = monotonic()

        if self.opened_at is not None:
            if now - self.opened_at < self.timeout:
                raise RuntimeError("Circuit OPEN")

            self.opened_at = None
            self.failures = 0

        try:
            result = operation()

        except ConnectionError:
            self.failures += 1

            if self.failures >= self.threshold:
                self.opened_at = monotonic()

            raise

        self.failures = 0
        return result


def unstable_service():
    raise ConnectionError("Service unavailable")


breaker = CircuitBreaker()

for _ in range(5):
    try:
        breaker.execute(unstable_service)

    except (ConnectionError, RuntimeError) as error:
        print(type(error).__name__, error)