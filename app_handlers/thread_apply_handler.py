from app_data.threads import threads_invitations, users_thread_applications, threads_applications
from app_models import ThreadApplicationModel


class ThreadApplyHandler(object):
    def post(self, user_id, thread_model):
        # Create thread application
        thread_application_model = ThreadApplicationModel(
            user=user_id,
            thread_id=thread_model.id
        )

        # Register application

        # Register application for thread
        threads_applications[thread_model.id].append(thread_application_model)
        # Register application for user
        users_thread_applications[user_id].append(thread_application_model)

        # If user is already invited simply accept the invitation
        if user_id in threads_invitations[thread_model.id]:
            pass
            # TODO when accept handler is done

        return thread_application_model
