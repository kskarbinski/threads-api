from flask import abort


class HttpException(object):
    @staticmethod
    def throw_403(msg):
        if msg is None:
            msg = "Access denied"
        abort(403, msg)

    @staticmethod
    def throw_404(msg):
        if msg is None:
            msg = "Resource does not exist"
        abort(404, msg)

    @staticmethod
    def throw_409(msg):
        if msg is None:
            msg = "Resource conflict occurred"
        abort(409, msg)

    @staticmethod
    def throw_422(msg):
        if msg is None:
            msg = "Server understands but refuses to fulfill request"
        abort(422, msg)
