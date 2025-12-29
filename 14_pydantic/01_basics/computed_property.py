from pydantic import BaseModel, computed_field

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
product = Product(price=100, quantity=10)
print(product.total_price)

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    
booking = Booking(user_id=1, room_id=1, nights=3, rate_per_night=100)
print(booking.total_amount)
print(booking.model_dump_json())