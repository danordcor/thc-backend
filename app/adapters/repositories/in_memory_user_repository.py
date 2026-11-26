from uuid import UUID

from app.domain.models.user import User


class InMemoryUserRepository:
    def __init__(self) -> None:
        self._users: dict[UUID, User] = {}

    def save(self, user: User) -> None:
        self._users[user.id] = user

    def get_by_id(self, user_id: UUID) -> User | None:
        return self._users.get(user_id)

    def get_by_email(self, email: str) -> User | None:
        normalized = email.strip().lower()
        return next((u for u in self._users.values() if u.email == normalized), None)

    def list_all(self) -> list[User]:
        return list(self._users.values())

    def delete(self, user_id: UUID) -> None:
        self._users.pop(user_id, None)
