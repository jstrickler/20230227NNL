
x = 100  # global

def spam():
    x = 42   # local variable  (only visible inside function)

spam()

print(f"x: {x}")


