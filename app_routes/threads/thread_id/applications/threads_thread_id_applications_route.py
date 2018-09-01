from flask import request
from flask_restful import Resource, reqparse

from app_auth import auth
from app_handlers import ThreadApplicationsHandler
from app_verifications.thread import ThreadVerifications


class ThreadsThreadIdApplicationsRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        if request.method == "GET":
            self.reqparse.add_argument("start", type=int, required=False, location="values")
            self.reqparse.add_argument("limit", type=int, required=False, location="values")

        super(ThreadsThreadIdApplicationsRoute, self).__init__()

    def get(self, thread_id):
        """
        @api {GET} /threads/<String:thread_id>/applications Get received thread applications
        @apiGroup Thread
        @apiDescription Get received thread applications as thread owner
        """
        args = self.reqparse.parse_args()
        caller_user_id = auth.user_id

        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        # Verify thread exists
        thread_verifications.verify_thread_exists()
        # Verify user is thread owner
        thread_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Get thread applications
        thread_application_models = ThreadApplicationsHandler().get(
            thread_id=thread_id,
            start=args.start,
            limit=args.limit
        )

        return thread_application_models.jsonify()
