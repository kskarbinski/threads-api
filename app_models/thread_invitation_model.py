from .base_model import BaseModel
from app_types.invitation.status import InvitationStatusType


class ThreadInvitationModel(BaseModel):
    def __init__(self, user, thread_id, invited_by, users_in_thread, invitation_status=InvitationStatusType.PENDING):
        """
        @api ThreadInvitationModel ThreadInvitationModel
        @apiGroup |Models
        @apiSuccessExample JSON
        {
            "createdAt": Number,
            "updatedAt": Number,
            "id": String,
            "modelType": "ThreadInvitationModel",
            "user": UserId,
            "thread": ThreadId,
            "status": InvitationStatusType,
            "invitedBy": UserId,
            "usersInThread": UserId[],
            "deleted": Bool
        }
        """
        super(ThreadInvitationModel, self).__init__(model_type="ThreadInvitationModel")
        self.user = user
        self.thread = thread_id
        self.status = invitation_status.value
        self.invited_by = invited_by
        self.users_in_thread = users_in_thread
        self.deleted = False
