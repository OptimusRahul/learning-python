def local_chai():
    yield "Masala Chai"
    yield "Iced Lemon Tea"

def imported_chai():
    yield "Matcha Chai"
    yield "Oolong Chai"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for order"
    except:
        print("Stall Closed, No more chai")

stall = chai_stall()
print(next(stall))
stall.close()