from typing import Protocol
from uuid import UUID 

from app.domain.models.user import User 

class UserRepository(Protocol): 
    def save(self, user: User) -> None: ...

    def get_by_id(self, user_id: UUID) -> User | None: ...

    def get_by_email(self, email: str) -> User | None: ...

    def list_all(self) -> list[User]: ... 

    def delete(self, user_id: UUID) -> None: ...


