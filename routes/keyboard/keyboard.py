from flask_restful import Resource, reqparse

import controllers.keyboard_controller as keyboardController
from utils.errors import error_response

_parser = reqparse.RequestParser()
_parser.add_argument("hotkey", type=str or int, required=True)
_parser.add_argument("hold", type=bool, default=False)


class Keyboard(Resource):

    def post(self):
        try:
            args = _parser.parse_args()
            keyboardController.handle_request(args)
            return {"data": {"status": "success"}}, 200
        except Exception as err:
            return error_response(err)
