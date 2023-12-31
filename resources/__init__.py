from flask import Flask
from flask_restful import Api
from resources.routes import Foo


app = Flask(__name__)
api = Api(app)


api.add_resource(Foo, '/foo')