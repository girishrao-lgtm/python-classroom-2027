'''
Exercise 05 — Streaming CSV Transformation
'''

import csv

with open("sales.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["product", "quantity", "price"])
    writer.writerows([
        ["Laptop", 2, 50000],
        ["Mouse", 5, 500],
        ["Keyboard", 3, 1500]
    ])

with open("sales.csv", "r", newline="", encoding="utf-8") as source, open(
    "sales_processed.csv",
    "w",
    newline="",
    encoding="utf-8"
) as destination:

    reader = csv.DictReader(source)

    writer = csv.DictWriter(
        destination,
        fieldnames=["product", "quantity", "price", "total"]
    )

    writer.writeheader()

    for row in reader:
        quantity = int(row["quantity"])
        price = int(row["price"])

        row["total"] = quantity * price

        writer.writerow(row)

print("Transformation completed")