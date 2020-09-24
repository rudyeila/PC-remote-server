from flask import Flask
from flask_restful import Resource, Api

from routes.mouse.mouse_position import MousePosition
from routes.mouse.mouse_buttons import MouseButtons
from routes.keyboard.keyboard import Keyboard
from routes.system.volume.volume import Volume
from routes.system.volume.level import Level
from routes.system.volume.mute import Mute

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# System routes
api.add_resource(Volume, '/system/volume')
api.add_resource(Level, '/system/volume/level')
api.add_resource(Mute, '/system/volume/mute')

# Mouse routes
api.add_resource(MousePosition, '/mouse/position')
api.add_resource(MouseButtons, '/mouse/buttons')

# Keyboard routes
api.add_resource(Keyboard, '/keyboard')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True, debug=True)
