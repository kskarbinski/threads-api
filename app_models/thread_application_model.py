from .base_model import BaseModel
from app_types.application.status import ApplicationStatusType


class ThreadApplicationModel(BaseModel):
    def __init__(self, user, thread_id, application_status=ApplicationStatusType.PENDING):
        """
        @api ThreadApplicationModel ThreadApplicationModel
        @apiGroup |Models
        @apiSuccessExample JSON
        {
            "createdAt": Number,
            "updatedAt": Number,
            "id": String,
            "modelType": "ThreadApplicationModel",
            "user": UserId,
            "thread": ThreadId,
            "status": ApplicationStatusType,
            "deleted": Bool
        }
        """
        super(ThreadApplicationModel, self).__init__(model_type="ThreadApplicationModel")
        self.user = user
        self.thread = thread_id
        self.status = application_status.value
        self.deleted = False
