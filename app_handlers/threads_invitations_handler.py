from app_data.threads import users_thread_invitations
from app_utils.helpers.pagination import Paginate


class ThreadsInvitationsHandler(object):
    def get(self, user_id, start, limit):
        paginated_thread_invitation_models = Paginate(
            start=start,
            limit=limit,
            resource=users_thread_invitations[user_id],
            resource_name="invitations"
        )

        return paginated_thread_invitation_models
