from flask_restful import Resource

from app_auth import auth
from app_handlers import ThreadInvitationHandler
from app_verifications.thread import ThreadVerifications
from app_verifications.invitation import InvitationVerifications


class ThreadsThreadIdInvitationsInvitationIdRoute(Resource):
    decorators = [auth.login_required]

    def get(self, thread_id, invitation_id):
        """
        @api {GET} /threads/<String:thread_id>/invitations/<String:invitation_id> Get sent thread invitation
        @apiGroup Thread
        @apiDescription Get sent thread invitation

        @apiSuccessExample {JSON} Success-Response:
            {
                ThreadInvitationModel
            }
        """
        caller_user_id = auth.user_id

        # Verifications

        # Thread verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        # Verify user is thread owner
        thread_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Invitation verifications
        invitation_verifications = InvitationVerifications(thread_id=thread_id, value=invitation_id)
        # Verify user is invitation owner
        invitation_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Get thread invitation
        thread_invitation_model = ThreadInvitationHandler().get(
            thread_id=thread_id,
            invitation_id=invitation_id
        )

        return thread_invitation_model.jsonify()

    def delete(self, thread_id, invitation_id):
        """
        @api {DELETE} /threads/<String:thread_id>/invitations/<String:invitation_id> Cancel sent thread invitation
        @apiGroup Thread
        @apiDescription Cancel sent thread invitation

        @apiSuccessExample {JSON} Success-Response:
            {
                ThreadInvitationModel
            }
        """
        caller_user_id = auth.user_id

        # Verifications

        # Thread verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        # Verify user is thread owner
        thread_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Invitation verifications
        invitation_verifications = InvitationVerifications(thread_id=thread_id, value=invitation_id)
        thread_invitation_model = invitation_verifications.thread_invitation_model
        # Verify user is invitation owner
        invitation_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Update invitation and mark as deleted
        ThreadInvitationHandler().delete(
            thread_invitation_model=thread_invitation_model
        )

        return thread_invitation_model.jsonify()
