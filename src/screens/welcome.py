from kivy.uix.screenmanager import Screen
from src.ui import load_screen
from src.utils import navigate_to

load_screen('screens/welcome')


class WelcomeScreen(Screen):

    def navigate_to_game(self):
        navigate_to('game')

    def navigate_to_scores(self):
        navigate_to('scores')

    def navigate_to_settings(self):
        navigate_to('settings')

    def navigate_to_help(self):
        navigate_to('help')
