from .base_model import BaseModel


class UsernameValidationModel(BaseModel):
    def __init__(self):
        super(UsernameValidationModel, self).__init__(model_type="UsernameValidationModel")
        self.errors = []
