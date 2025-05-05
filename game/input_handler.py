from kivy.app import App
from kivy.core.window import Window

def setup_input(widget):
    Window.bind(on_key_down=lambda w, k, s, c, m: on_keystroke_down(widget, c, m))

def on_keystroke_down(widget, codepoint, modifier):
    # print(f"codepoint: {codepoint}\nmodifier: {modifier}")

    # Quit on Ctrl+Shift+Q, does not work correctly with wayland, must use Hyprland's Meta+Shift+Q
    if codepoint == 'q' and all(v in modifier for v in ['ctrl', 'shift']):
        App.get_running_app().stop() # type: ignore
        return True

    shifted_numbers_map = {
        "0": "close_paren",
        "1": "exclamation_mark",
        "2": "at",
        "3": "pound_sign",
        "4": "dollar_sign",
        "5": "percent",
        "6": "carat",
        "7": "ampersand",
        "8": "asterisk",
        "9": "open_paren"
    }
    shifted_symbols_map = {
        "]": "close_curly_brace",
        ";": "colon",
        "'": "double_quote",
        ",": "left_angle_bracket",
        "[": "open_curly_brace",
        "\\": "pipe",
        "=": "plus",
        "/": "question_mark",
        ".": "right_angle_bracket",
        "`": "tilde",
        "-": "underscore"
    }
    symbols_map = {
        ")": "close_paren",
        "!": "exclamation_mark",
        "@": "at",
        "#": "pound_sign",
        "$": "dollar_sign",
        "%": "percent",
        "^": "carat",
        "&": "ampersand",
        "*": "asterisk",
        "(": "open_paren",

        "}": "close_curly_brace",
        ":": "colon",
        "\"": "double_quote",
        "<": "left_angle_bracket",
        "{": "open_curly_brace",
        "|": "pipe",
        "+": "plus",
        "?": "question_mark",
        ">": "right_angle_bracket",
        "~": "tilde",
        "_": "underscore",

        "\\": "backslash",
        "`": "backtick",
        "]": "close_square_bracket",
        ",": "comma",
        "=": "equals",
        "-": "minus",
        "[": "open_square_bracket",
        ".": "period",
        ";": "semicolon",
        "'": "single_quote",
        "/": "slash"
    }

    is_shift = 'shift' in modifier
    char = None

    if codepoint and codepoint.isalpha():
        char = codepoint.upper() if is_shift else codepoint
    elif codepoint and codepoint.isdigit():
        char = shifted_numbers_map.get(codepoint) if is_shift else codepoint
    elif codepoint:
        # Wayland implementation
        char = symbols_map.get(codepoint)

        # X11 implementation
        # char = shifted_symbols_map.get(codepoint) if is_shift else symbols_map.get(codepoint)

    if not char:
        return True

    # Update the single character image
    img_path = widget.asset_manager.images.get(char)
    if img_path:
        widget.char_image.source = img_path  # Replace the image
        # Cancel any running animation
        if widget.char_image.current_anim:
            widget.char_image.current_anim.cancel(widget.char_image)
        widget.start_animation()
    else:
        return True

    from .audio import play_sound
    play_sound(widget, char)
    return True
