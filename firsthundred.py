#!/usr/bin/python3

#function returns the n + nn + nnn
def n_nn_nnn(num):
    n1 = int("{}".format(num))
    n2 = int("{}{}".format(num, num))
    n3 = int("{}{}{}".format(num, num, num))

    print("{}".format(n1 + n2 + n3))


#print documents of python builtin functions
def printdocuments(module_name):
    try:
        module = __import__(module_name)
        return module.__doc__
    except ImportError:
        return f"Module {module_name} not found"

#print calendar of a given month and year
def printcal(month, year):
    import calendar
    print(calendar.month(year, month))

#printmultilinecomments
def printmultiline():
    print("""
            This is a multiline string
            dont you understand
            """
            )

#get the volume of a sphere with radius
def sphere_volume(radius):
    import math
    pi = math.pi
    radius_cubed = radius * radius * radius
    volume = pi * radius_cubed * 4 / 3
    return volume


#return length of string
def returnlengthofstr(string):
    return len(string)

#count char frequency in string
def countcharfreq(string):
    dict = {}
    for i in string:
        keys = dict.keys()

        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

if __name__ == "__main__":
    mynum = 5
    n_nn_nnn(mynum)
    print(printdocuments("math"))
    print(printcal(12, 2018))
    printmultiline()
    print(sphere_volume(9))
    print(returnlengthofstr("makena"))
    print(countcharfreq("makena"))
