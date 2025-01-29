#!/usr/bin/python3

def firstnlast(mylist):
    return ("{} {}".format(mylist[0], mylist[-1]))

if __name__ == "__main__":
    mylist = ["head", "shoulders", "knees", "toes"]
    print(firstnlast(mylist))
