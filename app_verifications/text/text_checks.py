from app_verifications import BaseChecks
from app_data.threads import threads, threads_invitations, threads_applications
from app_utils.helpers.finders import FindModel


class TextChecks(object):
    """
    Checks related to text.
    All checks return True or False.
    """
    def __init__(self, text):
        self.text = text
    
    def check_text_length(self, min_l, max_l):
        return min_l <= len(self.text) <= max_l
