input_seat = input("Enter the seat type 'sleeper' or 'ac' or 'first_class' or 'second_class': ").lower()

match input_seat:
    case "sleeper":
        print("Sleeper seat selected")
    case "ac":
        print("AC seat selected")
    case "first_class":
        print("First class seat selected")
    case "second_class":    
        print("Second class seat selected")
    case _:
        print("Invalid seat type")