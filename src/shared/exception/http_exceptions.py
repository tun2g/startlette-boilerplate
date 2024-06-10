from starlette.exceptions import HTTPException
from .common import ErrorDetails
from typing import List
from starlette.status import (
  HTTP_403_FORBIDDEN, 
  HTTP_400_BAD_REQUEST, 
  HTTP_422_UNPROCESSABLE_ENTITY,
  HTTP_401_UNAUTHORIZED
)

class BadRequestException(HTTPException):
  def __init__(self, details: List[ErrorDetails]) -> None:
    super().__init__(
      HTTP_400_BAD_REQUEST, 
      message = 'Bad Request Exception',
      body = {"details" : details}
    )

class UnprocessableEntityException(HTTPException):
  def __init__(self, details: List[ErrorDetails]) -> None:
    super().__init__(
      HTTP_422_UNPROCESSABLE_ENTITY, 
      message = 'Unprocessable Entity Exception',
      body = {"details" : details}
    )

class UnauthorizedException(HTTPException):
   def __init__(self, details: List[ErrorDetails]) -> None:
    super().__init__(
      HTTP_401_UNAUTHORIZED, 
      message = 'Unauthorized Exception',
      body = {"details" : details}
    )

class ForbiddenException(HTTPException):
  def __init__(self, details: List[ErrorDetails]) -> None:
    super().__init__(
      HTTP_403_FORBIDDEN, 
      message = 'Unauthorized Exception',
      body = {"details" : details}
    )
