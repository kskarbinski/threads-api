from flask_restful import Resource, reqparse

from app_auth import auth

from app_verifications.thread import ThreadVerifications

from app_handlers import ThreadKickHandler


class ThreadsThreadIdKickRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(name="users", type=str, action="append", required=True, location="json")
        super(ThreadsThreadIdKickRoute, self).__init__()

    def post(self, thread_id):
        args = self.reqparse.parse_args()
        caller_user_id = auth.user_id

        # Verifications
        thread_verifications = ThreadVerifications(value=thread_id)
        thread_model = thread_verifications.thread_model
        # Verify if user is owner of thread
        thread_verifications.verify_user_is_owner(user_id=caller_user_id)
        # Verify user is not trying to kick himself
        thread_verifications.verify_excludes_owner(user_ids=args.users)
        # Verify users to be kicked are members of the thread
        for user_id in args.users:
            thread_verifications.verify_user_is_member(user_id=user_id)

        # Kick users from thread
        thread_model = ThreadKickHandler().post(
            thread_model=thread_model,
            user_ids=args.users
        )

        return thread_model.jsonify()
