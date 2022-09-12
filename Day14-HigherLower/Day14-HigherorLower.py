import random
from random import randint
import art
import game_data
from platform import system as system_name  # Returns the system/OS name
from subprocess import call as system_call  # Execute a shell command


def clear_screen():
    """
    Clears the terminal screen.
    """
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    # Executes
    system_call([command])


def grab_question(compare: str):
    score = game_data.data[random.randint(0, len(game_data.data) - 1)]
    print(f"{compare} {score['name']}, "
          f"a {score['description']}, "
          f"from {score['country']} ")
    return score['follower_count']


def compare(compare: int, against: int):
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == 'a':
        guess = compare
    else:
        guess = against

    if guess == compare and compare > against:
        print("You Win")
        return 1

    elif guess == against and against > compare:
        print("You Win")
        return 1
    else:
        print("You Lose")
        return 0


flag = True
score = 0

while flag:
    print(art.logo)
    compareA = grab_question("Compare A: ")
    print(compareA)
    print(art.vs)
    againstB = grab_question("Against B: ")
    if compareA == againstB:
        compareA = grab_question("Compare A: ")
    print(againstB)
    correct = compare(compareA, againstB)
    if correct:
        score += 1
        clear_screen()
        print(f"Current score: {score}")
    else:
        clear_screen()
        print(f"Sorry, that's wrong. Final score: {score}")
        score = 0
        flag = False

# Compare the two scores


# If correct, add point
# show two other questions
# Else, that's wrong Final Score


# compare two terms
# if right show
# You are right! Current Score: 1
# Compare A: Name, operation, from
# then VS symbol
# Compare A: Name, operation, from

# keep score
# keep going until you are wrong
# Sorry, that's wong. Final score: 3
