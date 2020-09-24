from flask_restful import Resource, reqparse

import controllers.mouse_controller as mouseController

from utils.errors import error_response

class Mouse(Resource):

    """Get mouse coordinates"""

    def get(self):
        try:
            pos_x, pos_y = mouseController.get_position()
            return {
                "x": pos_x,
                "y": pos_y,
            }
        except Exception as err:
            return error_response(err, 500)
