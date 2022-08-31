from platform import system as system_name  # Returns the system/OS name
from subprocess import call as system_call  # Execute a shell command
from art import logo


def clear_screen():
    """
    Clears the terminal screen.
    """
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    # Executes
    system_call([command])




bidding_over = False
highest_bid = 0
highest_bidder = None
bids = []
print(logo)

while not bidding_over:
    user_bid = {}

    name = input("What is your name?: ")
    try:
        bid = int(input("What is your bid?: $"))
    except ValueError as e:
        if e:
            print("Please enter valid bid")
            continue

    user_bid["name"] = name
    user_bid["bid"] = bid
    bids.append(user_bid)
    other_bidders = input("Are there any other bidders? Type 'yes or 'no. ").lower()
    print(bids)

    if other_bidders == 'no':
        bidding_over = True
        clear_screen()
        for i, person in enumerate(bids):
            if bids[i]['bid'] > highest_bid:
                highest_bid = bids[i]['bid']
                highest_bidder = bids[i]['name']

    clear_screen()

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
