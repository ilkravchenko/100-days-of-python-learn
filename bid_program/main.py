from art import logo
from os import system

bid_dict = {}
play = True

print(logo)
print("Welcome to the secret auction program.")


def find_highest_bidder(biding_records):
    winner_key = ''
    max_bid = 0

    for key, value in bid_dict.items():
        if value > max_bid:
            winner_key = key
            max_bid = value

    print(f"The winner is {winner_key} with a bid of ${bid_dict[winner_key]}.")


while play:
    name = input("What is your name?: ").capitalize()
    bid = int(input("What is your bid? $"))

    bid_dict[name] = bid

    more_bids = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

    if more_bids == 'yes':
        system('cls')
    else: 
        find_highest_bidder(bid_dict)
        play = False
