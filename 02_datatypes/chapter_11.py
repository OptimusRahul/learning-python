# import arrow

# brewing_time = arrow.utcnow()
# print(f"Brewing time: {brewing_time}")

from collections import namedtuple

Chai = namedtuple("Chai", ["type", "size", "sugar", "milk", "spices"])
print(f"Chai type: {Chai.type}")

chai_order = Chai(type="Masala Chai", size="Large", sugar=2, milk="Full Fat", spices=["cardamom", "ginger"])
print(f"Chai order: {chai_order}")

print(f"Chai type: {chai_order.type}")
print(f"Chai size: {chai_order.size}")
print(f"Chai sugar: {chai_order.sugar}")
print(f"Chai milk: {chai_order.milk}")
print(f"Chai spices: {chai_order.spices}")