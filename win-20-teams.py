# MACROPAD Hotkeys example: MEMM 13.10.2021
# file was from https://learn.adafruit.com/macropad-hotkeys/project-code

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Teams', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x080500, 'Hand', [Keycode.CONTROL, Keycode.SHIFT, 'K']),
        (0x080500, 'Mute', [Keycode.CONTROL, Keycode.SHIFT, 'M']),
        (0x000800, 'Video', [Keycode.CONTROL, Keycode.SHIFT, 'O']),
        # 2nd row ----------
        (0x000000, '', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x000000, '', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x000000, '', [Keycode.SHIFT, ' ']),
        # 3rd row ----------
        (0xFFFF00, 'Hand', [Keycode.CONTROL, Keycode.SHIFT, 'K']),
        (0x000000, '', ['All the best\nMatthias']),
        (0x000000, '', ['Kind regards\nMatthias']),
        # 4th row ----------
        (0xFF8800, 'Cut', [Keycode.CONTROL, 'x']),
        (0xFF8800, 'Copy', [Keycode.CONTROL, 'c']),
        (0xFF8800, 'Paste', [Keycode.CONTROL, 'v']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w'])
    ]
}
