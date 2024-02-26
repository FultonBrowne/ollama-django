import json
from channels.generic.websocket import WebsocketConsumer
import ollama
from django_streaming import settings


class ChatChannel(WebsocketConsumer):

    def __init__(self):
        super(ChatChannel, self).__init__()
        self.history = []
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.close()

    def receive(self, text_data, **kwargs):
        text_data_json = json.loads(text_data)
        expression = text_data_json['prompt']
        prompt = {'role': 'user', 'content': expression}
        self.history.append(prompt)
        stream = ollama.chat(
            model='llama2',
            messages=self.history,
            stream=True,
        )
        message = {'role': 'assistant', 'content': ''}
        for i in stream:
            if i['done']:
                self.history.append(message)
            content = i['message']['content']
            message['content'] += content
            self.send(text_data=json.dumps({
                'result': content
            })) 
        self.send(text_data=json.dumps({
            'result': "DONE"
        }))
        print(stream)
