from .find_models import FindModels


class FindModel(FindModels):
    def _find_model_in_models_list_by_attr(self, attr_name, attr_value):
        models = self._find_models_in_models_list_by_attr(attr_name=attr_name, attr_value=attr_value)
        if models:
            return models[0]
        return None

    def by_id(self, id_):
        return self._find_model_in_models_list_by_attr(attr_name="id", attr_value=id_)

    def by_name(self, name):
        return self._find_model_in_models_list_by_attr(attr_name="name", attr_value=name)

    def by_username(self, username):
        return self._find_model_in_models_list_by_attr(attr_name="username", attr_value=username)

    def by_user(self, user):
        return self._find_model_in_models_list_by_attr(attr_name="user", attr_value=user)
