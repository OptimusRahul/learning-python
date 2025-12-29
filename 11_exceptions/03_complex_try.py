def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == 'unknown':
            raise ValueError("We don't have this flavour in the menu")
    except ValueError as e:
        print(f"Error: {e}")
        return None
    else: 
        print(f"Here is your {flavour} chai")
    finally:
        print("Thank you for visiting our chai shop")

print(serve_chai('masala'))
print(serve_chai('unknown'))
print(serve_chai('cardamom'))