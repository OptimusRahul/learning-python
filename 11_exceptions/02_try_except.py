chai_menu = {'masala': 30, 'ginger': 40}

try:
    chai_menu['elaichi']
except KeyError:
    print("Sorry, we don't have elaichi in the menu")

print("Hello World")