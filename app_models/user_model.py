from .base_model import BaseModel


class UserModel(BaseModel):
    def __init__(self, username, firstname, lastname):
        """
        @api UserModel UserModel
        @apiGroup |Models
        @apiSuccessExample JSON
        {
            "createdAt": Number,
            "updatedAt": Number,
            "id": String,
            "modelType": "UserModel",
            "username": String,
            "firstname": String,
            "lastname": String
        }
        """
        super(UserModel, self).__init__(model_type="UserModel")
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
