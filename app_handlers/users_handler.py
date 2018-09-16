from app_data.users import users
from app_utils.helpers.pagination import Paginate


class UsersHandler(object):
    def get(self, start, limit):
        return Paginate(
            start=start,
            limit=limit,
            resource=users
        )
