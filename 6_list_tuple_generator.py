#!/usr/bin/python3

def generate_tuple_and_lists():
    newlist=[]
    newtuple=()
    mylist=list(input("enter comma generated numbers: "))
    for i in range(0, len(mylist)):
        newlist.append(mylist[i])
        newtuple=tuple(newlist)

    print(newlist)
    print(newtuple)

if __name__ == "__main__":
    generate_tuple_and_lists()

