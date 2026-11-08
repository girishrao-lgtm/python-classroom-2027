'''
Example 14 — Duck Typing
'''
class PDFExporter:

    def export(self, data):
        return f"PDF exported: {data}"


class CSVExporter:

    def export(self, data):
        return f"CSV exported: {data}"


class JSONExporter:

    def export(self, data):
        return f"JSON exported: {data}"


def generate_report(exporter, data):
    print(exporter.export(data))


exporters = [
    PDFExporter(),
    CSVExporter(),
    JSONExporter()
]

for exporter in exporters:
    generate_report(exporter, "Student Results")