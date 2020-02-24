# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Julianna Adler-Colvin
# Created: 2020-02-24

def getname():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    
    return first, last 

def buildname(first, last):
    return (first + "." + last)

def checkstrength(passwd):
    while len(passwd)<8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one…")
    return passwd

def main():
    # get user's first and last names
    first, last = getname()

    #GENERATE A MARIST-STYLE USERNAME
    uname = buildname(first,last)

    passwd = input("Create a new password: ")

    checkstrength(passwd)

    print("Account configured. Your new email address is", uname + "@marist.edu")
main()
