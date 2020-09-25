import pytest

from controllers.volume.volume_controller import VolumeController

mute_status = False
initial_volume = 0.5

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    global mute_status, initial_volume
    # get original values
    mute_status = VolumeController.get_mute()
    initial_volume = VolumeController.get_volume()


def teardown_module(module):
    """teardown any state that was previously setup with a setup_module
    method.
    """
    global mute_status, initial_volume
    # restore value
    VolumeController.set_mute(mute_status)
    VolumeController.set_volume(initial_volume)

class TestVolumeController: 
    
    def __compare_volume(self, value1, value2, epsilon=0.00001):
        # Add margin for error due to numbers being float. We only care for the first few digits after the comma
        assert abs(value1 - value2) < 0.00001

    def test_set_volume(self):
        old_volume = VolumeController.get_volume()
        new_volume = old_volume
        if (old_volume > 0.1):
            new_volume = old_volume - 0.1
        else:
            new_volume = old_volume + 0.4

        VolumeController.set_volume(new_volume)
        
        # assert
        self.__compare_volume(VolumeController.get_volume(), new_volume)

        # restore volume 
        VolumeController.set_volume(old_volume)

    def test_set_volume_illegal_value(self):
        old_volume = VolumeController.get_volume()

        illegal_values = [-5, -0.1, 1.0001, 2, 100]
        for val in illegal_values:
            # make sure ValueError is raised
            with pytest.raises(ValueError):
                VolumeController.set_volume(val)
            # assert
            self.__compare_volume(VolumeController.get_volume(), old_volume)


    def test_get_volume(self):
        old_volume = VolumeController.get_volume()
        assert isinstance(old_volume, (int, float))
        assert old_volume > 0 and old_volume < 1.0  

    def test_set_mute(self):
        # get original mute value 
        og_mute = VolumeController.get_mute()
        # Make sure mute is off to start...
        VolumeController.set_mute(False)
        assert VolumeController.get_mute() == False 

        VolumeController.set_mute(True)
        assert VolumeController.get_mute() == True

        # restore pre-test value
        VolumeController.set_mute(og_mute)

    def test_toggle_mute(self):
        # get original mute value 
        og_mute = VolumeController.get_mute()

        # Make sure mute is off to start...
        new_mute = VolumeController.toggle_mute()
        assert VolumeController.get_mute() == (not og_mute)

        VolumeController.toggle_mute()
        assert VolumeController.get_mute() == (not new_mute)
        assert  VolumeController.get_mute() == og_mute

        # restore pre-test value
        VolumeController.set_mute(og_mute)

    def test_get_mute(self):
        # get original mute value 
        og_mute = VolumeController.get_mute()
        # Make sure mute is off to start...
        VolumeController.set_mute(False)
        assert VolumeController.get_mute() == False 

        VolumeController.set_mute(True)
        assert VolumeController.get_mute() == True

        # restore pre-test value
        VolumeController.set_mute(og_mute)
