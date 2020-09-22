from flask import Flask
from flask_restful import Resource, Api

from routes.mouse.mouse_position import MousePosition 
from routes.mouse.mouse_buttons import MouseButtons 
from routes.keyboard.keyboard import Keyboard


app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

api.add_resource(MousePosition, '/mouse/position')
api.add_resource(MouseButtons, '/mouse/buttons')

api.add_resource(Keyboard, '/keyboard')


app.run(host='0.0.0.0', port=80, threaded=True, debug=True)
