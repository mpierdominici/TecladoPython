from pynput.keyboard import Key, Controller
import time
keyboard = Controller()


time.sleep(5)
# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
keyboard.press(Key.ctrl)
keyboard.press('x')
keyboard.release('x')
keyboard.release(Key.ctrl)

# Type two upper case As
keyboard.press('A')
keyboard.release('A')
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

keyboard.press(Key.ctrl)
keyboard.press('v')
keyboard.release('v')
keyboard.release(Key.ctrl)


# Type 'Hello World' using the shortcut type method
keyboard.type('Hello World')