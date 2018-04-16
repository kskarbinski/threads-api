from flask_httpauth import HTTPBasicAuth

from app_data.users import users_credentials
from app_utils.helpers.finders import FindModel
from app_data.users import users


class Auth(HTTPBasicAuth):
    @property
    def user_model(self):
        username = self.username()
        user_model = FindModel(users).by_username(username)
        return user_model

    @property
    def user_id(self):
        return self.user_model.id

    @property
    def firstname(self):
        return self.user_model.firstname

    @property
    def lastname(self):
        return self.user_model.lastname


auth = Auth()


@auth.get_password
def get_pw(username):
    for user in users_credentials:
        if user.username == username:
            return user.password
