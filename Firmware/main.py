# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

from kmk.extensions.LED import LED

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# This is the LED
led = LED(led_pin=[board.GP4])
keyboard.extensions.append(led)

# function for key #1
def helloWorld(keyboard):
    keyboard.led.pwm_led(0, 1)  # LED on
    keyboard.sleep_ms(100)
    keyboard.led.pwm_led(0, 0)  # LED off
    keyboard.sleep_ms(100)
    keyboard.led.pwm_led(0, 1)  # LED on
    keyboard.sleep_ms(100)
    keyboard.led.pwm_led(0, 0)  # LED off
    keyboard.sleep_ms(100)

    keyboard.type_string("Hello World!")

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D26, board.D27, board.D28, 
        board.D29, board.D6, board.D7, 
        board.D0, board.D1, board.D2]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [Macro(helloWorld), KC.Macro(Press(KC.LCMD), Tap(KC.LALT), Release(KC.LCMD)), KC.Macro(Press(KC.LCTRL), Tap(KC.S), Release(KC.LCTRL)),
     KC.Macro(Press(KC.LCTRL), Tap(KC.X), Release(KC.LCTRL)), KC.Macro(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)), KC.Macro(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)),
     KC.Macro(Press(KC.LEFT)), KC.Macro(Press(KC.SPACE)), KC.Macro(Press(KC.RIGHT))]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()