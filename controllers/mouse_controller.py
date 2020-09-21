from typing import Tuple

# https://github.com/boppreh/mouse
import mouse


class MouseController:

    def get_position(self) -> Tuple[int, int]:
        """Get the current x and y coordinates of the mouse 

        Returns
        -------
        tuple of ints
            (x, y) coordinates of the mouse 
        """
        return mouse.get_position()

    def move_mouse(self, x: int, y: int, absolute=True, duration=0):
        mouse.move(x, y, absolute, duration)

    def perform_action(self, action: str): # Change action type from string to predefined costants
        if (action == "LEFT_CLICK"):
            mouse.click()
            return True
        elif (action == "RIGHT_CLICK"):
            mouse.click(mouse.RIGHT)
            return True
        elif (action == "MIDDLE_CLICK"):
            mouse.click(mouse.MIDDLE)
            return True
        elif (action == "DOUBLE_CLICK"):
            mouse.double_click()
            return True
        else: 
            return False