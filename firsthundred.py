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

if __name__ == "__main__":
    mynum = 5
    n_nn_nnn(mynum)
    string = "math"
    print(printdocuments(string))
