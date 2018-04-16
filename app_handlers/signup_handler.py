from app_models import UserModel, CredentialsModel
from app_data.users import users, users_credentials
from app_data.threads import users_thread_applications, users_thread_invitations, users_threads


class SignupHandler(object):
    def post(self, username, password, firstname, lastname):
        # Creat UserModel and CredentialsModel
        user_model = UserModel(
            username=username,
            firstname=firstname,
            lastname=lastname,
        )
        credentials_model = CredentialsModel(
            username=username,
            password=password
        )

        # Register user
        users.append(user_model)
        users_credentials.append(credentials_model)
        # Register user's threads
        users_threads[user_model.id] = list()
        # Register user's thread applications
        users_thread_applications[user_model.id] = list()
        # Register user's thread invitations
        users_thread_invitations[user_model.id] = list()

        return user_model
