size = input("Enter the size of the chai (small, medium, large): ").lower()
print(f"You chose: {size}")

if size == "small":
    price = 10
elif size == "medium":
    price = 15
elif size == "large":
    price = 20
else:
    print("Invalid size")
    price = 0

print(f"The price of the chai is: {price}")