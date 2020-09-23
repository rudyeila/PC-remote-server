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
    __interface = __devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    __volume = cast(__interface, POINTER(IAudioEndpointVolume))
    __sessions = AudioUtilities.GetAllSessions()

    @classmethod
    def toggleMute(cls):
        if (cls.mute_status):
            cls.unmute()
        else: 
            cls.mute()

    @classmethod
    def mute(cls):
        cls.__volume_before_muting = cls.get_volume()
        cls.set_volume(0)
        cls.mute_status = True

    @classmethod
    def unmute(cls):
        cls.set_volume(cls.__volume_before_muting)
        cls.mute_status = False

    @classmethod
    def set_mute(cls, mute: bool):
        print(f"set_mute: {mute}")
        if (mute):
            cls.mute()
        else:
            cls.unmute()

    @classmethod
    def get_mute(cls):
        return cls.mute_status

    @classmethod
    def get_volume(cls):
        volume = cls.__volume.GetMasterVolumeLevelScalar()
        return volume

    @classmethod
    def set_volume(cls, newVolume: float):
        if (newVolume < 0 or newVolume > 1):
            raise ValueError("Volume value must be between 0 and 1")
        cls.__volume.SetMasterVolumeLevelScalar(newVolume, None)
        return True
