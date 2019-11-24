from flask_restful import Resource
import copy

from app_auth import auth
from app_errors.http_exceptions import HttpException
from app_handlers import UserHandler


class UsersUserNameRoute(Resource):
    decorators = [auth.login_required]

    def get(self, username):
        """
        @api {GET} /users/name/<String:username> Get user by username
        @apiGroup User
        @apiDescription Get user details by username

        @apiSuccessExample {JSON} Success-Response:
            {
                UserModel
            }
        """
        user_model = UserHandler().get(value=username, by="username")
        if user_model:
            # Intentional bug that returns UserModel without firstname attribute
            user_model = copy.deepcopy(user_model)
            del user_model.firstname
            return user_model.jsonify()
        HttpException.throw_404("User with username '{username}' not found".format(username=username))
