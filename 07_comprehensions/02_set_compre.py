spices = ["Masala Chai", "Iced Peach Tea", "Green Tea", "Iced Peach Tea", "Ginger Chai", "Green Tea"]

strong_spices = {spice for spice in spices}
print(strong_spices)

recipes = {
    "Masala Chai": ["cardamom", "ginger", "cinnamon"],
    "Iced Peach Tea": ["peach", "lemon", "mint"],
    "Green Tea": ["green tea", "lemon", "mint"],
    "Ginger Chai": ["ginger", "cinnamon"],
}

unique_spices = {spice for recipe in recipes.values() for spice in recipe}
print(unique_spices)