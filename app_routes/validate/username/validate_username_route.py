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
        @api {GET} /validate/username Validate username
        @apiGroup User
        @apiDescription Validate username. Check whether it's already taken and has correct format
        @apiParam (URL query param) {String} username Validate username. Has to be unique, must not be a number, length 2-20

        @apiSuccessExample {JSON} Success-Response:
            {
                UserValidationModel
            }
        """
        args = self.reqparse.parse_args()

        errors = []

        user_model = FindModel(models_list=users).by_username(args.username)
        if user_model:
            errors.append("Username already taken")
            return UsernameValidationModel(errors=errors).jsonify()
        if args.username.isdigit():
            errors.append("Username must not be a number")
        if not validate_length(2, 20, args.username):
            errors.append("Username length must be between 2 and 20 characters")

        return UsernameValidationModel(errors=errors).jsonify()
