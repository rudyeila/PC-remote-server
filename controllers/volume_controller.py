from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL

from pythoncom import CoInitialize
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume


class VolumeController:

    mute_status: bool = False

    # Saves the volume when muting in order to restore it after
    __volume_before_muting: float = 0.8

    CoInitialize()
    __devices = AudioUtilities.GetSpeakers()
    __interface = __devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    __volume = cast(__interface, POINTER(IAudioEndpointVolume))
    __sessions = AudioUtilities.GetAllSessions()

    @classmethod
    def refresh_devices(cls):
        CoInitialize()
        cls.__devices = AudioUtilities.GetSpeakers()
        cls.__interface = __devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        cls.__volume = cast(__interface, POINTER(IAudioEndpointVolume))
        cls.__sessions = AudioUtilities.GetAllSessions()

    @classmethod
    def toggle_mute(cls):
        if cls.mute_status:
            cls.__unmute()
        else:
            cls.__mute()

    @classmethod
    def __mute(cls):
        cls.__volume_before_muting = cls.get_volume()
        cls.set_volume(0)
        cls.mute_status = True

    @classmethod
    def __unmute(cls):
        cls.set_volume(cls.__volume_before_muting)
        cls.mute_status = False

    @classmethod
    def set_mute(cls, mute: bool):
        if not type(mute) == bool:
            raise ValueError(f"Illegal value when setting mute: {mute}")
        if mute:
            cls.__mute()
        else:
            cls.__unmute()

    @classmethod
    def get_mute(cls):
        return cls.mute_status

    @classmethod
    def get_volume(cls):
        volume = cls.__volume.GetMasterVolumeLevelScalar()
        return volume

    @classmethod
    def set_volume(cls, newVolume: float):
        if not isinstance(newVolume, (int, float)):
            raise ValueError(f"Illegal value when setting volume: {newVolume}")
        if newVolume < 0 or newVolume > 1:
            raise ValueError("Volume value must be between 0 and 1")
        cls.__volume.SetMasterVolumeLevelScalar(newVolume, None)
        return True
