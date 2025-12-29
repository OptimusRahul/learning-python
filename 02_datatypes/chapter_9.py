essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential: {only_in_essential}")

only_in_optional = optional_spices - essential_spices
print(f"Only in optional: {only_in_optional}")

only_in_essential = essential_spices ^ optional_spices
print(f"Only in essential: {only_in_essential}")

only_in_optional = optional_spices ^ essential_spices
print(f"Only in optional: {only_in_optional}")