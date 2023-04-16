from os import system
from art import logo
import random

play = True

############### Blackjack Project #####################

#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def deal_first_two_cards():
    cards = []
    for i in range(2):
        cards.append(deal_card())

    return cards

def calculate_score(list_of_cards):
    return int(sum(list_of_cards))

def check_for_results():
    if player_lose:
        print("You went over. You lose!")
    elif comp_lose:
        print("Opponent went over. You win!")
    elif calculate_score(computer_cards) > calculate_score(player_cards):
        print("You lose!")
    elif calculate_score(computer_cards) == calculate_score(player_cards):
        print("Draw!")
    else:
        print("You win!")

def change_ace(cards):
    if 11 in cards and calculate_score(cards) > 21:
        index_of_ace = cards.index(11)
        cards[index_of_ace] = 1

    return cards

def add_card():
    global player_lose
    global comp_lose
    global player_cards
    global computer_cards

    while input("Type 'y' to get another card, or 'n' to pass: ") == "y":
        player_cards.append(deal_card())

        player_cards = change_ace(player_cards)

        print(f"\tYour final hand: {player_cards}, final score: {calculate_score(player_cards)}")
        print(f"\tComputer first card: {computer_cards[0]}")

        if calculate_score(player_cards) >= 22:
            player_lose = True
            return
    else:
        print(f"\tYour final hand: {player_cards}, final score: {calculate_score(player_cards)}")
        while int(sum(computer_cards)) < 17:
            computer_cards.append(deal_card())
        
        computer_cards = change_ace(computer_cards)

        print(f"\tComputer final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")

        if calculate_score(computer_cards) >= 22:
            comp_lose = True
            return

def check_for_black_jack(player_cards, computer_cards):
    global user_black_jack
    global comp_black_Jack
    if calculate_score(player_cards) == 21:
        print("You have Black Jack. Congratulation")
        user_black_jack = True
    elif calculate_score(computer_cards) == 21:
        print("Computer have Black Jack. Congratulation")
        comp_black_Jack = True

while play:
    start_play = input("Do you want play in BlackJack? 'y' for yes and 'n' or no.: ")
    if start_play == "y":
        play = True
        system('cls')
    else:
        play = False
        break

    comp_lose = None
    player_lose = None
    user_black_jack = None
    comp_black_Jack = None

    print(logo)

    player_cards = deal_first_two_cards()
    computer_cards = deal_first_two_cards()

    print(f"\tYour cards: {player_cards}, current score: {calculate_score(player_cards)}")
    print(f"\tComputer first card: {computer_cards[0]}")

    check_for_black_jack(player_cards, computer_cards)
    if user_black_jack == True and comp_black_Jack == True:
        print("Two players has Black Jack!")
        break
    elif user_black_jack == True:
        print("User win!")
        break
    elif comp_black_Jack == True:
        print("Dealler win!")
        break
    add_card()
    check_for_results()

print("Thank you for playing! Have a nice day!")