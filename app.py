from flask import Flask
from flask_restful import Api

from app_routes import RootRoute
from app_routes.user import UserRoute
from app_routes.signup import SignupRoute
from app_routes.users.user_id import UsersUserIdRoute
from app_routes.users.user_name import UsersUserNameRoute
from app_routes.users import UsersRoute
from app_routes.validate.username import ValidateUsernameRoute
from app_routes.threads import ThreadsRoute
from app_routes.threads.thread_id.invite import ThreadsThreadIdInviteRoute
from app_routes.threads.thread_id import ThreadsThreadIdRoute
from app_routes.threads.thread_id.kick import ThreadsThreadIdKickRoute
from app_routes.threads.thread_id.apply import ThreadsThreadIdApplyRoute
from app_routes.threads.thread_id.invitations import ThreadsThreadIdInvitationsRoute
from app_routes.threads.thread_id.applications import ThreadsThreadIdApplicationsRoute
from app_routes.threads.thread_id.messages import ThreadsThreadIdMessagesRoute
from app_routes.threads.thread_id.messages.message_id import ThreadsThreadIdMessageRoute
from app_routes.threads.thread_id.invitations.invitation_id import ThreadsThreadIdInvitationRoute
from app_routes.threads.thread_id.applications.application_id import ThreadsThreadIdApplicationRoute
from app_routes.threads.invitations import ThreadsInvitationsRoute
from app_routes.threads.applications import ThreadsApplicationsRoute
from app_routes.threads.invitations.invitation_id import ThreadsInvitationsInvitationIdRoute
from app_routes.threads.applications.application_id import ThreadsApplicationsApplicationIdRoute


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(RootRoute, "/", endpoint="root")
    api.add_resource(UserRoute, "/user", endpoint="user")
    # signup_handler
    api.add_resource(SignupRoute, "/signup", endpoint="signup")
    # user_handler
    api.add_resource(UsersUserIdRoute, "/users/id/<string:user_id>", endpoint="user_by_user_id")
    # user_handler
    api.add_resource(UsersUserNameRoute, "/users/username/<string:username>", endpoint="user_by_username")
    # users_handler
    api.add_resource(UsersRoute, "/users", endpoint="users")
    api.add_resource(ValidateUsernameRoute, "/validate/username", endpoint="validate_username")
    # threads_handler
    api.add_resource(ThreadsRoute, "/threads", endpoint="threads")
    # thread_invite handler
    api.add_resource(ThreadsThreadIdInviteRoute, "/threads/<string:thread_id>/invite", endpoint="thread_invite")
    # thread_handler
    api.add_resource(ThreadsThreadIdRoute, "/threads/<string:thread_id>", endpoint="thread_by_thread_id")
    # thread_kick_handler
    api.add_resource(ThreadsThreadIdKickRoute, "/threads/<string:thread_id>/kick", endpoint="thread_kick")
    # thread_apply_handler
    api.add_resource(ThreadsThreadIdApplyRoute, "/threads/<string:thread_id>/apply", endpoint="thread_apply")
    # thread_invitations_handler
    api.add_resource(
        ThreadsThreadIdInvitationsRoute, "/threads/<string:thread_id>/invitations", endpoint="thread_invitations")
    # thread_applications_handler
    api.add_resource(
        ThreadsThreadIdApplicationsRoute, "/threads/<string:thread_id>/applications", endpoint="thread_applications")
    # thread_messages_handler
    api.add_resource(ThreadsThreadIdMessagesRoute, "/threads/<string:thread_id>/messages", endpoint="thread_messages")
    # thread_message_handler
    api.add_resource(
        ThreadsThreadIdMessageRoute,
        "/threads/<string:thread_id>/messages/<string:message_id>",
        endpoint="thread_message"
    )
    # thread_invitation_handler
    api.add_resource(
        ThreadsThreadIdInvitationRoute,
        "/threads/<string:thread_id>/invitations/<string:invitation_id>",
        endpoint="thread_invitation"
    )
    # thread_application_handler
    api.add_resource(
        ThreadsThreadIdApplicationRoute,
        "/threads/<string:thread_id>/applications/<string:application_id>",
        endpoint="thread_application"
    )
    # threads_invitations_handler
    api.add_resource(ThreadsInvitationsRoute, "/threads/invitations", endpoint="threads_invitations")
    # threads_applications_handler
    api.add_resource(ThreadsApplicationsRoute, "/threads/applications", endpoint="threads_applications")
    # thread_invitation_handler
    api.add_resource(
        ThreadsInvitationsInvitationIdRoute,
        "/threads/invitations/<string:invitation_id>",
        endpoint="user_thread_invitation"
    )
    # thread_application_handler
    api.add_resource(
        ThreadsApplicationsApplicationIdRoute,
        "/threads/applications/<string:application_id>",
        endpoint="user_thread_application"
    )

    app.run()
