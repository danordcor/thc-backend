import pytest 
from pydantic import ValidationError 

from app.domain.models.user import User 

def test_create_normalizes_fields():
    user = User.create(name="  Dan  ", email="Dan@Mentoria.dev ")
    assert user.name == "Dan"
    assert user.email == "dan@mentoria.dev"

def test_blank_name_is_rejected(): 
    with pytest.raises(ValidationError): 
        User.create(name="   ", email="dan@mentoria.dev")

def test_update_keeps_id_and_revalidate():
    user = User.create(name="Dan", email="dan@mentoria.dev")
    assert user.update(name="Dan. O", email="dan@mentoria.dev").id == user.id 
    with pytest.raises(ValidationError):
        user.update(name="Dan", email="invalid_email")
