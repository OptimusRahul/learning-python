order_amount = float(input("Enter the order amount: "))

delivery_fee = 0 if order_amount > 300 else 30
print(f"Delivery fee: {delivery_fee}")