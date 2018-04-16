from app_utils.helpers.finders import FindModel


class BaseChecks(object):
    def __init__(self, container, value=None, by="id", model=None):
        assert value or model

        self.value = value
        self.by = by
        if model:
            self.model = model if model in container else None
        else:
            self.model = FindModel(container)._find_model_in_models_list_by_attr(attr_name=by, attr_value=value)
