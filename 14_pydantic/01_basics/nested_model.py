from typing import Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    name: str
    email: str
    address: Address
    phone: Optional[str] = None

address = Address(street="123 Main St", city="Anytown", state="CA", zip_code="12345")
user = User(name="John Doe", email="john.doe@example.com", address=address, phone="1234567890")

user_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip_code": "12345"
    },
    "phone": "1234567890"
}
user = User(**user_data)
print(user)