colors =["RED", "ORANGE", "GREEN", "BLUE", "INDIGO", "VIOLET", "BLACK", "WHITE", "BROWN"]

def showTitle():
    print ("Color Preference Evaluator")

def promptForColor():
    color = input("Enter a color: ")
    color = color.upper()
    color = color.strip()
    
    return color

def confirmColor(color):

    while (1==1):
    
        yesno = input("You have entered " +color+ ". Is this correct? (Y/N)? ")

        if (yesno.lower() == "y"):
            return True
        elif(yesno.lower()=="n"):
            return False
        else:
            print("Invalid input.")
    

def containsElement(color):
    for x in colors:
        if (color==x):
            return True
    return False

def praiseUser():
    print("Great job, that color is valid!")

def ridiculeUSER():
    print("Bad job that color is invalid!")

def main():
    showTitle()
    color = promptForColor()
    dogbowl = 0
    while (confirmColor (color)!=True):
        color = promptForColor()
        color = color.upper()
    if (containsElement(color)==True):
        praiseUser()
    else:
        ridiculeUser()

main()
