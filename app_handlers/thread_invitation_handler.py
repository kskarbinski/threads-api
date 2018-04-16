from time import time

from app_data.threads import threads_invitations, users_threads, threads
from app_utils.helpers.finders import FindModel
from app_types.invitation.status import InvitationStatusType


class ThreadInvitationHandler(object):
    def get(self, thread_id, invitation_id):
        # Get thread invitation
        thread_invitation_model = FindModel(models_list=threads_invitations[thread_id]).by_id(invitation_id)

        return thread_invitation_model

    def post(self, thread_invitation_model, accept):
        # Update thread invitation and mark as accepted or rejected
        status = InvitationStatusType.ACCEPTED if accept else InvitationStatusType.REJECTED
        thread_invitation_model.status = status.value
        thread_invitation_model.updated_at = int(time())

        thread_model = FindModel(models_list=threads).by_id(thread_invitation_model.thread)
        # Add user to thread
        thread_model.users.append(thread_invitation_model.user)
        # Update thread
        thread_model.updated_at = int(time())
        # Add thread to users threads
        users_threads[thread_invitation_model.user].append(thread_model)

        return thread_invitation_model

    def delete(self, thread_invitation_model):
        # Update thread invitation and mark as deleted
        thread_invitation_model.status = InvitationStatusType.CANCELLED.value
        thread_invitation_model.updated_at = int(time())

        return thread_invitation_model
