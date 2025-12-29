def serve_chai():
    yield "Masala Chai"
    yield "Iced Lemon Tea"
    yield "Green Tea"
    yield "Iced Peach Tea"
    yield "Ginger Chai"

stall = serve_chai()
print(stall)
print(next(stall))
print(next(stall))
print(next(stall))
print(next(stall))
print(next(stall))