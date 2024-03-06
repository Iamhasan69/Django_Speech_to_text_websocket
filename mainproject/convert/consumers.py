import asyncio
import whisper as ws
from channels.generic.websocket import AsyncWebsocketConsumer
model = ws.load_model("base")


class AudioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, close_code):
        # Perform any cleanup tasks here
        print("WebSocket connection closed.")
    
    async def receive(self, bytes_data):
        try:
            
            audio_chunk = bytes_data
            text = model.transcribe(audio_chunk)
            await self.send(text["text"])
        except Exception as e:
            print("Error: ", e)
        