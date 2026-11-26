from uuid import UUID


class UserError(Exception):
    pass


class UserNotFoundError(UserError):
    def __init__(self, user_id: UUID) -> None:
        super().__init__(f"User {user_id} not found")
        self.user_id = user_id


class UserConflictError(UserError):
    def __init__(self, email: str) -> None:
        super().__init__(f"Email {email} is already in use")
        self.email = email
