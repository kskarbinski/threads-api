from flask import jsonify


class ModelsList(object):
    def __init__(self, list_of_models):
        self.list_of_models = list_of_models

    def to_dict(self, camel_case=False):
        return [model.to_dict(camel_case=camel_case) for model in self.list_of_models]

    def jsonify(self):
        return jsonify(
            self.to_dict(camel_case=True)
        )
