from kivy.lang import Builder

import os

__all__ = ['load_resource', 'load_screen']


def load_resource(path):
    resource_path = os.path.join(os.path.dirname(__file__), path)
    Builder.load_file(resource_path)


def load_screen(name):
    load_resource(f'../resources/{name}.kv')
