import time

# https://pypi.org/project/keyboard/
import keyboard


def hold(hotkey):
    """Presses and holds down a hotkey """
    keyboard.press(hotkey)


def press_and_release(hotkey: str or int):
    """Sends OS events that perform the given *hotkey* hotkey.

    - `hotkey` can be either a scan code (e.g. 57 for space), single key  
    (e.g. 'space') or multi-key, multi-step hotkey (e.g. 'alt+F4, enter').

        press_and_release(57)  
        press_and_release('ctrl+alt+del')  
        press_and_release('alt+F4, enter')  
        press_and_release('shift+s')  
    Note: keys are released in the opposite order they were pressed."""
    keyboard.press_and_release(hotkey)


def handle_request(args):
    """This function handles incoming requests to the keyboard resource

    Args:
        args (object): The HTML request body, which looks as follows: 
        {"hotkey": str or int, "hold": bool}
    """
    if (args.hold):
        hold(args.hotkey)
    else:
        press_and_release(args.hotkey)

    