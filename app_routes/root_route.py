from flask import jsonify
from flask_restful import Resource


class RootRoute(Resource):
    def get(self):
        return jsonify({"api": "test workshop api"})
