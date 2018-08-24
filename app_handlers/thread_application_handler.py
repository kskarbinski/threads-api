from time import time

from app_data.threads import threads_applications, users_threads, threads
from app_utils.helpers.finders import FindModel
from app_types.application.status import ApplicationStatusType


class ThreadApplicationHandler(object):
    def get(self, thread_id, application_id):
        # Get thread application
        thread_application_model = FindModel(models_list=threads_applications[thread_id]).by_id(application_id)

        return thread_application_model

    def post(self, thread_application_model, accept):
        # Update thread application and mark as accepted or rejected
        status = ApplicationStatusType.ACCEPTED if accept else ApplicationStatusType.REJECTED
        thread_application_model.status = status.value
        thread_application_model.updated_at = int(time())

        thread_model = FindModel(models_list=threads).by_id(thread_application_model.thread)
        # Add user to thread
        thread_model.users.insert(0, thread_application_model.user)
        # Update thread
        thread_model.updated_at = int(time())
        # Add thread to users threads
        users_threads[thread_application_model.user].insert(0, thread_model)

        return thread_application_model

    def delete(self, thread_application_model):
        # Update thread application and mark as deleted
        thread_application_model.status = ApplicationStatusType.CANCELLED.value
        thread_application_model.updated_at = int(time())
