'''
Created on 14 nov. 2018

@author: saparicio
'''

from flask import Flask, send_file
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class RetrieveFile(Resource):
    def __init__(self):
        self.filename = "concurrent.py"
    def get(self):
        return send_file(self.filename, mimetype='application/octet-stream')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

api.add_resource(RetrieveFile, '/file')

if __name__ == '__main__':
    app.run(debug=False)
