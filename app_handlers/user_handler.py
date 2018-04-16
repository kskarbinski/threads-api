from app_data.users import users
from app_utils.helpers.finders import FindModel


class UserHandler(object):
    def get(self, value, by="id"):
        if by == "id":
            return FindModel(models_list=users).by_id(id_=value)
        elif by == "username":
            return FindModel(models_list=users).by_username(username=value)
        else:
            raise ValueError("Get user by id or username")
