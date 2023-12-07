a = 1
b = 2


result = __import__("add_0").add(a, b)

print("{:d} + {:d} = {:d}".format(a, b, result))

if __name__ == "__main__":
    pass 