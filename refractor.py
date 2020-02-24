# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Julianna Adler-Colvin
# Created: 2020-02-24

def getname():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    
    return first, last 

def buildname(first, last):
    fullname = first + "." + last
    return (fullname.lower())

def getPass():
    passwd= input("Create a new password:")
    realstrength(passwd)
    print("The force is strong with this one...")
    return passwd

def realstrength(passwd):
    while len(passwd)<8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    while (passwd.isupper() or passwd.islower()):
        print("Password not strong enough, use both upper and lower case.")
        passwd = input("Create a new password.")

def main():
    # get user's first and last names
    first, last = getname()

    #GENERATE A MARIST-STYLE USERNAME
    uname = buildname(first,last)

    getPass() 

    print("Account configured. Your new email address is", uname + "@marist.edu")
main()
