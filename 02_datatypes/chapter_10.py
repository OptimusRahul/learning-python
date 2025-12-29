chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "water"
print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe liquid: {chai_recipe['liquid']}")
del chai_recipe["liquid"]
print(f"Recipe base: {chai_recipe}")

print(f"Is sugaar in order? {'sugar' in chai_order}")

print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Last item: {last_item}")
print(f"Chai order: {chai_order}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Chai recipe: {chai_recipe}")

customer_note = chai_order.get('customer_note', "No Note")
print(f"Customer note: {customer_note}")