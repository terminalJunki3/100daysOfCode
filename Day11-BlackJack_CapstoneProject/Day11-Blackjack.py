import random
import art

players_hand = []
dealers_hand = []


def get_random_card():
    """provide provides random card"""
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def draw_single_card():
    players_hand.append(get_random_card())
    show_cards_and_score()


def show_cards_and_score():
    print(f"[+] Your cards: {players_hand}, current score {calculate_score(players_hand)}")
    print(f"[+] Dealers first card: {dealers_hand[0]}")


def final_score():
    print(f"[+] Your final hand: {players_hand}, final score: {calculate_score(players_hand)}")
    print(f"[+] Dealers final hand: {dealers_hand}, final score {calculate_score(dealers_hand)} ")
    again()


def calculate_score(hand: list):
    """ Calculate the score for the player and the dealer """
    replaced_ace = False
    sum_of_hand = sum(hand)
    # if sum_of_hand == 21 and len(hand) == 2:
    #     return sum_of_hand

    if 11 in hand and sum_of_hand > 21:
        """Checks if there is an Ace and replaces it if its under 21"""
        find_ace = hand.index(11)
        hand[find_ace] = 1
        if sum_of_hand > 21:
            return sum_of_hand
        else:
            return sum_of_hand
    elif sum_of_hand > 21:
        return sum_of_hand
    else:
        return sum_of_hand


def game():
    print(art.logo)
    for _ in range(2):
        players_hand.append(get_random_card())
        dealers_hand.append(get_random_card())
        if calculate_score(players_hand) == 21 and len(players_hand) == 2:
            print("Black Jack! You win")
            final_score()
    show_cards_and_score()

    another_card_bool = True
    while another_card_bool:
        if calculate_score(players_hand) > 21:
            print("You busted!")
            final_score()

        another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if another_card == 'n':
            ## Calculate dealers score here
            while calculate_score(dealers_hand) < 17:
                dealers_hand.append(get_random_card())
            print(f"[+] Your final hand: {players_hand}, final score: {calculate_score(players_hand)}")
            print(f"[+] Dealers final hand: {dealers_hand}, final score {calculate_score(dealers_hand)} ")

            if calculate_score(players_hand) > calculate_score(dealers_hand):
                print("You win!")
            elif calculate_score(players_hand) == calculate_score(dealers_hand):
                print("You Tied")

            elif calculate_score(dealers_hand) > 21:
                print("You Win. Dealer Busted")

            elif calculate_score(players_hand) < calculate_score(dealers_hand):
                print("You lose!")
            break
        else:
            draw_single_card()


def again():
    play_again = True
    while play_again:
        ask_to_play_again = input("Do want to play a game of Blackjack? Type 'y' or n': ").lower()
        players_hand.clear()
        dealers_hand.clear()
        if ask_to_play_again == 'n':
            print("[-] Good bye.")
            break
        game()


again()
