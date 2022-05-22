from types import EllipsisType
from typing import List


class ErrorInfo():
    def __str__(self,):
        ...

    def __repr__(self,) -> str:
        ...

    def __init__(self, stuff):
        ...


class Error(Exception):

    info: List[ErrorInfo] | EllipsisType = ...

    def __init__(self, message, *messages, **options):
        self.info = ErrorInfo(message, *messages, **options)
