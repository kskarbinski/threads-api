class FindModels(object):
    def __init__(self, models_list):
        self.models_list = models_list

    def _find_models_in_models_list_by_attr(self, attr_name, attr_value):
        return [m for m in self.models_list if getattr(m, attr_name) == attr_value]

    def by_id(self, id_):
        models = self._find_models_in_models_list_by_attr(attr_name="id", attr_value=id_)
        if len(models) > 1:
            print "Found two models with the same id!"
            for model in models:
                print "\n" + model.to_dict()
            raise AssertionError
        return models

    def by_name(self, name):
        return self._find_models_in_models_list_by_attr(attr_name="name", attr_value=name)

    def by_username(self, username):
        return self._find_models_in_models_list_by_attr(attr_name="username", attr_value=username)
