def infinte_chai():
    count = 1
    while True:
        yield f"Masala Chai {count}"
        count += 1

stall = infinte_chai()

for _ in range(10):
    print(next(stall))