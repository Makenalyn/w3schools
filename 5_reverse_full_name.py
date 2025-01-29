#!/usr/bin/python3

def reversenames():
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")

    print("{} {}".format(lastname, firstname))

if __name__ == "__main__":
    reversenames()
