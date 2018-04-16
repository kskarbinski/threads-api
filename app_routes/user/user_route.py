from flask import abort
from flask_restful import Resource

from app_auth import auth


class UserRoute(Resource):
    decorators = [auth.login_required]

    def get(self):
        user_model = auth.user_model
        if user_model:
            return user_model.jsonify()
        else:
            abort(500, "Error in user_route.py::UserRoute::get")
