from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.api.schemas.user_schemas import CreateUserRequest, UpdateUserRequest, UserResource
from app.application.services.user_service import UserApplicationService
from app.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])

UserService = Annotated[UserApplicationService, Depends(get_user_service)]


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserResource)
def create_user(body: CreateUserRequest, user_service: UserService):
    user = user_service.create_user(name=body.name, email=body.email)
    return UserResource.from_domain(user)


@router.get("", response_model=list[UserResource])
def list_users(user_service: UserService):
    return [UserResource.from_domain(u) for u in user_service.list_users()]


@router.get("/{user_id}", response_model=UserResource)
def get_user(user_id: UUID, user_service: UserService):
    return UserResource.from_domain(user_service.get_user(user_id))


@router.put("/{user_id}", response_model=UserResource)
def update_user(user_id: UUID, body: UpdateUserRequest, user_service: UserService):
    user = user_service.update_user(user_id, name=body.name, email=body.email)
    return UserResource.from_domain(user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: UUID, user_service: UserService) -> None:
    user_service.delete_user(user_id)
