from app_verifications import BaseChecks
from app_data.threads import threads, threads_invitations, threads_applications
from app_utils.helpers.finders import FindModel


class ThreadChecks(BaseChecks):
    """
    Checks related to thread/threads.
    All checks return True or False.
    """
    def __init__(self, value=None, by="id", model=None):
        super(ThreadChecks, self).__init__(container=threads, value=value, by=by, model=model)
        self.thread_model = self.model
    
    def check_thread_exists(self):
        return True if self.thread_model else False

    def check_user_is_owner(self, user_id):
        return True if self.thread_model.owner == user_id else False

    def check_user_is_not_owner(self, user_id):
        return not self.check_user_is_owner(user_id=user_id)

    def check_excludes_owner(self, user_ids):
        return True if self.thread_model.owner not in user_ids else False

    def check_user_is_invited(self, user_id):
        thread_invitations = threads_invitations[self.thread_model.id]
        return True if FindModel(models_list=thread_invitations).by_user(user_id) else False

    def check_user_is_member(self, user_id):
        return True if user_id in self.thread_model.users else False

    def check_thread_is_private(self):
        return True if self.thread_model.private else False

    def check_thread_is_not_private(self):
        return not self.check_thread_is_private()

    def check_user_applied(self, user_id):
        return True if FindModel(models_list=threads_applications[self.thread_model.id]).by_user(user_id) else False

    def check_user_not_applied(self, user_id):
        return not self.check_user_applied(user_id=user_id)

    def check_user_invited(self, user_id):
        return True if FindModel(models_list=threads_invitations[self.thread_model.id]).by_user(user_id) else False

    def check_user_not_invited(self, user_id):
        return not self.check_user_invited(user_id=user_id)
