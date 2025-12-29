class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk < 100 or sugar < 10:
        raise OutOfIngredientsError("Not enough ingredients")
    print(f"Making chai with {milk} ml of milk and {sugar} g of sugar")

make_chai(90, 9)
make_chai(100, 10)