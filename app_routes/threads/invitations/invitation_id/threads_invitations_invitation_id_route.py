from flask_restful import Resource, reqparse
from flask import request

from app_auth import auth
from app_handlers import ThreadInvitationHandler
from app_verifications.invitation import InvitationVerifications


class ThreadsInvitationsInvitationIdRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        if request.method == "POST":
            self.reqparse.add_argument(name="accept", type=bool, required=True, location="json")

        super(ThreadsInvitationsInvitationIdRoute, self).__init__()

    def get(self, invitation_id):
        """
        @api {GET} /threads/invitations/<String:invitation_id> Get received thread invitation
        @apiDescription Get received thread invitation by id
        @apiGroup Thread

        @apiSuccessExample {JSON} Success-Response:
            {
                ThreadInvitationModel
            }
        """
        caller_user_id = auth.user_id

        # Verifications

        # Invitation verifications
        invitation_verifications = InvitationVerifications(user_id=caller_user_id, value=invitation_id)
        # Verify user is invitee
        invitation_verifications.verify_user_is_invitee(user_id=caller_user_id)

        # Get thread invitation
        thread_invitation_model = ThreadInvitationHandler().get(
            thread_id=invitation_verifications.thread_invitation_model.thread,
            invitation_id=invitation_id
        )

        return thread_invitation_model.jsonify()

    def post(self, invitation_id):
        """
        @api {POST} /threads/invitations/<String:invitation_id> Accept or reject thread invitation
        @apiGroup Thread

        @apiParam (JSON param) {Boolean} accept Accept or reject the invitation

        @apiSuccessExample {JSON} Success-Response:
            {
                ThreadInvitationModel
            }
        """
        caller_user_id = auth.user_id
        args = self.reqparse.parse_args()

        # Verifications

        # Invitation verifications
        invitation_verifications = InvitationVerifications(user_id=caller_user_id, value=invitation_id)
        thread_invitation_model = invitation_verifications.thread_invitation_model
        # Verify user is invitee
        invitation_verifications.verify_user_is_invitee(user_id=caller_user_id)

        # Update invitation and mark as accepted or rejected
        ThreadInvitationHandler().post(
            thread_invitation_model=thread_invitation_model,
            accept=args.accept
        )

        return thread_invitation_model.jsonify()
