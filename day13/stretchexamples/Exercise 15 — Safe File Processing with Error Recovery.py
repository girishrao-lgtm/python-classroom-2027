'''
Exercise 15 — Safe File Processing with Error Recovery
'''
from pathlib import Path


def process_file(source, destination):
    source = Path(source)
    destination = Path(destination)

    try:
        with source.open("r", encoding="utf-8") as file:
            lines = file.readlines()

        processed = [
            line.strip().upper()
            for line in lines
            if line.strip()
        ]

        with destination.open("w", encoding="utf-8") as file:
            file.write("\n".join(processed))

    except FileNotFoundError as error:
        raise RuntimeError("Source file missing") from error

    except PermissionError as error:
        raise RuntimeError("File access denied") from error


Path("source.txt").write_text(
    "python\n\njava\nc++\n",
    encoding="utf-8"
)

process_file("source.txt", "output.txt")

print(Path("output.txt").read_text(encoding="utf-8"))