from flask_restful import Resource, reqparse

from app_auth import auth

from app_verifications.user import UserVerifications
from app_verifications.thread import ThreadVerifications

from app_handlers import ThreadInviteHandler


class ThreadsThreadIdInviteRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(name="users", type=str, action="append", required=True, location="json")
        super(ThreadsThreadIdInviteRoute, self).__init__()

    def post(self, thread_id):
        args = self.reqparse.parse_args()
        caller_user_id = auth.user_id

        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        thread_model = thread_verifications.thread_model
        # Verify user is owner of thread
        thread_verifications.verify_user_is_owner(user_id=caller_user_id)
        # Verify that owner is not inviting himself
        thread_verifications.verify_excludes_owner(user_ids=args.users)
        # Verify users to be invited exist and are not already invited
        for user_id in args.users:
            UserVerifications(value=user_id).verify_user_exists()
            thread_verifications.verify_user_not_invited(user_id=user_id)

        # Create and register invitations
        models_list = ThreadInviteHandler().post(
            owner_user_id=caller_user_id,
            user_ids=args.users,
            thread_model=thread_model
        )

        return models_list.jsonify()
