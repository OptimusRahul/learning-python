# Integer

black_tea_grams = 14
ginger_grams = 3

total_tea_grams = black_tea_grams + ginger_grams
print(f"Total tea grams: {total_tea_grams}")

remaining_tea_grams = total_tea_grams - ginger_grams
print(f"Remaining tea grams: {remaining_tea_grams}")

milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(f"Milk per serving: {milk_per_serving}")

total_tea_bags = 7
pots = 4
tea_bags_per_pot = total_tea_bags // pots
print(f"Tea bags per pot: {tea_bags_per_pot}")

total_cardomom_pods = 10
pods_per_cup = 3
left_over_pods = total_cardomom_pods % pods_per_cup
print(f"Left over pods: {left_over_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor_strength = base_flavor_strength ** scale_factor
print(f"Powerful flavor strength: {powerful_flavor_strength}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")
