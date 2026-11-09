'''
Exercise 06 — Custom File Manager
'''
class FileManager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(
            self.filename,
            self.mode,
            encoding="utf-8"
        )
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file is not None:
            self.file.close()

        return False


with FileManager("report.txt", "w") as file:
    file.write("Python Context Manager Example\n")

with FileManager("report.txt", "r") as file:
    print(file.read())
    