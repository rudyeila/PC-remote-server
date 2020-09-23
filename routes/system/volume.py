from flask import request
from flask_restful import Resource, reqparse
from utils.errors import error_response

from controllers.volume_controller import VolumeController

volumeController = VolumeController()

class Volume(Resource):

    def get(self):
        try:
            # volumeController.mute()
            volume = volumeController.get_volume()
            return {"data": {"volume": volume, "status": "success"}}, 200
        except Exception as err:
            return error_response(err)


    def put(self):
        try:
            # volumeController.mute()
            args = request.get_json()
            volumeController.set_volume(args['volume'])
            return self.get()
        except Exception as err:
            return error_response(err)