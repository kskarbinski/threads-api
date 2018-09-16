from .base_model import BaseModel


class UsernameValidationModel(BaseModel):
    def __init__(self):
        """
        @api UsernameValidationModel UsernameValidationModel
        @apiGroup |Models
        @apiSuccessExample JSON
        {
            "createdAt": Number,
            "updatedAt": Number,
            "id": String,
            "modelType": "UsernameValidationModel",
            "errors": String[]
        }
        """
        super(UsernameValidationModel, self).__init__(model_type="UsernameValidationModel")
        self.errors = []
