from flask import request
from flask_restful import Resource, reqparse
from utils.errors import error_response

from controllers.volume.volume_controller import VolumeController


class Volume(Resource):

    def get(self):
        try:
            mute = VolumeController.get_mute()
            volume = VolumeController.get_volume() 
            return {"volume": volume, "mute": mute}, 200
        except Exception as err:
            return error_response(err)
