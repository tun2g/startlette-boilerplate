from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from .shared.exception.global_exception_handler import global_exception_handler

app = Starlette(debug=True)

app.add_exception_handler(Exception, global_exception_handler)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["GET", "POST", "DELETE", "PATCH", "PUT"])
