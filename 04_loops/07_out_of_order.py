flavours = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Spiced", "Mint"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"Enjoy your {flavour} chai!")