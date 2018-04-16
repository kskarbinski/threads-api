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
        args = self.reqparse.parse_args()

        paginated_threads = UsersHandler().get(
            start=args.start,
            limit=args.limit
        )

        return paginated_threads.jsonify()
