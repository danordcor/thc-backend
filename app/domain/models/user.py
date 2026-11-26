from typing import Annotated, Self
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

UserName = Annotated[str, Field(min_length=1, max_length=100)]


class User(BaseModel):
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True)

    id: UUID
    name: UserName
    email: EmailStr

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        return value.lower()

    @classmethod
    def create(cls, name: str, email: str) -> Self:
        return cls(id=uuid4(), name=name, email=email)

    def update(self, name: str, email: str) -> Self:
        return type(self)(id=self.id, name=name, email=email)
