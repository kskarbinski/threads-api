from .user_checks import UserChecks
from app_errors.http_exceptions import HttpException


class UserVerifications(UserChecks):
    """
    Verifications related to user/users.
    All verifications return True if check passes, otherwise throw HttpException
    """
    def __init__(self, value=None, by="id", model=None):
        super(UserVerifications, self).__init__(value=value, by=by, model=model)

    def verify_user_exists(self):
        if self.check_user_exists():
            return True
        HttpException.throw_404(
            "User with {by} '{value}' not found".format(by=self.by, value=self.value)
        )
