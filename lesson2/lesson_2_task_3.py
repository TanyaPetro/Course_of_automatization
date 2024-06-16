import math


side = float(input("Длина стороны квадрата"))


def square(side):
    if side % 1 == 0:
        print(side*side)
    else:
        print(math.ceil(side*side))


square(side)
