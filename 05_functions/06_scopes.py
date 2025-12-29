def serve_chai():
    chai_type = "Masala Chai" # local scope
    print(f"Inside function: Serving {chai_type} chai")

chai_type = "Lemon" # global scope
serve_chai()
print(f"Outside function: Chai type: {chai_type}") # NameError: name 'chai_type' is not defined

def chai_counter():
    chai_order = "Lemon"
    def print_order():
        chai_order = "Masala"
        print(f"Inside nested function: Serving {chai_order} chai")
    print_order()
    print(f"Outside nested function: Chai order: {chai_order}")

chai_counter()