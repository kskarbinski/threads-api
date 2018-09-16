from flask_restful import Resource

from app_auth import auth

from app_verifications.thread import ThreadVerifications

from app_handlers import ThreadApplyHandler


class ThreadsThreadIdApplyRoute(Resource):
    decorators = [auth.login_required]

    def post(self, thread_id):
        """
        @api {POST} /threads/<String:thread_id>/apply Apply to thread
        @apiGroup Thread

        @apiSuccessExample {JSON} Success-Response:
            {
                ThreadApplicationModel
            }
        """
        caller_user_id = auth.user_id

        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        thread_model = thread_verifications.thread_model
        # Verify if thread exists
        thread_verifications.verify_thread_exists()
        # Verify it is not thread owner applying
        thread_verifications.verify_user_is_not_owner(user_id=caller_user_id)
        # Verify thread is not private
        thread_verifications.verify_thread_is_not_private()
        # Verify user did not already apply
        thread_verifications.verify_user_not_applied(user_id=caller_user_id)

        # Create and register application
        thread_application_model = ThreadApplyHandler().post(
            user_id=caller_user_id,
            thread_model=thread_model
        )

        return thread_application_model.jsonify()
