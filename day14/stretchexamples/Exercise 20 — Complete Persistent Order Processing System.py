'''
Exercise 20 — Complete Persistent Order Processing System
'''

import sqlite3
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Order:
    order_id: int
    product_id: int
    quantity: int


class InventoryRepository:

    def __init__(self, connection):
        self.connection = connection

    def reserve(self, product_id, quantity):
        cursor = self.connection.execute(
            """
            UPDATE inventory
            SET quantity = quantity - ?
            WHERE product_id = ?
              AND quantity >= ?
            """,
            (quantity, product_id, quantity)
        )

        if cursor.rowcount != 1:
            raise ValueError("Insufficient inventory")


class OrderRepository:

    def __init__(self, connection):
        self.connection = connection

    def save(self, order, total):
        self.connection.execute(
            """
            INSERT INTO orders
            (order_id, product_id, quantity, total)
            VALUES (?, ?, ?, ?)
            """,
            (
                order.order_id,
                order.product_id,
                order.quantity,
                str(total)
            )
        )


class OrderService:

    def __init__(self, connection):
        self.connection = connection
        self.inventory = InventoryRepository(connection)
        self.orders = OrderRepository(connection)

    def process(self, order):
        if order.quantity <= 0:
            raise ValueError("Invalid quantity")

        with self.connection:
            row = self.connection.execute(
                """
                SELECT price
                FROM inventory
                WHERE product_id = ?
                """,
                (order.product_id,)
            ).fetchone()

            if row is None:
                raise ValueError("Product not found")

            price = Decimal(row[0])
            total = price * order.quantity

            self.inventory.reserve(
                order.product_id,
                order.quantity
            )

            self.orders.save(order, total)

        return total


connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
        CREATE TABLE inventory (
            product_id INTEGER PRIMARY KEY,
            price TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity >= 0)
        )
    """)

    connection.execute("""
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            total TEXT NOT NULL
        )
    """)

    with connection:
        connection.execute(
            "INSERT INTO inventory VALUES (?, ?, ?)",
            (101, "500.00", 10)
        )

    service = OrderService(connection)

    print("Order total:", service.process(Order(1, 101, 3)))

    try:
        service.process(Order(2, 101, 100))
    except ValueError as error:
        print("Rejected:", error)

    print("Inventory:")
    print(connection.execute(
        "SELECT * FROM inventory"
    ).fetchall())

    print("Orders:")
    print(connection.execute(
        "SELECT * FROM orders"
    ).fetchall())

finally:
    connection.close()