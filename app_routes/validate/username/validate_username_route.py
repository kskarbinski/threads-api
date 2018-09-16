from flask_restful import Resource, reqparse

from app_data.users import users
from app_utils.validators.length import validate_length
from app_utils.helpers.finders import FindModel
from app_models import UsernameValidationModel


class ValidateUsernameRoute(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(name="username", type=str, required=True, location="values")
        super(ValidateUsernameRoute, self).__init__()

    def get(self):
        """
        @api {GET} /validate/<String:username> Validate username
        @apiGroup User
        @apiDescription Validate username. Check whether it's already taken and has correct format

        @apiSuccessExample {JSON} Success-Response:
            {
                UserValidationModel
            }
        """
        args = self.reqparse.parse_args()

        username_validation_model = UsernameValidationModel()

        user_model = FindModel(models_list=users).by_username(args.username)
        if user_model:
            username_validation_model.errors.append("Username already taken")
            return username_validation_model.jsonify()
        if args.username.isdigit():
            username_validation_model.errors.append("Username must not be a number")
        if not validate_length(2, 20, args.username):
            username_validation_model.errors.append("Username length must be between 2 and 20 characters")

        return username_validation_model.jsonify()
