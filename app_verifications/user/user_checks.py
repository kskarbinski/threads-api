from app_verifications import BaseChecks
from app_data.users import users


class UserChecks(BaseChecks):
    """
    Checks related to user/users.
    All checks return True or False.
    """
    def __init__(self, value=None, by="id", model=None):
        super(UserChecks, self).__init__(container=users, value=value, by=by, model=model)
        self.user_model = self.model

    def check_user_exists(self):
        return True if self.user_model else False
