#!/usr/bin/python3

#function returns the n + nn + nnn
def n_nn_nnn(num):
    n1 = int("{}".format(num))
    n2 = int("{}{}".format(num, num))
    n3 = int("{}{}{}".format(num, num, num))

    print("{}".format(n1 + n2 + n3))

if __name__ == "__main__":
    mynum = 5
    n_nn_nnn(mynum)
