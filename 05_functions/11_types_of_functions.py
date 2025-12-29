def pure_chai(cups):
    return cups * 10

total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups
    return total_chai

print(pure_chai(10))
print(total_chai)
print(impure_chai(10))
print(total_chai)

def pour_chai(n):
    print(f"Pouring {n} cups")
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(6))

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))
print(strong_chai)
