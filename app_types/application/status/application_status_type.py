from enum import IntEnum


class ApplicationStatusType(IntEnum):
    PENDING = 1
    ACCEPTED = 2
    REJECTED = 3
    CANCELLED = 4
