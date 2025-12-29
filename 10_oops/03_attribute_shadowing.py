class Chai:
    temperature = "Hot"
    strength = "Strong"

cutting = Chai()
print(f"Cutting chai temperature: {cutting.temperature}")

cutting.temperature = "Mild"
cutting.cup = "Small"
print(f"Cutting chai temperature: {cutting.temperature}")
print(f"Cutting chai cup: {cutting.cup}")
print(f"Chai class temperature: {Chai.temperature}")
print(f"Chai class cup: {Chai.cup}")

del cutting.temperature
del cutting.cup
print(f"Cutting chai temperature: {cutting.temperature}")
print(f"Cutting chai cup: {cutting.cup}")