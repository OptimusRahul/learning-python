from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product = Product(id=1, name="Chai", price=10.0, in_stock=True)
print(product)

product_two = Product(id=2, name="Coffee", price=15.0)
print(product_two)

product_three = Product(id=3, name="Tea")
print(product_three)