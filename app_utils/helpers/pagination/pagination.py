from flask import abort, jsonify

from app_containers import ModelsList


class Paginate(object):
    def __init__(self, start, limit, resource, resource_name="items"):
        assert isinstance(resource, list) or isinstance(resource, tuple)

        self.start = start
        self.limit = limit
        self.resource = resource
        self.resource_name = resource_name

    def paginate(self):
        start = self.start or 1
        limit = self.limit or 100

        len_resource = len(self.resource)
        if not len_resource:
            return list()
        elif len_resource < start:
            abort(404, "Items starting with index '{start}' not found".format(start=start))

        # Start building response dict
        response = dict()
        response["start"] = start
        response["limit"] = limit
        response["{resource_name}Found".format(resource_name=self.resource_name)] = len_resource

        # Build previous
        if start < 2:
            response["previous"] = ""
        else:
            previous_start = max(1, start - limit)
            previous_limit = start - 1
            response["previous"] = "?start={previous_start}&limit={previous_limit}".format(
                previous_start=previous_start,
                previous_limit=previous_limit
            )

        # Build next
        if start + limit > len_resource:
            response["next"] = ""
        else:
            next_start = start + limit
            response["next"] = "?start={next_start}&limit={limit}".format(
                next_start=next_start,
                limit=limit
            )

        # Get results
        models = self.resource[(start - 1):(start - 1 + limit)]
        response[self.resource_name] = ModelsList(list_of_models=models).to_dict(camel_case=True)

        return response

    def jsonify(self):
        return jsonify(self.paginate())
