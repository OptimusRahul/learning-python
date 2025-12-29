# chai = "Masala Chai"

# def prepare_chai(order):
#     print(f"Preparing {order}")

# prepare_chai(chai)
# print(f"Chai: {chai}")

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(f"Chai: {chai}")

def make_chai(tea, milk, sugar):
    print(f"Making chai with {tea} tea, {milk} milk, and {sugar} sugar")

make_chai("black tea", "full fat", 2)
make_chai(sugar=2,tea="black tea", milk="full fat")

def special_chai(*ingredients, **extras):
    print(f"Making chai with {ingredients} and {extras}")

special_chai("Cardamom", "Ginger", sugar=2, milk="full fat")

def chai_order(order=None):
    if order is None:
        order = []
    order.append("Masala")
    print(f"order: {order}")

chai_order()
chai_order()