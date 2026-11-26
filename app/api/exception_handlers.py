from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.domain.services.errors.user_errors import UserConflictError, UserNotFoundError


async def user_not_found_handler(request: Request, exc: UserNotFoundError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": str(exc)})


async def user_conflict_handler(request: Request, exc: UserConflictError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"error": str(exc)})


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(UserNotFoundError, user_not_found_handler)
    app.add_exception_handler(UserConflictError, user_conflict_handler)
