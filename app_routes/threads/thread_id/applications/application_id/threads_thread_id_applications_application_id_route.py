from flask_restful import Resource, reqparse
from flask import request

from app_auth import auth
from app_handlers import ThreadApplicationHandler
from app_verifications.thread import ThreadVerifications
from app_verifications.application import ApplicationVerifications


class ThreadsThreadIdApplicationsApplicationIdRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        if request.method == "POST":
            self.reqparse.add_argument("accept", type=bool, required=True, location="json")

        super(ThreadsThreadIdApplicationsApplicationIdRoute, self).__init__()

    def get(self, thread_id, application_id):
        """
        @api {GET} /threads/<String:thread_id>/applications/<String:application_id> Get received thread application
        @apiGroup Thread
        @apiDescription Get received thread application by id
        """
        caller_user_id = auth.user_id

        # Verifications

        # Thread verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        # Verify user is thread owner
        thread_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Application verifications
        application_verifications = ApplicationVerifications(thread_id=thread_id, value=application_id)
        # Verify application exists
        application_verifications.verify_application_exists()

        # Get thread application
        thread_application_model = ThreadApplicationHandler().get(
            thread_id=thread_id,
            application_id=application_id
        )

        return thread_application_model.jsonify()

    def post(self, thread_id, application_id):
        """
        @api {POST} /threads/<String:thread_id>/applications/<String:application_id> Accept or reject received thread application
        @apiGroup Thread

        @apiParam (JSON param) {Boolean} accept Accept or reject the application
        """
        args = self.reqparse.parse_args()
        caller_user_id = auth.user_id

        # Verifications

        # Thread verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        # Verify user is thread owner
        thread_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Application verifications
        application_verifications = ApplicationVerifications(thread_id=thread_id, value=application_id)
        thread_application_model = application_verifications.thread_application_model
        # Verify application exists
        application_verifications.verify_application_exists()

        # Add user to thread, mark application as accepted or rejected
        ThreadApplicationHandler().post(
            thread_application_model=thread_application_model,
            accept=args.accept
        )

        return thread_application_model.jsonify()
