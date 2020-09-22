from flask import make_response, request
from flask_restful import Resource, reqparse

import controllers.mouse_controller as mouseController
from controllers.mouse_controller import MouseClicks

from utils.errors import error_response


__parser = reqparse.RequestParser()
__parser.add_argument(
    'action',
    type=str,
    choices=[MouseClicks.LEFT_CLICK, MouseClicks.RIGHT_CLICK,
             MouseClicks.DOUBLE_CLICK, MouseClicks.MIDDLE_CLICK],
    required=True,
    help='The action to perform on the mouse resource'
)


class MouseButtons(Resource):

    """Perform a mouse click action """
    def post(self):
        try:
            args = __parser.parse_args()
            result = mouseController.perform_action(args.action)
            if (result):
                return {"data": {"action": args.action, "result": "success"}}, 200
            return error_response("undefined action", 400)
        except Exception as err:
            print(err)
            return error_response(err, 500)
