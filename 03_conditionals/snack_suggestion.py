snack = input("Enter your preferred snack: ").lower()
print(f"You chose: {snack}")

if snack == "cookies" or snack == "chips":
    print(f"Great choice! We will serve: {snack}")
else:
    print("Not available")