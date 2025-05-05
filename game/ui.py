from kivy.uix.image import Image
from kivy.core.window import Window
from asset_manager.config import BACKGROUND_IMAGE_PATH

def setup_ui(widget):
    h_size = Window.size[0]
    v_size = Window.size[1]

    # widget.bg = Image(source=BACKGROUND_IMAGE_PATH, size=(1920, 1080), fit_mode="contain")
    # widget.bg.opacity = 0.5
    # widget.add_widget(widget.bg)

    widget.char_image = Image(size=(h_size, v_size), fit_mode="contain", opacity=0)
    widget.char_image.center = (h_size / 2, v_size / 2)
    widget.char_image.current_anim = None  # pyright: ignore[reportAttributeAccessIssue]
    widget.add_widget(widget.char_image)
