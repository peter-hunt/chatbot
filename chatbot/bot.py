from dataclasses import dataclass

__all__ = ['Chatbot']


@dataclass
class Chatbot:
    def run(self):
        print('Hello World!')
