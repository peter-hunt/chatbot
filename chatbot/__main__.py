from sys import version_info

from .bot import Chatbot

__all__ = ['chatbot_main']


def chatbot_main():
    if version_info < (3, 10):
        raise ValueError('at least python 3.10 is required by this project')

    bot = Chatbot()
    bot.run()


if __name__ == '__main__':
    chatbot_main()
