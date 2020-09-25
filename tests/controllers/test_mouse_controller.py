import mouse

import controllers.mouse_controller as mouseController


class TestMouseController: 
    
    def test_get_position(self):
        # get original coords
        x_old, y_old = mouseController.get_position()

        # first move mouse to 0, 0
        mouseController.move(0, 0, absolute=True)
        
        # get coordinates 
        x, y = mouseController.get_position()
        assert x == 0 and y == 0

        # restore position
        mouseController.move(x_old, y_old, absolute=True)


    def test_move_abs(self):
        # get original coords
        x_old, y_old = mouseController.get_position()

        # first move mouse to 0, 0
        mouseController.move(0, 0, absolute=True)
        
        # get coordinates 
        x, y = mouseController.get_position()
        assert x == 0 and y == 0

        # restore position
        mouseController.move(x_old, y_old, absolute=True)


    def test_move_relative(self):
        # get original coords
        x_old, y_old = mouseController.get_position()

        x_offset = 100
        y_offset = 100

        # move mouse relatively
        mouseController.move(x_offset, y_offset, absolute=False)
        
        # get coordinates 
        x_new, y_new = mouseController.get_position() 
        x_expected = x_old + x_offset 
        y_expected = y_old + y_offset
        assert x_new == x_expected
        assert y_new == y_expected

        # restore position
        mouseController.move(x_old, y_old, absolute=True)
