from typing import List

class ErrorDetails:
  def __init__(self, issue_id: str | None, issue: str, field: str | None):
    self.issue_id = issue_id
    self.issue = issue
    self.field = field

class ErrorResponseBody:
  def __init__(self, message: str, request_id: str,details: List[ErrorDetails]):
    self.message = message
    self.request_id = request_id
    self.details = details