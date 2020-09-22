from enum import Enum
from typing import Tuple

# https://github.com/boppreh/mouse
import mouse


class MouseClicks(Enum):
    LEFT_CLICK = 0
    RIGHT_CLICK = 1
    MIDDLE_CLICK = 2
    DOUBLE_CLICK = 3




def get_position() -> Tuple[int, int]:
    """Get the current x and y coordinates of the mouse

    Returns
    -------
    tuple of ints
        (x, y) coordinates of the mouse
    """
    return mouse.get_position()

def move_mouse(x: int, y: int, absolute=True, duration=0):
    mouse.move(x, y, absolute, duration)

def perform_action(action: str):  # Change action type from string to predefined costants
    if (action == MouseClicks.LEFT_CLICK):
        mouse.click()
        return True
    elif (action == MouseClicks.RIGHT_CLICK):
        mouse.click(mouse.RIGHT)
        return True
    elif (action == MouseClicks.MIDDLE_CLICK):
        mouse.click(mouse.MIDDLE)
        return True
    elif (action == MouseClicks.DOUBLE_CLICK):
        mouse.double_click()
        return True
    else:
        return False
