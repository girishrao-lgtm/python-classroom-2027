'''
Exercise 08 — Notification System Using Duck Typing
'''
class EmailNotifier:

    def send(self, message):
        return f"Email: {message}"


class SMSNotifier:

    def send(self, message):
        return f"SMS: {message}"


class PushNotifier:

    def send(self, message):
        return f"Push: {message}"


class NotificationManager:

    def __init__(self, notifiers):
        self.notifiers = notifiers

    def notify_all(self, message):
        results = []

        for notifier in self.notifiers:
            results.append(notifier.send(message))

        return results


manager = NotificationManager([
    EmailNotifier(),
    SMSNotifier(),
    PushNotifier()
])

for result in manager.notify_all("System maintenance"):
    print(result)
    