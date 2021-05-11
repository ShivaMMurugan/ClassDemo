import random


def play_game():
    choices = 0
    while choices < 7:
        user_input = int(input("Enter a number between 1 to 10: "))
        random_number = random.randrange(1, 11)
        if user_input == random_number:
            print("You have got the correct number {} ".format(user_input))
            break
        else:
            choices += 1
            print("Invalid Guess, choice used so far is >> {}".format(choices))
    print("Please Veetuku Poidu {} Chances Mudinjithu...".format(choices))


play_game()


def ask_again():
    while True:
        ask = (input("Would you like to play again? Type Yes or No to continue: "))
        if ask.lower() == "yes":
            play_game()
        else:
            print("Thanks playing...")
            break


ask_again()
