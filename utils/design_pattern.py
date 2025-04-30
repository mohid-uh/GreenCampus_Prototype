class Publisher:
    """
    Publisher class that can register subscribers
    and notify them of events.
    """
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, event, data=None):
        for sub in self.subscribers:
            sub.update(event, data)


class Subscriber:
    """
    Subscriber class requiring an 'update' method.
    """
    def update(self, event, data):
        raise NotImplementedError("Subscriber must implement 'update' method.")
