from flask_restful import Resource, reqparse

from 
from utils.errors import error_response

__parser = reqparse.RequestParser()
__parser.add_argument("hotkey", type=str or int, required=True)

class Keyboard(Resource):
    
    def post(self):
        try:
            args = __parser.parse_args()
            keyboard.press_and_release(args.hotkey)
        except Exception as err: 
            return error_response(err)