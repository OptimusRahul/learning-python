def chai_customer():
    print("Welcome to the chai customer")
    order = yield
    while True:
        print(f"Preparing {order}")
        order = yield

stall = chai_customer()
next(stall)
stall.send("Masala Chai")
stall.send("Iced Lemon Tea")
stall.send("Green Tea")
stall.send("Iced Peach Tea")
stall.send("Ginger Chai")