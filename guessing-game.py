def main():
    title = "THE PYTHON GUESSING GAME!"
    print(title)
    animal = "axolotl"
    zero = 0
    while zero == 0:
        print("I am thinking of an animal.")
        guess = input("Guess what animal I am thinking of.")
        if guess.lower() == animal:
            zero += 1
            print("Congrats! You've guessed the animal.")
            Theaxolotl = 0
            while Theaxolotl == 0:
                response = input("Do you like this animal? Y/N: ")
                if response[0].lower() == "n":
                    print("Boo. The axolotl is a great animal!")
                    Theaxolotl += 1
                elif response [0].lower() == "y":
                    print("Great! I love this animal too.")
                    Theaxolotl += 1
        elif guess[0].lower() == "q":
            zero += 1
        else:
            print("Try again. Wrong animal.")
    print ("Play again!")
main()

            
            
    
