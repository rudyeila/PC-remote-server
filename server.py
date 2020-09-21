from flask import Flask
from flask_restful import Resource, Api

from routes.mouse_route import Mouse 


app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

api.add_resource(Mouse, '/mouse')


app.run(host='0.0.0.0', port=80, threaded=True,)
