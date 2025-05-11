from kivy.app import App
from kivy.uix.popup import Popup
from kivy.factory import Factory

from src.ui import load_screen
from src.utils import bind_window, unbind_window

load_screen('utils/quitpopup')


class QuitPopup(Popup):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._binds = {}

        bind_window(on_key_down=self._on_key_down)
        self.bind_event(on_dismiss=self._on_dismiss)

    def _on_key_down(self, window, key, *args):
        if key == 27:
            self.dismiss()
            return True

        return None

    def _on_dismiss(self, *args):
        unbind_window(on_key_down=self._on_key_down)

    def quit_app(self):
        App.get_running_app().stop()

    def bind_event(self, **kwargs):
        key = list(kwargs.keys())[0]
        val = kwargs[key]

        if not self._binds.get(key):
            self._binds[key] = []

        self._binds[key].append(val)

        def callback(*args):
            binds = self._binds.get(key, [])

            for fn in reversed(binds):
                if callable(fn):
                    ret = fn(*args)
                    if ret:
                        return True

            return None

        new_kwargs = {key: callback}
        self.bind(**new_kwargs)

    def unbind_event(self, **kwargs):
        key = list(kwargs.keys())[0]
        val = kwargs[key]
        binds = self._binds.get(key, [])

        try:
            binds.remove(val)
        except ValueError:
            pass


Factory.register('QuitPopup', cls=QuitPopup)


class EscapableQuitPopup:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._eqp__popup = None
        self._eqp__is_quit_popup_shown = False
        bind_window(on_key_down=self._eqp__on_key_down)

    def _eqp__on_key_down(self, window, key, *args):
        if key == 27:
            self.show_quit_popup()
            return True

        return None

    def show_quit_popup(self):
        if not self._eqp__is_quit_popup_shown:
            self._eqp__is_quit_popup_shown = True
            self._eqp__popup = QuitPopup()
            self._eqp__popup.bind_event(on_dismiss=self._eqp__on_quit_popup_dismiss)
            self._eqp__popup.open()

    def hide_quit_popup(self):
        if self._eqp__is_quit_popup_shown:
            self._eqp__is_quit_popup_shown = False
            self._eqp__popup.unbind_event(on_dismiss=self._eqp__on_quit_popup_dismiss)
            self._eqp__popup.dismiss()

    def _eqp__on_quit_popup_dismiss(self, instance):
        self._eqp__is_quit_popup_shown = False
