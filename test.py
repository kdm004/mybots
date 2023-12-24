import constants as c

# print(c.botPositions[0])

def dummy_func(x, y, z=1):
    print(x)
    print(y)
    print(z)

test1 = dummy_func(*c.botPositions[0])