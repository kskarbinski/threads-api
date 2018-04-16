from app_verifications import BaseChecks
from app_data.threads import threads_messages


class MessageChecks(BaseChecks):
    """
    Checks related to message.
    All checks return True or False.
    """
    def __init__(self, thread_id, value=None, by="id", model=None):
        super(MessageChecks, self).__init__(container=threads_messages[thread_id], value=value, by=by, model=model)
        self.thread_message_model = self.model
    
    def check_message_exists(self):
        return True if self.thread_message_model else False

    def check_user_is_owner(self, user_id):
        return True if self.thread_message_model.user == user_id else False
