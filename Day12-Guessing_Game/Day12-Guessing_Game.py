import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def get_random_number():
    number = list(range(1, 101))
    return random.choice(number)


def select_mode():
    turns = input("Enter 'E' or Easy Mode and 'H' for hard mode: ")
    if turns == "E":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    random_number = get_random_number()
    number_of_guesses = 0
    guessed = False
    while not guessed:
        players_guess = int(input("Guess a number between 1 and 100: "))
        number_of_guesses += 1
        if number_of_guesses == number_of_turns:
            print("To exceeded the number of turns. Please try again.")
            game()
        if players_guess == random_number:
            print(f"You guessed correctly! The answer is {random_number}")
            guessed = True
        elif players_guess < random_number:
            print("Too low.")
        else:
            print("Too high.")
        print(f"You have {number_of_turns - number_of_guesses} guesses left.")


print(art.art)
number_of_turns = select_mode()
game()
