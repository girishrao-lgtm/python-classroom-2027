'''
Example 15 — File Locking with Exclusive Creation
'''
import os
from pathlib import Path

lock_path = Path("application.lock")

descriptor = None

try:
    descriptor = os.open(
        lock_path,
        os.O_CREAT | os.O_EXCL | os.O_WRONLY,
        0o600
    )

    with os.fdopen(descriptor, "w") as file:
        descriptor = None
        file.write(str(os.getpid()))

    print("Lock acquired")
    print("Critical operation executing")

except FileExistsError:
    print("Another lock file already exists")

finally:
    if descriptor is not None:
        os.close(descriptor)

    # Only remove the lock if this process acquired it.
    # See ownership tracking in the stretch exercises.