from flask import jsonify, abort
from flask_restful import Resource

from app_auth import auth

from app_data.users import users


class UserRoute(Resource):
    decorators = [auth.login_required]

    def get(self, phrase):
        pass
