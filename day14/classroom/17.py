'''
Example 17 — ZIP Archive Creation and Extraction
'''
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

folder = Path("reports")
folder.mkdir(exist_ok=True)

(folder / "report1.txt").write_text("Report One")
(folder / "report2.txt").write_text("Report Two")

with ZipFile("reports.zip", "w", ZIP_DEFLATED) as archive:
    for path in folder.glob("*.txt"):
        archive.write(path, arcname=path.name)

with ZipFile("reports.zip", "r") as archive:
    print(archive.namelist())

    for name in archive.namelist():
        print(name, archive.read(name).decode("utf-8"))