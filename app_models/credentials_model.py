from .base_model import BaseModel


class CredentialsModel(BaseModel):
    def __init__(self, username, password):
        super(CredentialsModel, self).__init__(model_type="CredentialsModel")
        self.username = unicode(username)
        self.password = unicode(password)
