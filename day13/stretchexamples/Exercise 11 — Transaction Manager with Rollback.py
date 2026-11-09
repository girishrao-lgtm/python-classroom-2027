'''
Exercise 11 — Transaction Manager with Rollback
'''
from contextlib import contextmanager
from copy import deepcopy

database = {
    "accounts": {
        "A101": 5000,
        "A102": 2000
    }
}


@contextmanager
def transaction():
    snapshot = deepcopy(database)

    try:
        yield database

    except Exception:
        database.clear()
        database.update(snapshot)
        print("Transaction rolled back")
        raise

    else:
        print("Transaction committed")


try:
    with transaction() as db:
        db["accounts"]["A101"] -= 1000
        db["accounts"]["A102"] += 1000

        raise RuntimeError("Simulated failure")

except RuntimeError:
    pass

print(database)