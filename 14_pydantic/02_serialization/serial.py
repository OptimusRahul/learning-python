from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")}
    )


user = User(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    is_active=True,
    created_at=datetime(2025, 1, 1, 12, 0, 0),
    address=Address(street="123 Main St", city="Anytown", zip_code="12345"),
    tags=["admin", "user"],
)

python_dict = user.model_dump()

print(user)
print("="*30)
print(python_dict)

json_data = user.model_dump_json()
print("="*30)
print(json_data)