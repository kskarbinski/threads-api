from .base_model import BaseModel


class ThreadMessageModel(BaseModel):
    def __init__(self, user_id, thread_id, message):
        super(ThreadMessageModel, self).__init__()
        self.user = user_id
        self.thread = thread_id
        self.message = message
        self.deleted = False
