from flask_restful import Resource

from app_auth import auth
from app_handlers import ThreadHandler
from app_verifications.thread import ThreadVerifications


class ThreadsThreadIdRoute(Resource):
    decorators = [auth.login_required]

    def get(self, thread_id):
        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        # Verify thread exists
        thread_verifications.verify_thread_exists()

        thread_model = ThreadHandler().get(thread_id=thread_id)

        return thread_model.jsonify()

    def delete(self, thread_id):
        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        thread_model = thread_verifications.thread_model
        # Verify if user is thread owner
        thread_verifications.verify_user_is_owner(user_id=auth.user_id)

        # Delete thread
        thread_model = ThreadHandler().delete(thread_model=thread_model)

        return thread_model.jsonify()
