import random
import art


players_sum = 0
dealers_sum = 0
players_hand = []
dealers_hand = []


def get_random_card():
    """provide provides random card"""
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


play_again = True
ask_to_play_again = input("Do want to play a game of Blackjack? Type 'y' or n': ").lower()
while play_again:
    if ask_to_play_again == 'y':
        print(art.logo)
        for _ in range(2):
            players_hand.append(get_random_card())
            dealers_hand.append(get_random_card())


        print(f"[+] Your cards: {players_hand}, current score {}")
        print(f"[+] Dealers first card: {dealers_hand[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
    if another_card == 'n':
        print(f"[+] Your final hand: {players_hand}, final score ")
        print(f"[+] Dealers first card: {dealers_hand}, final score ")


# initial notes for the game
# Ask, you want to play black jack y,n #### done
# if Yes,
# show logo and show :your cards and current score
# show "computers first card"

# ask y to get another card or n to pass
# if no or lost
# computer has to hit under = to 16?
# Show logo
# Show user final hand
# Show computer hand
# Show if you won
# ask if you want to play another game
