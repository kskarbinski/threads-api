from flask_restful import Resource, reqparse

from app_auth import auth
from app_handlers import UsersHandler


class UsersRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("start", type=int, required=False, location="values")
        self.reqparse.add_argument("limit", type=int, required=False, location="values")
        super(UsersRoute, self).__init__()

    def get(self):
        """
        @api {GET} /users Get users
        @apiGroup User
        @apiDescription Get last 100 created users

        @apiSuccessExample {JSON} Success-Response:
            {
                "items": UserModel[]
            }
        """
        args = self.reqparse.parse_args()

        user_models = UsersHandler().get(
            start=args.start,
            limit=args.limit
        )

        return user_models.jsonify()
