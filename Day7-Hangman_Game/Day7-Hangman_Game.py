import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list.
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
answer = list()
for i in range(0, len(chosen_word)):
    answer.append("_")

all_letters_guessed = False
while not all_letters_guessed:

    print(f"Chosen word is: {chosen_word}")

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Take a guess: ").lower()
    # Create an empty List called display.
    # Loop through each position in the chosen_word;
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            answer[i] = guess

    print(answer)
    if "_" not in answer:
        print("You Win! Game Over. ")
        all_letters_guessed = True



