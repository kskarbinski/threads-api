from flask_restful import Resource

from app_auth import auth
from app_errors.http_exceptions import HttpException
from app_handlers import UserHandler


class UsersUserNameRoute(Resource):
    decorators = [auth.login_required]

    def get(self, username):
        user_model = UserHandler().get(value=username, by="username")
        if user_model:
            return user_model.jsonify()
        HttpException.throw_404("User with username '{username}' not found".format(username=username))
