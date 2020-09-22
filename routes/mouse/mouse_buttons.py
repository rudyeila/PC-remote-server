from flask import make_response, request
from flask_restful import Resource, reqparse

import controllers.mouse_controller as mouseController
from utils.errors import error_response

class MouseButtons(Resource):

    def __init__(self):
        self.__parser = reqparse.RequestParser()
        # choices=["MOVE, LEFT_CLICK, RIGHT_CLICK, DOUBLE_CLICK, MIDDLE_CLICK"]
        self.__parser.add_argument('action', type=str, choices=[
                                   "MOVE, LEFT_CLICK, RIGHT_CLICK, DOUBLE_CLICK, MIDDLE_CLICK"], required=True, help='The action to perform on the mouse resource')

        self.__move_parser = reqparse.RequestParser()
        self.__move_parser.add_argument('action', type=str, choices=[
                                        "MOVE"], default="MOVE", help='The action to perform on the mouse resource')
        self.__move_parser.add_argument('x', type=int, required=True,
                                        help='The new X coordinate of the mouse')
        self.__move_parser.add_argument('y', type=int, required=True,
                                        help='The new Y coordinate of the mouse')
        self.__move_parser.add_argument(
            'absolute', default=True, type=bool, help='Should the new mouse coordinates be absolute or relative?')
        self.__move_parser.add_argument(
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
            body = request.get_json()
            print(body)
            # if ('action' not in body):
            #     return {"error": "Invalid Syntax. You must provide an action to perform on the mouse resource"}, 400
            action = body['action']
            if (action == "MOVE"):
                reqbody = self.__move_parser.parse_args()
                mouseController.move_mouse(
                    reqbody.x, reqbody.y, reqbody.absolute, reqbody.duration)
                return self.get()

            result = mouseController.perform_action(action)
            if (result):
                return {"data": {"action": action, "result": "success"}}, 200
            return error_response("undefined action", 400)
        except Exception as err:
            print(err)
            return error_response(err, 500)
