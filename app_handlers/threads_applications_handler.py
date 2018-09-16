from app_data.threads import users_thread_applications
from app_utils.helpers.pagination import Paginate


class ThreadsApplicationsHandler(object):
    def get(self, user_id, start, limit):
        paginated_thread_application_models = Paginate(
            start=start,
            limit=limit,
            resource=users_thread_applications[user_id],
        )

        return paginated_thread_application_models
