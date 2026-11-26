from fastapi import FastAPI

from app.api import health_endpoint, users_endpoint
from app.api.exception_handlers import register_exception_handlers
from app.config import config_by_name
from app.dependencies import build_user_service


def create_app(config_name: str | None = None) -> FastAPI:
    app = FastAPI(title="Mentoria API")
    app.state.config = config_by_name[config_name or "development"]
    app.state.user_service = build_user_service()

    register_exception_handlers(app)
    app.include_router(health_endpoint.router)
    app.include_router(users_endpoint.router)
    return app
