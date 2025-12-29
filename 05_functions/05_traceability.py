def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100

orders = [100, 150, 200]

for order in orders:
    vat_price = add_vat(order, 10)
    print(f"Order: {order}, VAT price: {vat_price}")