from .base_model import BaseModel


class ThreadModel(BaseModel):
    def __init__(self, name, owner, users, private):
        super(ThreadModel, self).__init__(model_type="ThreadModel")
        self.name = name
        self.owner = owner
        self.users = users
        self.private = private
        self.deleted = False
