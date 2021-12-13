# MACROPAD Hotkeys example: MEMM 13.10.2021
# file was from https://learn.adafruit.com/macropad-hotkeys/project-code

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Outlook', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000008, 'Mail', [Keycode.CONTROL, '1']),
        (0x080808, 'Calendar', [Keycode.CONTROL, '2']),
        (0x040404, '!?', [Keycode.LEFT_ALT, Keycode.KEYPAD_EIGHT, -Keycode.KEYPAD_EIGHT, Keycode.KEYPAD_TWO, -Keycode.KEYPAD_TWO, Keycode.KEYPAD_FIVE, -Keycode.KEYPAD_FIVE, Keycode.KEYPAD_THREE, -Keycode.KEYPAD_THREE]),
        # 2nd row ----------
        (0x00CC00, 'Pound', [Keycode.LEFT_ALT, Keycode.KEYPAD_ZERO, -Keycode.KEYPAD_ZERO, Keycode.KEYPAD_ONE, -Keycode.KEYPAD_ONE, Keycode.KEYPAD_SIX, -Keycode.KEYPAD_SIX, Keycode.KEYPAD_THREE, -Keycode.KEYPAD_THREE]),
        (0xDD00DD, 'Ade2', ['\n\nAll the best\nMatthias']),
        (0xDD00DD, 'Ade3', ['\n\nKind regards\nMatthias']),       
        # 3rd row ----------
        (0xFF8800, 'All', [Keycode.CONTROL, 'a']),
        (0x00CC00, 'Lang', [Keycode.WINDOWS, Keycode.SPACEBAR, -Keycode.SPACEBAR]),
        (0xFF8800, 'PlainP', [Keycode.CONTROL, Keycode.SHIFT, 'v']),
        # 4th row ----------
        (0xFF8800, 'Cut', [Keycode.CONTROL, 'x']),
        (0xFF8800, 'Copy', [Keycode.CONTROL, 'c']),
        (0xFF8800, 'Paste', [Keycode.CONTROL, 'v']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w'])
    ]
}
