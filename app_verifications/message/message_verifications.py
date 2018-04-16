from .message_checks import MessageChecks
from app_errors.http_exceptions import HttpException


class MessageVerifications(MessageChecks):
    """
    Every method verifies something related to thread. If verification does not pass a HttpException is thrown.
    """
    def __init__(self, thread_id, value=None, by="id", model=None):
        super(MessageVerifications, self).__init__(thread_id=thread_id, value=value, by=by, model=model)

    def verify_message_exists(self):
        if self.check_message_exists():
            return True
        HttpException.throw_404("Message with {by} '{value}' not found".format(by=self.by, value=self.value))

    def verify_user_is_owner(self, user_id):
        self.verify_message_exists()
        if self.check_user_is_owner(user_id=user_id):
            return True
        HttpException.throw_403("You must be the message owner")
