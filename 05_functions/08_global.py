chai_type = "Plain"

def front_desk():
    chai_type = "Elaichi"
    def kitchen():
        global chai_type
        chai_type = "Masala"
        print(f"Kitchen: Serving {chai_type} chai")
    kitchen()
    print(f"Front desk: Serving {chai_type} chai")

front_desk()
print(f"Outside function: Chai type: {chai_type}")