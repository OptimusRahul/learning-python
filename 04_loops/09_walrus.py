# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisble, remainder is {remainder}")
# else:
#     print("No remainder")

value = 13
if (remainder := value % 5):
    print(f"Not divisble, remainder is {remainder}")
else:
    print("No remainder")

available_sizes = ["small", "medium", "large"]
if(required_size := input("Enter the size of the chai (small, medium, large): ").lower()) not in available_sizes:
    print("Invalid size")
else:
    print(f"You chose: {required_size}")

flavors = ["ginger", "cardamom", "mint"]
while(selected_flavor := input("Enter the flavor of the chai (ginger, cardamom, mint): ").lower()) not in flavors:
    print(f"Sorry, {selected_flavor} is not available. Please try again.")

print(f"You chose: {selected_flavor} chai")