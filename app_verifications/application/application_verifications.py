from .application_checks import ApplicationChecks
from app_errors.http_exceptions import HttpException


class ApplicationVerifications(ApplicationChecks):
    """
    Verifications related to thread application.
    All verifications return True if check passes, otherwise throw HttpException
    """
    def __init__(self, thread_id=None, user_id=None, value=None, by="id", model=None):
        super(ApplicationVerifications, self).__init__(
            thread_id=thread_id, user_id=user_id, value=value, by=by, model=model)

    def verify_application_exists(self):
        if self.check_application_exists():
            return True
        HttpException.throw_404(
            "Application with {by} '{value}' not found".format(by=self.by, value=self.value)
        )

    def verify_user_is_owner(self, user_id):
        self.verify_application_exists()
        if self.check_user_is_owner(user_id=user_id):
            return True
        HttpException.throw_403(
            "You must be the application owner"
        )
