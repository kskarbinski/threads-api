from .base_model import BaseModel


class ThreadModel(BaseModel):
    def __init__(self, name, owner, users, private):
        """
        @api ThreadModel ThreadModel
        @apiGroup |Models
        @apiSuccessExample JSON
        {
            "createdAt": Number,
            "updatedAt": Number,
            "id": String,
            "modelType": "ThreadModel",
            "name": String,
            "owner": UserId,
            "users": UserId[],
            "private": Bool,
            "deleted": Bool
        }
        """
        super(ThreadModel, self).__init__(model_type="ThreadModel")
        self.name = name
        self.owner = owner
        self.users = users
        self.private = private
        self.deleted = False
