from flask import request
from flask_restful import Resource, reqparse

from app_auth import auth
from app_handlers import ThreadMessageHandler
from app_verifications.thread import ThreadVerifications
from app_verifications.text import TextVerifications
from app_verifications.message import MessageVerifications


class ThreadsThreadIdMessagesMessageIdRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        if request.method == "POST":
            self.reqparse.add_argument("message", type=str, required=True, location="json")

        super(ThreadsThreadIdMessagesMessageIdRoute, self).__init__()

    def get(self, thread_id, message_id):
        """
        @api {GET} /threads/<String:thread_id>/messages/<String:message_id> Get thread message
        @apiGroup Thread
        @apiDescription Get thread message as member of thread
        """
        caller_user_id = auth.user_id

        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        # Verify user is thread member
        thread_verifications.verify_user_is_member(user_id=caller_user_id)
        # Verify message exists
        MessageVerifications(thread_id=thread_id, value=message_id).verify_message_exists()

        # Get thread message
        thread_message_model = ThreadMessageHandler().get(
            thread_id=thread_id,
            message_id=message_id
        )

        return thread_message_model.jsonify()

    def post(self, thread_id, message_id):
        """
        @api {POST} /threads/<String:thread_id>/messages/<String:message_id> Edit thread message
        @apiGroup Thread
        @apiDescription Edit thread message as message owner

        @apiParam (JSON param) {String} message New message. Length 1-300
        """
        args = self.reqparse.parse_args()
        caller_user_id = auth.user_id

        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        message_verifications = MessageVerifications(thread_id=thread_id, value=message_id)
        thread_message_model = message_verifications.thread_message_model
        # Verify user is thread member
        thread_verifications.verify_user_is_member(user_id=caller_user_id)
        # Verify user is message owner
        message_verifications.verify_user_is_owner(user_id=caller_user_id)
        # Verify new message length
        TextVerifications(text=args.message).verify_text_length(min_l=1, max_l=300)

        # Update thread message
        thread_message_model = ThreadMessageHandler().post(
            thread_message_model=thread_message_model,
            message=args.message
        )

        return thread_message_model.jsonify()

    def delete(self, thread_id, message_id):
        """
        @api {DELETE} /threads/<String:thread_id>/messages/<String:message_id> Remove thread message
        @apiGroup Thread
        @apiDescription Remove thread message as message owner
        """
        caller_user_id = auth.user_id

        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        message_verifications = MessageVerifications(thread_id=thread_id, value=message_id)
        thread_message_model = message_verifications.thread_message_model
        # Verify user is thread member
        thread_verifications.verify_user_is_member(user_id=caller_user_id)
        # Verify user is message owner
        message_verifications.verify_user_is_owner(user_id=caller_user_id)

        # Mark message as deleted
        thread_message_model = ThreadMessageHandler().delete(
            thread_message_model=thread_message_model
        )

        return thread_message_model.jsonify()
