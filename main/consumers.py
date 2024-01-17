import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LiveStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass

    async def send_hls_url_update(self, event):
        hls_url = event['hls_url']
        await self.send(text_data=json.dumps({'hls_url': hls_url}))        