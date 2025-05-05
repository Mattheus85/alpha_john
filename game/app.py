import os
os.environ['SDL_VIDEODRIVER'] = 'wayland'
from kivy.config import Config
Config.set('graphics', 'width', '1920')  # Force window width
Config.set('graphics', 'height', '1080')  # Force window height
from kivy.app import App
from kivy.core.window import Window
from .widget import GameWidget

class GameApp(App):
    def build(self):
        Window.fullscreen = False
        # Window.size = (1024, 768)
        # Window.size = (1280, 800)
        # Window.size = (1440, 900)
        # Window.size = (1680, 1050)
        Window.size = (1920, 1080)
        Window.clearcolor = (0, 0, 0, 0)
        return GameWidget()
