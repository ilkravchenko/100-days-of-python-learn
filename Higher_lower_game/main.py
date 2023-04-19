import random
from art import logo, vs
from game_data import data
from os import system


def choose_compared() -> dict:
    compared = random.choice(data)
    return compared

def print_compared(compared:dict) -> str:
    return f"{compared['name']}, a {compared['description']}, from {compared['country']}"

def play():
    continue_play = True
    score = 0

    first_compared = choose_compared()
    second_compared = choose_compared()
    
    while continue_play:
        system('cls')
        print(logo)
        if score >= 1:
            print(f"You are right! Current score: {score}.")

        print(f"Compare A: " + print_compared(first_compared))
        print(vs)
        print(f"Against B: " + print_compared(second_compared))

        player_turn = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        right_answer = "A" if first_compared["follower_count"] > second_compared["follower_count"] else "B"

        if player_turn == right_answer:
            score += 1

            first_compared = second_compared
            second_compared = choose_compared()
        else:
            system('cls')
            continue_play = False
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")


def main():
    play()

if __name__ == "__main__":
    main()