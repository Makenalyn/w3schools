#!/usr/bin/python3

def sumlist(mylist=[]):
    total = 0
    for i in range(0, len(mylist)):
        total += mylist[i]

    return total
