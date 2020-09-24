import platform

from .volume_controller_interface import IVolumeController
from .windows_volume_controller import WinVolumeController

isWindows = True if platform.system() == "Windows" else False


class VolumeController(IVolumeController):

    OS_vol_controller: IVolumeController
    if isWindows:
        OS_vol_controller = WinVolumeController
    else:
        raise NotImplementedError(
            f"No volume controller is currently implemented for OS: {platform.system()}"
        )

    @classmethod
    def toggle_mute(cls):
        cls.OS_vol_controller.toggle_mute()

    @classmethod
    def set_mute(cls, mute: bool):
        cls.OS_vol_controller.set_mute(mute)

    @classmethod
    def get_mute(cls) -> bool:
        return cls.OS_vol_controller.get_mute()

    @classmethod
    def get_volume(cls) -> float:
        return cls.OS_vol_controller.get_volume()

    @classmethod
    def set_volume(cls, newVolume: float) -> bool:
        return cls.OS_vol_controller.set_volume(newVolume)
