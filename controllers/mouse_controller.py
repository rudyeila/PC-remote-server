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