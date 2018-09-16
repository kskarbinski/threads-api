from app_data.threads import threads, users_threads, threads_invitations, threads_applications, threads_messages
from app_models import ThreadModel
from app_utils.helpers.pagination import Paginate


class ThreadsHandler(object):
    def get(self, start, limit, with_private=False, with_deleted=False):
        # Filter private and deleted threads
        thread_models = []
        for thread_model in threads:
            if not with_private:
                if thread_model.private:
                    continue
            if not with_deleted:
                if thread_model.deleted:
                    continue
            thread_models.append(thread_model)

        # Return paginated threads
        return Paginate(
            start=start,
            limit=limit,
            resource=thread_models
        )

    def post(self, user_id, name, private):
        # Create ThreadModel
        thread_model = ThreadModel(
            name=name,
            owner=user_id,
            users=[user_id],
            private=private,
        )

        # Register thread
        threads.insert(0, thread_model)
        # Register thread invitations
        threads_invitations[thread_model.id] = list()
        # Register thread applications
        threads_applications[thread_model.id] = list()
        # Register thread messages
        threads_messages[thread_model.id] = list()
        # Register thread for user
        users_threads[user_id].insert(0, thread_model)

        # Return thread
        return thread_model
