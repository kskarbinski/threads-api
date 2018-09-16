from enum import IntEnum


class ApplicationStatusType(IntEnum):
    """
    @api ApplicationStatusType ApplicationStatusType
    @apiGroup |Types
    @apiSuccessExample ENUM
    1: PENDING
    2: ACCEPTED
    3: REJECTED
    4: CANCELLED
    """
    PENDING = 1
    ACCEPTED = 2
    REJECTED = 3
    CANCELLED = 4
