from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run(debug=True, host='0.0.0.0', port=80, threaded=True,)
