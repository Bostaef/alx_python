import importlib

a = 1
b = 2

add_0 = importlib.import_module("add_0")
result = add_0.add(a, b)

print("{:d} + {:d} = {:d}".format(a, b, result))

if __name__ == "__main__":
    pass 