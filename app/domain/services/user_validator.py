from uuid import UUID 

from app.domain.ports.user_ports import UserRepository 
from app.domain.services.errors.user_errors import UserConflictError 


class UserValidator: 
    def __init__(self, user_repository: UserRepository) -> None: 
        self._user_repository = user_repository 

    def validate_email_available(self, email: str, current_user_id: UUID | None = None) -> None: 
        existing = self._user_repository.get_by_email(email)
        if existing is not None and existing.id != current_user_id: 
            raise UserConflictError(email)


