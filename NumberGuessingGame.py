# GUESSING GAME ---------
print("Welcome to the Guessing Game")
print("You have three chances to guess the number")
print("CLUE: The number lies between 1 and 10")
print("Get Ready")
secret_num = 7
guess_limit = 3
guess_count = 0
while guess_count<guess_limit:
    guess = int(input("Guess a number: "))
    guess_count += 1
    if guess==secret_num:
        print("Wohoo! You guessed the number right!")
        break #terminates the loop
    else:
        print("Sorry, that's not right.")
else:
    print("Sorry, you haven't guessed the number right!")