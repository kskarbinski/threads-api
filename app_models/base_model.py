from time import time
from flask import jsonify
from uuid import uuid4


class BaseModel(object):
    def __init__(self):
        current_time_in_seconds = int(time())
        self.created_at = current_time_in_seconds
        self.updated_at = current_time_in_seconds
        self.id = str(uuid4())

    def to_dict(self, camel_case=False):
        return self._to_dict(self, camel_case=camel_case)

    def jsonify(self):
        return jsonify(self.to_dict(camel_case=True))

    def update(self, key, value, action="replace"):
        """
        Update model's attribute.
        Action argument defines how to update (i.e. replace attribute with value, append value to attribute)

        :param str key: Key to update
        :param value: The new value
        :param action: How to update (replace, append)

        :return: None
        """
        actions = ["replace", "append"]
        if action not in actions:
            raise ValueError("action can only be one of {actions}".format(actions=actions))

        if action == "replace":
            self._update_replace(key=key, new_value=value)
        elif action == "append":
            self._update_append(key=key, value=value)

        setattr(self, "updated_at", time())

    def _verify_attribute_exists(self, key):
        if getattr(self, key, AttributeError) is AttributeError:
            raise AttributeError("Attribute {key} does not exist".format(key=key))

    def _update_replace(self, key, new_value):
        self._verify_attribute_exists(key=key)
        setattr(self, key, new_value)

    def _update_append(self, key, value):
        self._verify_attribute_exists(key=key)
        getattr(self, key).append(value)

    def _to_dict(self, obj, camel_case=False):
        if hasattr(obj, "__dict__"):
            final_list = []
            for key, value in vars(obj).iteritems():
                if not callable(value):
                    if camel_case:
                        final_list.append((self._snake_case_to_camel_case(key), self._to_dict(value)))
                    else:
                        final_list.append((key, self._to_dict(value)))
            return dict(final_list)
        else:
            return obj

    @staticmethod
    def _snake_case_to_camel_case(string):
        words = string.split("_")
        return words[0] + "".join([word.title() for word in words[1:]])
