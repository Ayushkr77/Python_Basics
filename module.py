# import math as m   # alias, now we have to write m only, otherwise eror
# print(m.pi)

# from math import pi   # prefer above one onlywither with or wothout alias according to ur choice
# print(pi)  # pi is now in the local scope, we can use it directly

import math as m

str="hello"

def calculate_area(radius):
    return m.pi * (radius ** 2)

def calculate_circumference(radius):
    return 2 * m.pi * radius
print(calculate_circumference(7))  