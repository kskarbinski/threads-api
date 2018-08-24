from app_data.threads import threads_messages
from app_models import ThreadMessageModel
from app_utils.helpers.pagination import Paginate


class ThreadMessagesHandler(object):
    def get(self, thread_id, start, limit):
        # Get paginated messages for thread
        return Paginate(
            start=start,
            limit=limit,
            resource=threads_messages[thread_id],
            resource_name="messages"
        )

    def post(self, thread_model, user_id, message):
        # Create message
        thread_message_model = ThreadMessageModel(
            user_id=user_id,
            thread_id=thread_model.id,
            message=message
        )

        # Register message
        threads_messages[thread_model.id].insert(0, thread_message_model)

        return thread_message_model
