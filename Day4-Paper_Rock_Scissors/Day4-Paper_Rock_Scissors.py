import random
from random import randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

guess = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
option = [rock, paper, scissors]
computer_guess = random.randint(0, 2)


print(f"""You chose {guess}:
{option[guess]}""")

print(f"""Computer chose {computer_guess}:
{option[computer_guess]}""")

if guess == computer_guess:
    print("You Tied!")

elif guess == 0 and computer_guess == 2:
    print("You Win!")

elif guess == 1 and computer_guess == 0:
    print("You Win!")

elif guess == 2 and computer_guess == 1:
    print("You Win!")

else:
    print("You Lose!")




