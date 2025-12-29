# String
chai_type = "Ginger Chai"
customer_name = "John"

print(f"Order for {customer_name} - {chai_type} please !")

chai_description = "Aromatic and bold with a hint of spice"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Reversed: {chai_description[::-1]}")

label_text = "Chai"
encoded_label = label_text.encode("utf-8")
print(f"Encoded label: {encoded_label!r}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")