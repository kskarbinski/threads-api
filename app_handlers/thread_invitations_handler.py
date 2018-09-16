from app_data.threads import threads_invitations
from app_utils.helpers.pagination import Paginate


class ThreadInvitationsHandler(object):
    def get(self, thread_id, start, limit):
        paginated_thread_invitation_models = Paginate(
            start=start,
            limit=limit,
            resource=threads_invitations[thread_id],
        )

        return paginated_thread_invitation_models
