from flask import request
from flask_restful import Resource, reqparse

from app_auth import auth
from app_handlers import ThreadsHandler


class ThreadsRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        if request.method == "GET":
            self.reqparse.add_argument("start", type=int, required=False, location="values")
            self.reqparse.add_argument("limit", type=int, required=False, location="values")
        elif request.method == "POST":
            self.reqparse.add_argument(name="name", type=str, required=True, location="json")
            self.reqparse.add_argument(name="private", type=bool, required=True, location="json")

        super(ThreadsRoute, self).__init__()

    def get(self):
        args = self.reqparse.parse_args()

        # Get paginated threads
        paginated_threads = ThreadsHandler().get(
            start=args.start,
            limit=args.limit
        )

        # Return paginated threads
        return paginated_threads.jsonify()

    def post(self):
        args = self.reqparse.parse_args()
        user_id = auth.user_id

        # Create thread
        thread_model = ThreadsHandler().post(
            user_id=user_id,
            name=args.name,
            private=args.private
        )

        # Return thread
        return thread_model.jsonify()
