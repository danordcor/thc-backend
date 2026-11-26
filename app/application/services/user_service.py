from uuid import UUID 

from app.domain.models.user import User 
from app.domain.ports.user_ports import UserRepository
from app.domain.services.errors.user_errors import UserNotFoundError
from app.domain.services.user_validator import UserValidator


class UserApplicationService: 
    def __init__(self, user_repository: UserRepository, validator: UserValidator) -> None:
        self._user_repository = user_repository
        self._validator = validator

    def create_user(self, name: str, email: str) -> User:
        user = User.create(name=name, email=email)
        self._validator.validate_email_available(user.email)
        self._user_repository.save(user)
        return user

    def list_users(self) -> list[User]:
        return self._user_repository.list_all()

    def get_user(self, user_id: UUID) -> User:
        user = self._user_repository.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError(user_id)
        return user

    def update_user(self, user_id: UUID, name: str, email: str) -> User:
        current = self.get_user(user_id)
        updated = current.update(name=name, email=email)
        self._validator.validate_email_available(updated.email, current_user_id=current.id)
        self._user_repository.save(updated)
        return updated

    def delete_user(self, user_id: UUID) -> None:
        self.get_user(user_id)
        self._user_repository.delete(user_id)


