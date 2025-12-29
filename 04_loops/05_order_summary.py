from typing import Any


names = ["John", "Jane", "Jim", "Jill"]
biils = [100, 200, 300, 400]

for name, bill in zip(names, biils):
    print(f"Customer: {name}, Bill: {bill}")    