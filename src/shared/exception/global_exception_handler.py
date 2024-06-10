from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.exceptions import HTTPException

async def global_exception_handler(request: Request, exc):
  return JSONResponse({"error": str(exc)}, status_code=500)


async def http_exception_handler(request: Request, exc: HTTPException):
  return JSONResponse(
    status_code=exc.status_code,
    content={"message": exc.detail},
  )
