from app_verifications import BaseChecks
from app_data.threads import threads_invitations, users_thread_invitations


class InvitationChecks(BaseChecks):
    """
    Checks related to thread invitation.
    All checks return True or False.
    """
    def __init__(self, thread_id=None, user_id=None, value=None, by="id", model=None):
        assert thread_id or user_id, "Get invitation by user id or thread id"
        if thread_id is not None:
            container = threads_invitations[thread_id]
        else:
            container = users_thread_invitations[user_id]

        super(InvitationChecks, self).__init__(
            container=container,
            value=value,
            by=by,
            model=model
        )
        self.thread_invitation_model = self.model

    def check_invitation_exists(self):
        return True if self.thread_invitation_model else False

    def check_user_is_owner(self, user_id):
        return True if self.thread_invitation_model.invited_by == user_id else False

    def check_user_is_invitee(self, user_id):
        return True if self.thread_invitation_model.user == user_id else False
