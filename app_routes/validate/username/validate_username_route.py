from flask import jsonify
from flask_restful import Resource, reqparse

from app_data.users import users
from app_utils.validators.length import validate_length
from app_utils.helpers.finders import FindModel


class ValidateUsernameRoute(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(name="username", type=str, required=True, location="json")
        super(ValidateUsernameRoute, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()

        response = {"errors": []}

        user_model = FindModel(models_list=users).by_username(args.username)
        if user_model:
            response["errors"].append("Username already taken")
            return jsonify(response)
        if args.username.isdigit():
            response["errors"].append("Username must not be a number")
        if not validate_length(2, 20, args.username):
            response["errors"].append("Username length must be between 2 and 20 characters")

        return jsonify(response)
