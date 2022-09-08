import random
import ascii_art
import wordlist

word_list = wordlist.word_list

# Randomly choose a word from the word_list.
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
answer = list()
lives = 8
count = -1

for i in range(0, len(chosen_word)):
    answer.append("_")

all_letters_guessed = False
last_guessed = []
while not all_letters_guessed:
    if count + lives == 0:
        print(f'You lose. Word was: {chosen_word} ')
        break

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Take a guess: ").lower()
    # Create an empty List called display.
    # Loop through each position in the chosen_word;

    correctly_guessed_letter = False

    for i, letter in enumerate(chosen_word):

        # if guess correctly
        if letter == guess:
            answer[i] = guess
            correctly_guessed_letter = True

    if guess not in last_guessed:

        if correctly_guessed_letter != True and guess not in last_guessed:
            print(ascii_art.stages[count])
            count -= 1

    else:
        print(f"You guess {guess} before. Try again")

    if guess not in last_guessed:
        last_guessed.append(guess)


    print(answer)
    if "_" not in answer:
        print("You Win! Game Over. ")
        all_letters_guessed = True



