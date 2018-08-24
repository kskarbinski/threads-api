from .thread_checks import ThreadChecks
from app_errors.http_exceptions import HttpException


class ThreadVerifications(ThreadChecks):
    """
    Every method verifies something related to thread. If verification does not pass a HttpException is thrown.
    """
    def __init__(self, value=None, by="id", model=None):
        super(ThreadVerifications, self).__init__(value=value, by=by, model=model)

    def verify_thread_exists(self):
        if self.check_thread_exists():
            return True
        HttpException.throw_404("Thread with {by} '{value}' not found".format(by=self.by, value=self.value))

    def verify_user_is_owner(self, user_id):
        self.verify_thread_exists()
        if self.check_user_is_owner(user_id=user_id):
            return True
        HttpException.throw_403("You must be the thread owner")

    def verify_user_is_not_owner(self, user_id):
        self.verify_thread_exists()
        if self.check_user_is_not_owner(user_id=user_id):
            return True
        HttpException.throw_422("You must not be the thread owner")

    def verify_excludes_owner(self, user_ids):
        self.verify_thread_exists()
        if self.check_excludes_owner(user_ids=user_ids):
            return True
        HttpException.throw_422("You may not perform this action on thread owner")

    def verify_user_is_member(self, user_id):
        self.verify_thread_exists()
        if self.check_user_is_member(user_id=user_id):
            return True
        HttpException.throw_403("User with id '{user_id}' is not a member of the thread".format(user_id=user_id))

    def verify_thread_is_not_private(self):
        self.verify_thread_exists()
        if self.check_thread_is_not_private():
            return True
        HttpException.throw_403("The thread is private")

    def verify_user_not_applied(self, user_id):
        self.verify_thread_exists()
        if self.check_user_not_applied(user_id=user_id):
            return True
        HttpException.throw_409("You have already applied to this thread")

    def verify_user_not_invited(self, user_id):
        self.verify_thread_exists()
        if self.check_user_not_invited(user_id=user_id):
            return True
        HttpException.throw_409("User with id '{user_id}' already invited".format(user_id=user_id))
