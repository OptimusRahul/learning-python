from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")
    def name_must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError("Name must be capitalized")
        return v
    
person = Person(first_name="John", last_name="Doe")
print(person)

class User(BaseModel):
    email: str

    @field_validator("email")
    def normalize_email(cls, v):
        return v.lower().strip()

user = User(email="Test@example.com")
print(user)

class Product(BaseModel):
    price: float # $4.44

    @field_validator("price", mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v
    
product = Product(price="$4.44")
print(product)

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')    
    def check_dates(self):
        if self.start_date > self.end_date:
            raise ValueError("Start date must be before end date")
        return self
    
date_range = DateRange(start_date=datetime(2025, 1, 1), end_date=datetime(2025, 1, 10))
print(date_range)