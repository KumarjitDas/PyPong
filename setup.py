from setuptools import setup, find_packages

setup(
    name='PyPong',
    version='0.1.0',
    description="""
PyPong is a simple and classic Pong game built with Python and Kivy, designed to bring back the retro gaming experience
with a modern touch. This project serves as both a fun game and a practical implementation of game development concepts
using the Kivy framework.
    """,
    author='Kumarjit Das',
    author_email='kumarjitdas1999+pypong@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pypong = pypong.main:main'
        ]
    },
    install_requires=[]
)
