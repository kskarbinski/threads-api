from .base_model import BaseModel


class ThreadMessageModel(BaseModel):
    def __init__(self, user_id, thread_id, message):
        """
        @api ThreadMessageModel ThreadMessageModel
        @apiGroup |Models
        @apiSuccessExample JSON
        {
            "createdAt": Number,
            "updatedAt": Number,
            "id": String,
            "modelType": "ThreadMessageModel",
            "user": UserId,
            "thread": ThreadId,
            "message": String,
            "deleted": Bool
        }
        """
        super(ThreadMessageModel, self).__init__(model_type="ThreadMessageModel")
        self.user = user_id
        self.thread = thread_id
        self.message = message
        self.deleted = False
