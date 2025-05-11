from kivy.app import App
from kivy.core.window import Window

_PREV_WINDOW_BINDS = {}
_WINDOW_BINDS = {}


def navigate_to(page):
    App.get_running_app().root.current = page


def bind_window(**kwargs):
    key = list(kwargs.keys())[0]
    val = kwargs[key]

    if not _WINDOW_BINDS.get(key):
        _WINDOW_BINDS[key] = []

    _WINDOW_BINDS[key].append(val)

    if not _PREV_WINDOW_BINDS.get(key):
        if hasattr(Window, key):
            _PREV_WINDOW_BINDS[key] = Window.__dict__.get(f"_{key}", None)
        else:
            _PREV_WINDOW_BINDS[key] = None

    def callback(*args):
        prev_window_bind = _PREV_WINDOW_BINDS.get(key)

        if callable(prev_window_bind):
            ret = prev_window_bind(*args)
            if ret:
                return True

        window_binds = _WINDOW_BINDS.get(key, [])

        for fn in reversed(window_binds):
            if callable(fn):
                ret = fn(*args)
                if ret:
                    return True

        return None

    new_kwargs = {key: callback}
    Window.bind(**new_kwargs)


def unbind_window(**kwargs):
    key = list(kwargs.keys())[0]
    val = kwargs[key]
    window_binds = _WINDOW_BINDS.get(key, [])

    try:
        window_binds.remove(val)
    except ValueError:
        pass


__all__ = ['navigate_to', 'bind_window', 'unbind_window']
