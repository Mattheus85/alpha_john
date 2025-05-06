import os
import random
from kivy.core.audio import SoundLoader
from .config import IMAGE_DIR, SOUND_DIR


class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.loaded_sounds = {}
        self.load_images("assets/images")
        self.load_sounds("assets/sounds")

    def load_images(self, image_dir):
        if os.path.exists(image_dir):
            for filename in os.listdir(image_dir):
                if filename.endswith(".png"):
                    asset_name = filename.replace('.png', '')
                    self.images[asset_name] = os.path.join(image_dir, filename)

    def load_sounds(self, sound_dir):
        if os.path.exists(sound_dir):
            for asset_name in os.listdir(sound_dir):
                asset_dir = os.path.join(sound_dir, asset_name)
                if os.path.isdir(asset_dir):
                    self.sounds[asset_name] = [os.path.join(asset_dir, f) for f in os.listdir(asset_dir) if f.endswith(".mp3")]

    def get_sound(self, asset_name):
        if asset_name in self.loaded_sounds:
            return self.loaded_sounds[asset_name]

        sound_paths = self.sounds.get(asset_name)
        if sound_paths:
            sound_path = random.choice(sound_paths)
            sound = SoundLoader.load(sound_path)
            if sound:
                self.loaded_sounds[asset_name] = sound
                return sound
        return None
