'''
Exercise 07 — Temporary Working Directory
'''
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def temporary_directory_context():
    original_directory = Path.cwd()

    with tempfile.TemporaryDirectory() as directory:
        try:
            os.chdir(directory)
            yield Path(directory)

        finally:
            os.chdir(original_directory)


print("Before:", Path.cwd())

with temporary_directory_context() as directory:
    print("Inside:", Path.cwd())

    Path("sample.txt").write_text(
        "Temporary data",
        encoding="utf-8"
    )

    print(list(directory.iterdir()))

print("After:", Path.cwd())

