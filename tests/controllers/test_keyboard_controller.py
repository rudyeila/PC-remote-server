import keyboard

import controllers.keyboard_controller as keyboardController


class TestKeyboardController: 
    
    callback_called = False 
        
    def __on_press_callback(self):
        """This function will be called as a callback when a specific key is pressed (will be defined in the test)
        thus confirming that the the key was indeed pressed.
        """
        self.callback_called = True 
        assert True

    def test_press_key(self):
        key = "space"
        # Calls the above defined callback upon pressing the specified key. 
        # So if the callback was called then the key was indeed pressed
        keyboard.on_press_key(key, self.__on_press_callback())

        keyboardController.press_and_release(key)
        assert self.callback_called

        # make sure key is released.
        assert not keyboard.is_pressed(key)

        # reset var 
        self.callback_called = False
