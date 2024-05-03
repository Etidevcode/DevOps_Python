# Defining Function
def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(257, 4845)
print(out)

def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)

adder(2057, 156)

def sum(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

out = sum([22, 45, 81])
print(out)

# Default argument
def greeting(MSG = "Morning"):
    print(f"Good {MSG}")
    print("Welcome to the function.")

greeting()
greeting("Evening")
