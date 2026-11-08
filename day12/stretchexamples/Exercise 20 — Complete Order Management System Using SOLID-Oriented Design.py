'''
Exercise 20 — Complete Order Management System Using SOLID-Oriented Design
'''
from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class OrderItem:
    name: str
    price: Decimal
    quantity: int


@dataclass(frozen=True)
class Order:
    order_id: int
    items: tuple[OrderItem, ...]


class PricingService:

    def calculate_total(self, order):
        return sum(
            (
                item.price * item.quantity
                for item in order.items
            ),
            Decimal(0)
        )


class PaymentGateway(ABC):

    @abstractmethod
    def charge(self, amount):
        pass


class UPIPaymentGateway(PaymentGateway):

    def charge(self, amount):
        print(f"UPI charged: {amount}")
        return True


class CardPaymentGateway(PaymentGateway):

    def charge(self, amount):
        print(f"Card charged: {amount}")
        return True


class NotificationService:

    def send(self, message):
        print("Notification:", message)


class OrderRepository:

    def __init__(self):
        self.orders = {}

    def save(self, order):
        self.orders[order.order_id] = order

    def find(self, order_id):
        return self.orders.get(order_id)


class OrderService:

    def __init__(
        self,
        pricing_service,
        payment_gateway,
        notification_service,
        repository
    ):
        self.pricing_service = pricing_service
        self.payment_gateway = payment_gateway
        self.notification_service = notification_service
        self.repository = repository

    def process_order(self, order):

        if not order.items:
            raise ValueError("Order cannot be empty")

        for item in order.items:
            if item.price < 0 or item.quantity <= 0:
                raise ValueError("Invalid order item")

        if self.repository.find(order.order_id) is not None:
            raise ValueError("Duplicate order ID")

        total = self.pricing_service.calculate_total(order)

        if not self.payment_gateway.charge(total):
            raise RuntimeError("Payment failed")

        self.repository.save(order)

        self.notification_service.send(
            f"Order {order.order_id} completed"
        )

        return total


order = Order(
    order_id=101,
    items=(
        OrderItem("Laptop", Decimal(50000), 1),
        OrderItem("Mouse", Decimal(500), 2)
    )
)

service = OrderService(
    PricingService(),
    UPIPaymentGateway(),
    NotificationService(),
    OrderRepository()
)

print("Total:", service.process_order(order))