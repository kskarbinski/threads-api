from flask_restful import Resource

from app_auth import auth
from app_errors.http_exceptions import HttpException
from app_handlers import UserHandler


class UsersUserIdRoute(Resource):
    decorators = [auth.login_required]

    def get(self, user_id):
        """
        @api {GET} /users/<String:user_id> Get user by id
        @apiGroup User
        @apiDescription Get user details by id

        @apiSuccessExample {JSON} Success-Response:
            {
                UserModel
            }
        """
        user_model = UserHandler().get(value=user_id)
        if user_model:
            return user_model.jsonify()
        HttpException.throw_404("User with id '{user_id}' not found".format(user_id=user_id))
