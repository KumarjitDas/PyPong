from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen

from src.models import get_all_entries
from src.ui import load_screen

load_screen('screens/scores')


class RowItem(BoxLayout):
    id = StringProperty()
    time_played = StringProperty()
    timestamp = StringProperty()
    p1_score = StringProperty()
    p2_score = StringProperty()


class GameResultsView(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_data()

    def refresh_data(self):
        rows = get_all_entries()

        self.data = [{
            'id': str(row[0]),
            'time_played': f"{row[1]:.1f}",
            'timestamp': row[2],
            'p1_score': str(row[3]),
            'p2_score': str(row[4])
        } for row in rows]


class ScoresScreen(Screen):
    pass
