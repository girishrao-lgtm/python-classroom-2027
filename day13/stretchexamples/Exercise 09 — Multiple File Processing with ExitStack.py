'''
Exercise 09 — Multiple File Processing with ExitStack
'''
from contextlib import ExitStack
from pathlib import Path

paths = [
    Path("input1.txt"),
    Path("input2.txt"),
    Path("input3.txt")
]

for index, path in enumerate(paths, start=1):
    path.write_text(
        f"File {index}\n",
        encoding="utf-8"
    )


with ExitStack() as stack:
    files = [
        stack.enter_context(
            path.open("r", encoding="utf-8")
        )
        for path in paths
    ]

    contents = [
        file.read()
        for file in files
    ]

print(contents)