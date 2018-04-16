from time import time

from app_data.threads import users_threads


class ThreadKickHandler(object):
    def post(self, thread_model, user_ids):
        for user_id in user_ids:
            # Remove user from thread
            thread_model.users.remove(user_id)
            users_threads[user_id].remove(thread_model)

        # Update thread
        thread_model.updated_at = int(time())

        # Return thread
        return thread_model
