def make_chai():
    # return "Here is you masala chai"
    print("Here is you masala chai")

return_value = make_chai()
print(return_value)

def idle_chai_wala():
    pass

print(idle_chai_wala())

def sold_cups():
    return 120

total = sold_cups()
print(f"Total cups sold: {total}")

def chai_status(cups_left):
    if cups_left == 0:
        return "All sold out"
    return "Still some chai left"
    print("This will never be executed")

print(chai_status(0))
print(chai_status(10))

def chai_report():
    return 100, 20 #sold, remaining

sold, remaining = chai_report()
print(f"Sold: {sold}, Remaining: {remaining}")
