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

if __name__ == "__main__":
    mynum = 5
    n_nn_nnn(mynum)
    print(printdocuments("math"))
    print(printcal(12, 2018))
