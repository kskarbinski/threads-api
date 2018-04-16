from .text_checks import TextChecks
from app_errors.http_exceptions import HttpException


class TextVerifications(TextChecks):
    """
    Every method verifies something related to text. If verification does not pass a HttpException is thrown.
    """
    def verify_text_length(self, min_l, max_l):
        if self.check_text_length(min_l=min_l, max_l=max_l):
            return True
        HttpException.throw_422(
            "Text has to be between {min_l} and {max_l} characters".format(min_l=min_l, max_l=max_l)
        )
