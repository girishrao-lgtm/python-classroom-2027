'''
Example 20 — Production-Oriented Order Processing with OOP
'''
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    order_id: int
    amount: float


class PaymentGateway(ABC):

    @abstractmethod
    def charge(self, amount):
        pass


class UPIGateway(PaymentGateway):

    def charge(self, amount):
        return f"UPI payment successful: {amount}"


class CardGateway(PaymentGateway):

    def charge(self, amount):
        return f"Card payment successful: {amount}"


class NotificationService:

    def send(self, message):
        print("Notification:", message)


class OrderService:

    def __init__(self, payment_gateway, notification_service):
        self.payment_gateway = payment_gateway
        self.notification_service = notification_service

    def process(self, order):
        if order.amount <= 0:
            raise ValueError("Invalid order amount")

        result = self.payment_gateway.charge(order.amount)

        self.notification_service.send(
            f"Order {order.order_id} processed"
        )

        return result


order = Order(101, 2500)

service = OrderService(
    UPIGateway(),
    NotificationService()
)

print(service.process(order))