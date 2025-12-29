def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type # accessing the local variable in the outer function
        chai_type = "Masala"
        print(f"Kitchen: Serving {chai_type} chai")
    kitchen()
    print(f"Update order: Serving {chai_type} chai")

update_order()