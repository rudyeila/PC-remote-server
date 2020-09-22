from flask import make_response, request
from flask_restful import Resource, reqparse

import controllers.mouse_controller as mouseController

from utils.errors import error_response


__parser = reqparse.RequestParser()
__parser.add_argument('x', type=int, required=True,
                      help='The new X coordinate of the mouse')
__parser.add_argument('y', type=int, required=True,
                      help='The new Y coordinate of the mouse')
__parser.add_argument(
    'absolute', default=False, type=bool, help='Should the new mouse coordinates be absolute or relative?')
__parser.add_argument(
    'duration', default=0, type=int, help='The duration of the movement animation, if required.')


class MousePosition(Resource):

    def get(self):
        try:
            pos_x, pos_y = mouseController.get_position()
            return {'data': {
                'pos_x': pos_x,
                'pos_y': pos_y,
            }}
        except Exception as err:
            return error_response(err, 500)

    def post(self):
        try:
            reqbody = __parser.parse_args()
            mouseController.move_mouse(
                reqbody.x, reqbody.y, reqbody.absolute, reqbody.duration)
            return self.get()
        except Exception as err:
            return error_response(err, 500)