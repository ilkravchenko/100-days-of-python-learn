from os import system
from art import logo
import random

play = True

############### Blackjack Project #####################

#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_for_results():
    if player_lose:
        print("You went over. You lose!")
    elif comp_lose:
        print("Opponent went over. You win!")
    elif int(sum(computer_cards)) > int(sum(player_cards)):
        print("You lose!")
    elif int(sum(computer_cards)) == int(sum(player_cards)):
        print("Draw!")
    else:
        print("You win!")

def change_ace(cards):
    if 11 in cards and int(sum(cards)) > 21:
        index_of_ace = cards.index(11)
        cards[index_of_ace] = 1

    return cards

def add_card():
    global player_lose
    global comp_lose
    global player_cards
    global computer_cards

    while input("Type 'y' to get another card, or 'n' to pass: ") == "y":
        player_cards.append(random.choice(cards))

        player_cards = change_ace(player_cards)

        print(f"\tYour final hand: {player_cards}, final score: {int(sum(player_cards))}")
        print(f"\tComputer first card: {computer_cards[0]}")

        if int(sum(player_cards)) >= 22:
            player_lose = True
            return
    else:
        print(f"\tYour final hand: {player_cards}, final score: {int(sum(player_cards))}")
        while int(sum(computer_cards)) < 17:
            computer_cards.append(random.choice(cards))
        
        computer_cards = change_ace(computer_cards)

        print(f"\tComputer final hand: {computer_cards}, final score: {int(sum(computer_cards))}")

        if int(sum(computer_cards)) >= 22:
            comp_lose = True
            return


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

    print(logo)

    player_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)

    print(f"\tYour cards: {player_cards}, current score: {int(sum(player_cards))}")
    print(f"\tComputer first card: {computer_cards[0]}")

    if int(sum(player_cards)) == 21:
        print("You have Black Jack. Congratulation")

    add_card()
    check_for_results()

print("Thank you for playing! Have a nice day!")