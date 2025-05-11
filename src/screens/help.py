from kivy.uix.screenmanager import Screen
from src.ui import load_screen
from src.utils import navigate_to

load_screen('screens/help')


class HelpScreen(Screen):

    def navigate_to_welcome(self):
        navigate_to('welcome')
