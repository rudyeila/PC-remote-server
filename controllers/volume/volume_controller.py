import platform

from .volume_controller_interface import IVolumeController
from .windows_volume_controller import WinVolumeController

isWindows = True if platform.system() == "Windows" else False

class VolumeControllerError(BaseException):
    pass


class VolumeController(IVolumeController):

    __OS_vol_controller: IVolumeController
    if isWindows:
        try:
            __OS_vol_controller = WinVolumeController
        except Exception: 
            raise VolumeControllerError("It seems like there are no sound devices available. ")
    else:
        raise NotImplementedError(
            f"No volume controller is currently implemented for OS: {platform.system()}"
        )  

    @classmethod
    def toggle_mute(cls) -> bool:
        return cls.__OS_vol_controller.toggle_mute()

    @classmethod
    def set_mute(cls, mute: bool):
        cls.__OS_vol_controller.set_mute(mute)

    @classmethod
    def get_mute(cls) -> bool:
        return cls.__OS_vol_controller.get_mute()

    @classmethod
    def get_volume(cls) -> float:
        return cls.__OS_vol_controller.get_volume()

    @classmethod
    def set_volume(cls, newVolume: float) -> bool:
        return cls.__OS_vol_controller.set_volume(newVolume)
