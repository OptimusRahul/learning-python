class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

masala = Chai()
print(f"Masala chai is hot: {masala.origin}")
print(f"Masala chai is hot: {masala.is_hot}")
masala.is_hot = False

print("Chai class is hot: ", Chai.is_hot)
print(f"Masala chai is hot: {masala.is_hot}")
masala.flavour = "Masala"
print(f"Masala chai flavour: {masala.flavour}")