from uuid import uuid4

import pytest

from app.adapters.repositories.in_memory_user_repository import InMemoryUserRepository
from app.application.services.user_service import UserApplicationService
from app.domain.services.errors.user_errors import UserConflictError, UserNotFoundError
from app.domain.services.user_validator import UserValidator


@pytest.fixture
def service() -> UserApplicationService:
    repository = InMemoryUserRepository()
    return UserApplicationService(repository, UserValidator(repository))


def test_create_user_saves_it(service):
    user = service.create_user(name="Ada", email="ada@mentoria.dev")

    assert service.get_user(user.id) == user


def test_duplicate_email_is_rejected(service):
    service.create_user(name="Ada", email="ada@mentoria.dev")

    with pytest.raises(UserConflictError):
        service.create_user(name="Otra", email="ADA@mentoria.dev")


def test_update_to_own_email_is_allowed(service):
    user = service.create_user(name="Ada", email="ada@mentoria.dev")
    updated = service.update_user(user.id, name="Ada L.", email="ada@mentoria.dev")

    assert updated.name == "Ada L."


def test_update_to_taken_email_is_rejected(service):
    service.create_user(name="Ada", email="ada@mentoria.dev")
    other = service.create_user(name="Grace", email="grace@mentoria.dev")

    with pytest.raises(UserConflictError):
        service.update_user(other.id, name="Grace", email="ada@mentoria.dev")


def test_get_missing_user_raises(service):
    with pytest.raises(UserNotFoundError):
        service.get_user(uuid4())


def test_delete_then_get_raises(service):
    user = service.create_user(name="Ada", email="ada@mentoria.dev")
    service.delete_user(user.id)

    with pytest.raises(UserNotFoundError):
        service.get_user(user.id)
