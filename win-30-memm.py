# MACROPAD Hotkeys example: MEMM 11.10.2021
# file was from https://learn.adafruit.com/macropad-hotkeys/project-code

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'MEMM', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x000000, '', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x000000, '', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x000500, 'Pound', [Keycode.LEFT_ALT, Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, Keycode.KEYPAD_SIX, -Keycode.KEYPAD_SIX, Keycode.KEYPAD_THREE, -Keycode.KEYPAD_THREE]),
        (0x000000, '', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0x000500, 'Lang', [Keycode.WINDOWS, Keycode.SPACEBAR, -Keycode.SPACEBAR]),
        # 3rd row ----------
        (0x000005, 'Ade1', ['Best wishes\nMatthias']),
        (0x000005, 'Ade2', ['All the best\nMatthias']),
        (0x000005, 'Ade3', ['Kind regards\nMatthias']),
        # 4th row ----------
        (0x080500, 'Cut', [Keycode.CONTROL, 'x']),
        (0x080500, 'Copy', [Keycode.CONTROL, 'c']),
        (0x080500, 'Paste', [Keycode.CONTROL, 'v']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w'])
    ]
}
