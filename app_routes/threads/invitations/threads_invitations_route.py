from flask_restful import Resource, reqparse
from flask import request

from app_auth import auth
from app_handlers import ThreadsInvitationsHandler


class ThreadsInvitationsRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        if request.method == "GET":
            self.reqparse.add_argument("start", type=int, required=False, location="values")
            self.reqparse.add_argument("limit", type=int, required=False, location="values")

        super(ThreadsInvitationsRoute, self).__init__()

    def get(self):
        """
        @api {GET} /threads/invitations Get received thread invitations
        @apiDescription Get last 100 received thread applications for current user
        @apiGroup Thread
        """
        args = self.reqparse.parse_args()
        caller_user_id = auth.user_id

        # Get received invitations to all threads
        thread_invitation_models = ThreadsInvitationsHandler().get(
            user_id=caller_user_id,
            start=args.start,
            limit=args.limit
        )

        return thread_invitation_models.jsonify()
