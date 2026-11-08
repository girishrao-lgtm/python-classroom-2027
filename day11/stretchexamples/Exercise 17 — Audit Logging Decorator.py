'''
Exercise 17 — Audit Logging Decorator
'''

from datetime import UTC, datetime
from functools import wraps

audit_logs = []

def audit(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        timestamp = datetime.now(UTC).isoformat()

        try:
            result = func(*args, **kwargs)
        except Exception:
            audit_logs.append({
                "function": func.__name__,
                "timestamp": timestamp,
                "status": "FAILED"
            })
            raise

        audit_logs.append({
            "function": func.__name__,
            "timestamp": timestamp,
            "status": "SUCCESS"
        })

        return result

    return wrapper

@audit
def transfer(amount):

    if amount <= 0:
        raise ValueError("Invalid transfer")

    return f"Transferred {amount}"

print(transfer(1000))

try:
    transfer(-100)
except ValueError:
    pass

for log in audit_logs:
    print(log)
    