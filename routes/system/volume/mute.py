from flask import request
from flask_restful import Resource, reqparse
from utils.errors import error_response

from controllers.volume_controller import VolumeController


class Mute(Resource):

    def get(self):
        try:
            mute = VolumeController.get_mute()
            return {"mute": mute}, 200
        except Exception as err:
            return error_response(err)

    def post(self):
        try:
            args = request.get_json()
            if (args is not None and 'mute' in args):
                VolumeController.set_mute(args['mute'])
            else: 
                VolumeController.toggleMute()
            return self.get()
        except Exception as err:
            return error_response(err)
