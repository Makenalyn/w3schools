#!/usr/bin/python3

import math
def area_of_circle():
    PI = float(math.pi)
    rad = int(input("Enter the radius: "))
    area = PI * rad * rad
    print(area)

if __name__ == "__main__":
    area_of_circle()
