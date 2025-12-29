device_status = input("Enter the status of the device (on, off): ").lower()

if device_status == "on":
    temperature = float(input("Enter the temperature: "))
    if temperature > 35:
        print("High temperature detected, turning on the cooler")
    else:
        print("Temperature is within the safe range")
else:
    print("Device is off")