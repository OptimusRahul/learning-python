from recipe.flavours import elaichi_chai, ginger_chai, cardamom_chai, mint_chai, lemon_chai

def make_chai(flavour):
    if flavour == "elaichi":
        return elaichi_chai()
    elif flavour == "ginger":
        return ginger_chai()
    elif flavour == "cardamom":
        return cardamom_chai()
    elif flavour == "mint":
        return mint_chai()
    elif flavour == "lemon":
        return lemon_chai()

print(make_chai("elaichi"))
print(make_chai("ginger"))
print(make_chai("cardamom"))
print(make_chai("mint"))
print(make_chai("lemon"))