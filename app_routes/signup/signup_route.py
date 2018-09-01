from flask_restful import Resource, reqparse

from app_utils.validators.length import validate_length
from app_handlers import SignupHandler
from app_errors.http_exceptions import HttpException
from app_verifications.user import UserVerifications


class SignupRoute(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(name="username", type=str, required=True, location="json")
        self.reqparse.add_argument(name="password", type=str, required=True, location="json")
        self.reqparse.add_argument(name="firstname", type=str, required=True, location="json")
        self.reqparse.add_argument(name="lastname", type=str, required=True, location="json")
        super(SignupRoute, self).__init__()

    def post(self):
        """
        @api {POST} /signup Signup
        @apiGroup User

        @apiParam (JSON param) {String} username Username. Has to be unique, cannot be a number, length 2-20
        @apiParam (JSON param) {String} password Password. Length 4-20
        @apiParam (JSON param) {String} firstname First name. Length 2-20
        @apiParam (JSON param) {String} lastname Last name. Length 2-50
        """
        args = self.reqparse.parse_args()

        # Verify username
        if UserVerifications(by="username", value=args.username).check_user_exists():
            HttpException.throw_409("Username already taken")
        elif args.username.isdigit():
            HttpException.throw_422("Username must not be a number")
        elif not validate_length(2, 20, args.username):
            HttpException.throw_422("Username length must be between 2 and 20 characters")
        # Verify password
        elif not validate_length(4, 20, args.password):
            HttpException.throw_422("password length must be between 4 and 20 characters")
        # Verify firstname
        elif not validate_length(2, 20, args.firstname):
            HttpException.throw_422("First name length must be between 2 and 20 characters")
        # Verify lastname
        elif not validate_length(2, 50, args.lastname):
            HttpException.throw_422("Last name length must be between 2 and 50 characters")
        # Register user
        user_model = SignupHandler().post(
            username=args.username,
            password=args.password,
            firstname=args.firstname,
            lastname=args.lastname
        )

        return user_model.jsonify()
