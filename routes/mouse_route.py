

from flask import make_response
from flask_restful import Resource

from controllers.mouse_controller import MouseController



class Mouse(Resource):
    mouseController = MouseController()

    def get(self):
        try:
            pos_x, pos_y = Mouse.mouseController.get_position()
            return {'data': {
                'pos_x': pos_x,
                'pos_y': pos_y,
            }}
        except Exception as err:
            return make_response({'error': str(err)}, 500)
