masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices
print(f"Main masala spice: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ginger ratio: {ginger_ratio}, Cardomom ratio: {cardamom_ratio}")

ginger_ratio, cardomom_ratio = cardamom_ratio, ginger_ratio
print(f"Ginger ratio: {ginger_ratio}, Cardomom ratio: {cardomom_ratio}")

# membershio

print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is cardamom in masala spices? {'cardamom' in masala_spices}")
print(f"Is cinnamon in masala spices? {'cinnamon' in masala_spices}")
