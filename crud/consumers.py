from channels.generic.websocket import WebsocketConsumer
import json


class ProductConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass

    def send_product_notification(self, event):
        product = event['product']
        self.send(text_data=json.dumps({
            'message': f'Новый продукт создан: {product}'
        }))
