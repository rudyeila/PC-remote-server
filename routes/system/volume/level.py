from flask import request
from flask_restful import Resource, reqparse
from utils.errors import error_response

from controllers.volume.volume_controller import VolumeController


class Level(Resource):

    def get(self):
        try:
            volume = VolumeController.get_volume()
            return {"volume": volume}, 200
        except Exception as err:
            return error_response(err)

    def put(self):
        try:
            args = request.get_json()
            VolumeController.set_volume(args['volume'])
            return self.get()
        except Exception as err:
            return error_response(err)
