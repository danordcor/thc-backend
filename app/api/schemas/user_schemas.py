from typing import Self
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr

from app.domain.models.user import User, UserName


class CreateUserRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    name: UserName
    email: EmailStr


class UpdateUserRequest(CreateUserRequest):
    pass


class UserResource(BaseModel):
    id: UUID
    name: str
    email: str

    @classmethod
    def from_domain(cls, user: User) -> Self:
        return cls(id=user.id, name=user.name, email=user.email)
