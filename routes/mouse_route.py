

from flask import make_response, request
from flask_restful import Resource, reqparse

from controllers.mouse_controller import MouseController


class Mouse(Resource):
    mouseController = MouseController()

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
            pos_x, pos_y = Mouse.mouseController.get_position()
            return {'data': {
                'pos_x': pos_x,
                'pos_y': pos_y,
            }}
        except Exception as err:
            return make_response({'error': str(err)}, 500)

    def put(self):
        try:
            args = self.__parser.parse_args()
            print(args)
            Mouse.mouseController.move_mouse(args.x, args.y, args.absolute, args.duration)
            return "success", 200
        except Exception as err:
            return make_response({'error': str(err)}, 500)
