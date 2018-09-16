from flask import request
from flask_restful import Resource, reqparse

from app_auth import auth
from app_handlers import ThreadsHandler
from app_verifications.thread import ThreadVerifications
from app_utils.validators.length import validate_length
from app_errors.http_exceptions import HttpException


class ThreadsRoute(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        if request.method == "GET":
            self.reqparse.add_argument("start", type=int, required=False, location="values")
            self.reqparse.add_argument("limit", type=int, required=False, location="values")
        elif request.method == "POST":
            self.reqparse.add_argument(name="name", type=str, required=True, location="json")
            self.reqparse.add_argument(name="private", type=bool, required=True, location="json")

        super(ThreadsRoute, self).__init__()

    def get(self):
        """
        @api {GET} /threads Get threads
        @apiDescription Get last 100 threads created
        @apiGroup Thread

        @apiSuccessExample {JSON} Success-Response:
            {
                "items": ThreadModel[]
            }
        """
        args = self.reqparse.parse_args()

        # Get paginated threads
        thread_models = ThreadsHandler().get(
            start=args.start,
            limit=args.limit
        )

        # Return paginated threads
        return thread_models.jsonify()

    def post(self):
        """
        @api {POST} /threads Create thread
        @apiGroup Thread

        @apiParam (JSON param) {String} name Name of the thread. Has to be unique, must not be a number, length 2-50
        @apiParam (JSON param) {Boolean} private Whether the thread is to be private or not

        @apiSuccessExample {JSON} Success-Response:
            {
                ThreadModel
            }
        """
        args = self.reqparse.parse_args()
        user_id = auth.user_id

        # Validate thread name
        if ThreadVerifications(by="name", value=args.name).check_thread_exists():
            HttpException.throw_409("Thread name already taken")
        elif args.name.isdigit():
            HttpException.throw_422("Thread name must not be a number")
        elif not validate_length(2, 50, args.name):
            HttpException.throw_422("Thread name length must be between 2 and 50 characters")

        # Create thread
        thread_model = ThreadsHandler().post(
            user_id=user_id,
            name=args.name,
            private=args.private
        )

        # Return thread
        return thread_model.jsonify()
