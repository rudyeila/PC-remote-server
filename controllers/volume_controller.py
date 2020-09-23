from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL

from pythoncom import CoInitialize
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume


class VolumeController:

    def __init__(self):
        CoInitialize()
        self.__devices = AudioUtilities.GetSpeakers()
        self.__interface = self.__devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.__volume = cast(self.__interface, POINTER(IAudioEndpointVolume))
        self.__sessions = AudioUtilities.GetAllSessions()
        self.__volume_before_muting = self.get_volume()

    def mute(self):
        for session in self.__sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            oldMute = volume.GetMute()
            print(f"volume.GetMute(): {volume.GetMute()}")
            newMute = 0
            if (oldMute == 0):
                newMute = 1
            volume.SetMute(newMute, None)

    def setMute(self, mute: bool):
        if (mute):
            self.set_volume(0)
        else:
            self.set_volume(self.__volume_before_muting)

    def get_volume(self):
        volume = self.__volume.GetMasterVolumeLevelScalar()
        # scaled_volume = convert_value_to_100_scale(volume)
        # self.__volume_before_muting = scaled_volume
        return volume

    def set_volume(self, newVolume: float):
        if (newVolume < 0 or newVolume > 1):
            raise ValueError("Volume value must be between 0 and 1")
        # volume = convert_value_to_weird_scale(newVolume)
        # print(f"Volume in weird scale: {volume}")
        self.__volume.SetMasterVolumeLevelScalar(newVolume, None)
        self.__volume_before_muting = self.get_volume()
        return True
