from app_data.threads import threads, threads_applications, threads_invitations
from app_utils.helpers.finders import FindModel

from app_types.invitation.status import InvitationStatusType
from app_types.application.status import ApplicationStatusType


class ThreadHandler(object):
    def get(self, thread_id):
        return FindModel(models_list=threads).by_id(thread_id)

    def delete(self, thread_model):
        # Mark thread as deleted
        thread_model.deleted = True

        # Cancel all invites sent out and decline all applications to this thread
        for thread_invitation_model in threads_invitations[thread_model.id]:
            thread_invitation_model.status = InvitationStatusType.CANCELLED
        for thread_application_model in threads_applications[thread_model.id]:
            thread_application_model.status = ApplicationStatusType.REJECTED

        # Return thread
        return thread_model
