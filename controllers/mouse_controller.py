from enum import Enum
from typing import Tuple

# https://github.com/boppreh/mouse
import mouse


LEFT_CLICK = "LEFT_CLICK"
RIGHT_CLICK = "RIGHT_CLICK"
MIDDLE_CLICK = "MIDDLE_CLICK"
DOUBLE_CLICK = "DOUBLE_CLICK"




def get_position() -> Tuple[int, int]:
    """Get the current x and y coordinates of the mouse

    Returns
    -------
    tuple of ints
        (x, y) coordinates of the mouse
    """
    return mouse.get_position()

def move(x: int, y: int, absolute=True, duration=0):
    """Moves the mouse to the new coordinates. 

    Args:
        x (int): The new X (coordinate/offset) of the mouse.
        y (int): The new Y (coordinate/offset) of the mouse.
        absolute (bool, optional): Whether the new coordinates are absolute or simply offsets. Defaults to True.
        duration (int, optional): The animation duration of the mouse movements. Defaults to 0.
    """
    mouse.move(x, y, absolute, duration)

def perform_action(action: str):  # Change action type from string to predefined costants
    if (action == LEFT_CLICK):
        mouse.click()
        return True
    elif (action == RIGHT_CLICK):
        mouse.click(mouse.RIGHT)
        return True
    elif (action == MIDDLE_CLICK):
        mouse.click(mouse.MIDDLE)
        return True
    elif (action == DOUBLE_CLICK):
        mouse.double_click()
        return True
    else:
        return False
