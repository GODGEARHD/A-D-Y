from modules import osd
from pynput.keyboard import Key, Controller

Keyboard = Controller()


def keystroke(media, run):

    match media:

        case "play":
            Keyboard.press(Key.media_play_pause)

        case "previous":
            Keyboard.press(Key.media_previous)

        case "next":
            Keyboard.press(Key.media_next)

        case "shortcut":
            Keyboard.press(Key.ctrl)
            Keyboard.press(Key.alt)
            Keyboard.press(Key.shift)
            Keyboard.press("a")
            Keyboard.release(Key.ctrl)
            Keyboard.release(Key.alt)
            Keyboard.release(Key.shift)
            Keyboard.release("a")

        case "show":
            osd.show()

        case "hide":
            osd.hide()

        case _:
            if run:
                Keyboard.press(Key.ctrl)
                Keyboard.press(Key.alt)
                Keyboard.press(Key.shift)
                Keyboard.press("u")
                Keyboard.release(Key.ctrl)
                Keyboard.release(Key.alt)
                Keyboard.release(Key.shift)
                Keyboard.release("u")
