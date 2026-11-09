'''
Example 17 — Dynamic Resource Management with ExitStack
'''
from contextlib import ExitStack
from pathlib import Path

files = [
    Path("file1.txt"),
    Path("file2.txt"),
    Path("file3.txt")
]

with ExitStack() as stack:
    handles = [
        stack.enter_context(
            path.open("w", encoding="utf-8")
        )
        for path in files
    ]

    for index, handle in enumerate(handles, start=1):
        handle.write(f"Content for file {index}\n")

print("All files closed")