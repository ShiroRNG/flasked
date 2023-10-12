from flask_restful import Resource


class Foo(Resource):
    def get(self):
        return 'Hello World!', 200

    def post(self):
        pass