class ClassOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def describe(self):
        return f"This is a {self.type} {self.size}ml cup"

order = ClassOrder("Small", 150)
print(order.describe())

order_two = ClassOrder("Large", 200)
print(order_two.describe())

