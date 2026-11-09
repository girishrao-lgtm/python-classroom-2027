'''
Example 14 — Atomic File Replacement
'''
import json
import os
import tempfile
from pathlib import Path

destination = Path("configuration.json")

configuration = {
    "debug": False,
    "timeout": 30,
    "version": 2
}

temporary_path = None

try:
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=destination.parent,
        prefix=".config_",
        suffix=".tmp",
        delete=False
    ) as file:
        temporary_path = Path(file.name)

        json.dump(configuration, file, indent=4)
        file.flush()
        os.fsync(file.fileno())

    os.replace(temporary_path, destination)

finally:
    if temporary_path is not None:
        temporary_path.unlink(missing_ok=True)

print(destination.read_text(encoding="utf-8"))
