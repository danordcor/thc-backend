from fastapi import Request

from app.adapters.repositories.in_memory_user_repository import InMemoryUserRepository
from app.application.services.user_service import UserApplicationService
from app.domain.services.user_validator import UserValidator


def build_user_service() -> UserApplicationService:
    user_repository = InMemoryUserRepository()
    validator = UserValidator(user_repository)
    return UserApplicationService(user_repository, validator)


def get_user_service(request: Request) -> UserApplicationService:
    return request.app.state.user_service
