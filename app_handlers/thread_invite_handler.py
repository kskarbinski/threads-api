from app_data.threads import users_thread_invitations, threads_invitations
from app_models import ThreadInvitationModel
from app_containers import ModelsList
from app_verifications.thread import ThreadVerifications


class ThreadInviteHandler(object):
    def post(self, owner_user_id, user_ids, thread_model):
        # Exclude users who are already invited or members
        thread_verifications = ThreadVerifications(model=thread_model)
        user_ids = [user_id for user_id in user_ids if
                    not thread_verifications.check_user_is_invited(user_id)
                    and
                    not thread_verifications.check_user_is_member(user_id)]

        # Create ThreadInvitationModel objects
        thread_invitation_models = [
            ThreadInvitationModel(
                user=user_id,
                thread_id=thread_model.id,
                invited_by=owner_user_id,
                users_in_thread=thread_model.users
            ) for user_id in user_ids
        ]

        # Register invitations
        for thread_invitation_model in thread_invitation_models:
            # Register invitation for thread
            threads_invitations[thread_model.id].insert(0, thread_invitation_model)
            # Register invitation for user
            users_thread_invitations[thread_invitation_model.user].insert(0, thread_invitation_model)

        return ModelsList(list_of_models=thread_invitation_models)
