from time import time

from app_data.threads import threads_messages
from app_utils.helpers.finders import FindModel


class ThreadMessageHandler(object):
    def get(self, thread_id, message_id):
        # Find and return message
        return FindModel(models_list=threads_messages[thread_id]).by_id(message_id)

    def post(self, thread_message_model, message):
        # Update message
        thread_message_model.message = message
        thread_message_model.updated_at = int(time())

        # Return message
        return thread_message_model

    def delete(self, thread_message_model):
        # Mark message as deleted
        thread_message_model.deleted = True
        thread_message_model.updated_at = int(time())

        # Return message
        return thread_message_model
