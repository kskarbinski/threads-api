from .base_model import BaseModel


class UserModel(BaseModel):
    def __init__(self, username, firstname, lastname):
        super(UserModel, self).__init__()
        self.username = username
        self.firstname = firstname
        self.lastname = lastname