from flask import request
from flask_restful import Resource, reqparse

from app_auth import auth
from app_handlers import ThreadsApplicationsHandler


class ThreadsApplicationsRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        if request.method == "GET":
            self.reqparse.add_argument("start", type=int, required=False, location="values")
            self.reqparse.add_argument("limit", type=int, required=False, location="values")

        super(ThreadsApplicationsRoute, self).__init__()

    def get(self):
        args = self.reqparse.parse_args()
        caller_user_id = auth.user_id

        # Get sent applications to all threads
        thread_application_models = ThreadsApplicationsHandler().get(
            user_id=caller_user_id,
            start=args.start,
            limit=args.limit
        )

        return thread_application_models.jsonify()
