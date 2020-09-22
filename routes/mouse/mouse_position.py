from flask import make_response, request
from flask_restful import Resource, reqparse

import controllers.mouse_controller as mouseController

from utils.errors import error_response


class MousePosition(Resource):

    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('x', type=int, required=True,
                                        help='The new X coordinate of the mouse')
        self.__parser.add_argument('y', type=int, required=True,
                                        help='The new Y coordinate of the mouse')
        self.__parser.add_argument(
            'absolute', default=True, type=bool, help='Should the new mouse coordinates be absolute or relative?')
        self.__parser.add_argument(
            'duration', default=0, type=int, help='The duration of the movement animation, if required.')

    def get(self):
        try:
            pos_x, pos_y = mouseController.get_position()
            return {'data': {
                'pos_x': pos_x,
                'pos_y': pos_y,
            }}
        except Exception as err:
            return error_response(err, 500)

    def put(self):
        try:
            reqbody = self.__parser.parse_args()
            mouseController.move_mouse(reqbody.x, reqbody.y, reqbody.absolute, reqbody.duration)
            return self.get()

            # result = MousePosition.mouseController.perform_action(action)
            # if (result):
            #     return {"data": {"action": action, "result": "success"}}, 200
            # return error_response("undefined action", 400)
        except Exception as err:
            return error_response(err, 500)
