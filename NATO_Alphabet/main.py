import pandas as pd

# while True:
#     user_word = input("Enter a word: ").upper()
#     if user_word.isalpha():
#         break
#     else:
#         print("Sorry, only letters in the alphabet please")
#     # user_word = [letter for letter in user_word]

def generate_phonetic():
    user_word = input("Enter a word: ").upper()

    word_df = pd.read_csv('nato_phonetic_alphabet.csv')

    word_dict = {row.letter:row.code for (index, row) in word_df.iterrows() if row.letter in user_word}

    try:
        letter_list = [word_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(letter_list)

generate_phonetic()
