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


#Day two:1 return length of string
def returnlengthofstr(string):
    return len(string)

#2count char frequency in string
def countcharfreq(string):
    dictionary = {}
    for i in string:
        keys = dictionary.keys()

        if i in keys:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    print(keys)
    return dictionary

#3get string of first and last 2 chars
def firstnlasttwo(string):
    mystr = string[:2] + string[-2:]
    return str(mystr)

#4 change all first letter occurences to $ sign
def changeletters(string):
    mychar = string[0]
    string = string.replace(mychar, '$')
    string = mychar + string[1:]
    return string

#5swap first 2 chars of 2 strings
def swapchars(string1, string2):
    new1 = string2[:2] + string1[2:]
    new2 = string1[:2] + string2[2:]
    return new1 + ' ' + new2

if __name__ == "__main__":
    string1 = "makena"
    string2 = "lynton"
    print(swapchars(string1, string2))
    print(changeletters("makenamakenamakena"))
    print(firstnlasttwo("Makena"))
    mynum = 5
    n_nn_nnn(mynum)
    print(printdocuments("math"))
    print(printcal(12, 2018))
    printmultiline()
    print(sphere_volume(9))
    print(returnlengthofstr("makena"))
    print(countcharfreq("makena"))
