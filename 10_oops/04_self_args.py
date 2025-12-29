class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"This is a {self.size}ml cup"

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 200
print(cup_two.describe())
print(Chaicup.describe(cup_two))