from kivy.app import App


def navigate_to(page):
    App.get_running_app().root.current = page


__all__ = ['navigate_to']
