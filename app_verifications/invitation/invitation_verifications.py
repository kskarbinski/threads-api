from .invitation_checks import InvitationChecks
from app_errors.http_exceptions import HttpException


class InvitationVerifications(InvitationChecks):
    """
    Verifications related to thread invitation.
    All verifications return True if check passes, otherwise throw HttpException
    """
    def __init__(self, thread_id=None, user_id=None, value=None, by="id", model=None):
        super(InvitationVerifications, self).__init__(
            thread_id=thread_id, user_id=user_id, value=value, by=by, model=model)

    def verify_invitation_exists(self):
        if self.check_invitation_exists():
            return True
        HttpException.throw_404(
            "Invitation with {by} '{value}' not found".format(by=self.by, value=self.value)
        )

    def verify_user_is_owner(self, user_id):
        self.verify_invitation_exists()
        if self.check_user_is_owner(user_id=user_id):
            return True
        HttpException.throw_403(
            "You must be the invitation owner"
        )

    def verify_user_is_invitee(self, user_id):
        self.verify_invitation_exists()
        if self.check_user_is_invitee(user_id=user_id):
            return True
        HttpException.throw_403(
            "You must be the invitee"
        )

    def verify_user_is_invitee_or_inviter(self, user_id):
        self.verify_invitation_exists()
        if self.check_user_is_owner(user_id=user_id) or self.check_user_is_invitee(user_id=user_id):
            return True
        HttpException.throw_403(
            "You must be the inviter or invitee"
        )
