from flask_restful import Resource

from app_auth import auth
from app_handlers import ThreadApplicationHandler
from app_verifications.application import ApplicationVerifications


class ThreadsApplicationsApplicationIdRoute(Resource):
    decorators = [auth.login_required]

    def get(self, application_id):
        """
        @api {GET} /threads/applications/<String:application_id> Get sent thread application
        @apiDescription Get sent thread application by id
        @apiGroup Thread

        @apiSuccessExample {JSON} Success-Response:
            {
                ThreadApplicationModel
            }
        """
        caller_user_id = auth.user_id

        # Verifications

        # Application verifications
        application_verifications = ApplicationVerifications(user_id=caller_user_id, value=application_id)
        # Verify user is application owner
        application_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Get thread application
        thread_application = ThreadApplicationHandler().get(
            thread_id=application_verifications.thread_application_model.thread,
            application_id=application_id
        )

        return thread_application.jsonify()

    def delete(self, application_id):
        """
        @api {DELETE} /threads/applications/<String:application_id> Cancel sent thread application
        @apiDescription Cancel sent thread application by id
        @apiGroup Thread

        @apiSuccessExample {JSON} Success-Response:
            {
                ThreadApplicationModel
            }
        """
        caller_user_id = auth.user_id

        # Verifications

        # Application verifications
        application_verifications = ApplicationVerifications(user_id=caller_user_id, value=application_id)
        thread_application_model = application_verifications.thread_application_model
        # Verify user is application owner
        application_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Update application and mark as accepted or rejected
        ThreadApplicationHandler().delete(
            thread_application_model=thread_application_model,
        )

        return thread_application_model.jsonify()
