from app_data.threads import threads_applications
from app_utils.helpers.pagination import Paginate


class ThreadApplicationsHandler(object):
    def get(self, thread_id, start, limit):
        paginated_thread_application_models = Paginate(
            start=start,
            limit=limit,
            resource=threads_applications[thread_id]
        )

        return paginated_thread_application_models
