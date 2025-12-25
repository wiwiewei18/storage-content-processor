import json

class EventPublisher:
    def __init__(self, channel, exchange: str, routing_key: str):
        self.channel = channel
        self.exchange = exchange
        self.routing_key = routing_key

    def publish(self, event):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=json.dumps(event.__dict__)
        )
