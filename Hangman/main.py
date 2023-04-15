import random
from hangman_art import stages, logo
from hangman_words import word_list

guessed_chars = []
choosen_word = random.choice(word_list)
lives = 6
end_of_the_game = False

print(logo)

display = []
for char in choosen_word:
    display.append("_")


while not end_of_the_game:
    if '_' in display:
        print(display)
        
        guess = input("Guess the letter: ").lower()

        if guess not in display and guess not in guessed_chars:
            guessed_chars.append(guess)
            
            for index, char in enumerate(choosen_word):
                if guess == char:
                    print(f"\nBingo! Letter {guess} is in a word")
                    display[index] = guess
            
            if guess not in choosen_word:
                print(f"\nOOOps, the letter {guess} not in the word")
                lives -= 1
                if lives == 0:
                    print("You loose")
                    end_of_the_game =True
            print(stages[lives])
        else:
            print(f"\nYou have already guessed this letter - {guess}\n_________________________________________")
    else:
        print("You Win!")
        end_of_the_game =True
    