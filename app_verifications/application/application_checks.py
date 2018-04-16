from app_verifications import BaseChecks
from app_data.threads import threads_applications, users_thread_applications


class ApplicationChecks(BaseChecks):
    """
    Checks related to thread application.
    All checks return True or False.
    """
    def __init__(self, thread_id=None, user_id=None, value=None, by="id", model=None):
        assert thread_id or user_id, "Get application by user id or thread id"
        if thread_id is not None:
            container = threads_applications[thread_id]
        else:
            container = users_thread_applications[user_id]

        super(ApplicationChecks, self).__init__(
            container=container,
            value=value,
            by=by,
            model=model
        )
        self.thread_application_model = self.model

    def check_application_exists(self):
        return True if self.thread_application_model else False

    def check_user_is_owner(self, user_id):
        return True if self.thread_application_model.user == user_id else False
