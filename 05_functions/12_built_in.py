def chai_flavour(flavour="masala"):
    """Return the flavour of the chai"""
    return flavour

print(chai_flavour.__doc__)
print(chai_flavour.__name__)
print(chai_flavour.__module__)
print(chai_flavour.__dict__)
print(chai_flavour.__code__)

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for the chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: Total bill
    """
    return (chai * 10) + (samosa * 15)

