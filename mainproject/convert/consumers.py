
import json
import numpy as np
import torch
import whisper as ws
from channels.generic.websocket import WebsocketConsumer
model = ws.load_model("small.en")



class AudioConsumer(WebsocketConsumer):
     def connect(self):
           self.accept()
           
    
     def disconnect(self, close_code):
        # Perform any cleanup tasks here
        self.send("WebSocket connection closed.")
    
     def receive(self, text_data=None, bytes_data=None):
        try:
            if bytes_data:
                self.send(text_data = "pohach gaya"
                )
            if len(bytes_data) % 2 != 0:
            # Adjust the length of bytes_data to make it even
                bytes_data = bytes_data[:-1]
            audio_array = np.frombuffer(bytes_data, dtype=np.int16)
            audio_array_float = audio_array.astype(np.float32) / 32768.0

            
            # print("Data type of audio_array_float:", audio_array_float.dtype)
             # Transcribe audio using the model
           

            text = model.transcribe(audio_array_float, task="transcribe", verbose=True)
            # text = model.transcribe(bytes_data, task="transcribe", verbose=True)
            print("recive and processing : ", text)
            self.send(text_data=text['text'])
        except Exception as error:
            print(f"error:{error}")
        
        
        # await self.send(text_data = text["text"])
        
        