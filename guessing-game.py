def main():
    title = "THE PYTHON GUESSING GAME!"
    print(title)
    animal = "axolotl"
    zero = 0
    while zero == 0:
        guess = input("Guess what animal I am thinking of.")
        if guess.lower() == animal:
            zero += 1
            print("Congrats! You've guessed the animal.")
        elif guess.lower() == "quit":
            zero += 1
        else:
            print("Try again. Wrong animal.")
main()

            
            
    
