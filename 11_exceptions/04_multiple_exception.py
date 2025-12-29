def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost  = price * quantity
        print(f"The cost of the {item} chai is {cost}")
    except KeyError:
        print(f"Sorry, we don't have {item} in the menu")
    except TypeError:
        print(f"Invalid quantity: {quantity}")
    except Exception as e:
        print(f"An error occurred: {e}")

process_order("masala", 2)
process_order("elaichi", 2)
process_order("masala", "two")