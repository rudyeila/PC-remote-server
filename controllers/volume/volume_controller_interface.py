import abc


class IVolumeController(metaclass=abc.ABCMeta):
    @classmethod
    def toggle_mute(cls):
        """Toggles mute back and forth"""
        raise NotImplementedError

    @classmethod
    def set_mute(cls, mute: bool):
        """sets mute to specific value

        Args:
            mute (bool): whether mute or unmute
        """
        raise NotImplementedError

    @classmethod
    def get_mute(cls) -> bool:
        """returns the mute status"""
        raise NotImplementedError

    @classmethod
    def get_volume(cls) -> float:
        """returns the current volume level"""
        raise NotImplementedError

    @classmethod
    def set_volume(cls, newVolume: float) -> bool:
        """sets the volume level

        Args:
            newVolume (float): the new volume level. Must be be between 0 and 1

        Raises:
            ValueError: [should be raised when newVolume is not between 0 and 1]

        Returns:
            [bool]: returns true of the volume was changed.
        """
        raise NotImplementedError