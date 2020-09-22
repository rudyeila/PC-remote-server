import keyboard


def hold(hotkey):
    """Presses and holds down a hotkey """
    keyboard.press(hotkey)


def press_and_release(hotkey):
    """Sends OS events that perform the given *hotkey* hotkey.

    - `hotkey` can be either a scan code (e.g. 57 for space), single key  
    (e.g. 'space') or multi-key, multi-step hotkey (e.g. 'alt+F4, enter').

    - `do_press` if true then press events are sent. Defaults to True.  
    - `do_release` if true then release events are sent. Defaults to True.  

        send(57)  
        send('ctrl+alt+del')  
        send('alt+F4, enter')  
        send('shift+s')  
    Note: keys are released in the opposite order they were pressed."""
    keyboard.press_and_release(hotkey)
