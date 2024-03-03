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
    
    async def receive(self, text_data):
        try:
            
            audio_chunk = text_data
            audio_file = open('audio.wav', 'wb')
            audio_file.write(audio_chunk)
            audio_file.close()
            text = model.transcribe(audio_chunk)
            await self.send(text_data=text)
        except Exception as e:
            print("Error: ", e)
        