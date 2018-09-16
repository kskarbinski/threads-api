from flask_restful import Resource, reqparse
from flask import request

from app_auth import auth
from app_handlers import ThreadInvitationsHandler
from app_verifications.thread import ThreadVerifications


class ThreadsThreadIdInvitationsRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        if request.method == "GET":
            self.reqparse.add_argument("start", type=int, required=False, location="values")
            self.reqparse.add_argument("limit", type=int, required=False, location="values")

        super(ThreadsThreadIdInvitationsRoute, self).__init__()

    def get(self, thread_id):
        """
        @api {GET} /threads/<String:thread_id>/invitations Get sent thread invitations
        @apiGroup Thread
        @apiDescription Get sent thread invitations

        @apiSuccessExample {JSON} Success-Response:
            {
                "items": ThreadInvitationModel[]
            }
        """
        args = self.reqparse.parse_args()
        caller_user_id = auth.user_id

        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        # Verify thread exists
        thread_verifications.verify_thread_exists()
        # Verify user is thread owner
        thread_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Get thread invitations
        thread_invitation_models = ThreadInvitationsHandler().get(
            thread_id=thread_id,
            start=args.start,
            limit=args.limit
        )

        return thread_invitation_models.jsonify()
