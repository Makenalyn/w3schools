#!/usr/bin/python3

import datetime
def currentDate():
    x = datetime.datetime.now()
    print("{}".format(x.strftime("%Y-%m-%d %H:%M:%S")))

if __name__ == "__main__":
    currentDate()
