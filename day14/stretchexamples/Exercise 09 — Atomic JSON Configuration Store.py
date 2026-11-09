'''
Exercise 09 — Atomic JSON Configuration Store
'''
import json
import os
import tempfile
from pathlib import Path


class AtomicJSONStore:

    def __init__(self, filename):
        self.path = Path(filename)

    def save(self, data):
        temporary = None

        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=self.path.parent,
                delete=False
            ) as file:
                temporary = Path(file.name)

                json.dump(data, file, indent=4)
                file.flush()
                os.fsync(file.fileno())

            os.replace(temporary, self.path)

        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)

    def load(self):
        with self.path.open("r", encoding="utf-8") as file:
            return json.load(file)


store = AtomicJSONStore("settings.json")

store.save({
    "theme": "dark",
    "timeout": 30
})

print(store.load())