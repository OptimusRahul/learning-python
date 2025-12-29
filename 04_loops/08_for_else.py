staff = [("John", 14), ("Jane", 15), ("Jim", 16), ("Jill", 17)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the tea stall")
        break
else:
    print("No staff is eligible to manage the tea stall")