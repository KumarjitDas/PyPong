from kivy.app import App
from kivy.core.window import Window

from src.appscreenmanager import AppScreenManager
from src.db import create_table

APP_MIN_WIDTH = 900
APP_MIN_HEIGHT = 600


class PyPongApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.size = (APP_MIN_WIDTH, APP_MIN_HEIGHT)
        Window.minimum_width = APP_MIN_WIDTH
        Window.minimum_height = APP_MIN_HEIGHT

        self.controller = None
        self.state_context = None
        self.start_command = None
        self.pause_command = None
        self.resume_command = None
        self.restart_command = None

        create_table()

    def build(self):
        app = AppScreenManager()
        return app


def main():
    print("""
PyPong - A simple and classic Pong game built with Python and Kivy, designed to bring back the retro gaming experience
with a modern touch. This project serves as both a fun game and a practical implementation of game development concepts
using the Kivy framework.
    """)

    PyPongApp().run()


if __name__ == '__main__':
    main()
