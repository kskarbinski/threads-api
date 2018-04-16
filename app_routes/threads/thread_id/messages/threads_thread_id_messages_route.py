from flask import request
from flask_restful import Resource, reqparse

from app_auth import auth
from app_handlers import ThreadMessagesHandler
from app_verifications.thread import ThreadVerifications
from app_verifications.text import TextVerifications


class ThreadsThreadIdMessagesRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        if request.method == "GET":
            self.reqparse.add_argument("start", type=int, required=False, location="values")
            self.reqparse.add_argument("limit", type=int, required=False, location="values")
        elif request.method == "POST":
            self.reqparse.add_argument("message", type=str, required=True, location="json")

        super(ThreadsThreadIdMessagesRoute, self).__init__()

    def get(self, thread_id):
        args = self.reqparse.parse_args()
        caller_user_id = auth.user_id

        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        # Verify thread exists
        thread_verifications.verify_thread_exists()
        # Verify user is thread member
        thread_verifications.verify_user_is_member(user_id=caller_user_id)

        # Get thread messages
        thread_message_models = ThreadMessagesHandler().get(
            thread_id=thread_id,
            start=args.start,
            limit=args.limit
        )

        return thread_message_models.jsonify()

    def post(self, thread_id):
        args = self.reqparse.parse_args()
        caller_user_id = auth.user_id

        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        thread_model = thread_verifications.thread_model
        # Verify thread exists
        thread_verifications.verify_thread_exists()
        # Verify user is thread member
        thread_verifications.verify_user_is_member(user_id=caller_user_id)
        # Verify message length
        TextVerifications(text=args.message).verify_text_length(min_l=1, max_l=300)

        # Create thread message
        thread_message_model = ThreadMessagesHandler().post(
            thread_model=thread_model,
            user_id=caller_user_id,
            message=args.message
        )

        return thread_message_model.jsonify()
