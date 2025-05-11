from kivy.app import App
from kivy.core.window import Window

from src.appscreenmanager import AppScreenManager


class PyPongApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.size = (900, 600)
        Window.minimum_width = 720
        Window.minimum_height = 480

        self.controller = None
        self.state_context = None
        self.start_command = None
        self.pause_command = None
        self.resume_command = None
        self.restart_command = None

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
