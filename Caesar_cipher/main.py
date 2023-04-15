import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
play_game = True


def caesar(text, shift, direction):
    result = ''

    for letter in text:

        if letter == " " or letter.isdigit():
            result += letter
        else:
            index_of_letter_in_alphabet = alphabet.index(letter)

            if direction == 'encode':
                if index_of_letter_in_alphabet + shift <= 25:
                    result += alphabet[index_of_letter_in_alphabet + shift]
                else:
                    out_of_index_number = index_of_letter_in_alphabet + shift - 25
                    result += alphabet[out_of_index_number-1]
            else:
                result += alphabet[index_of_letter_in_alphabet - shift]
        
    print(f"The {direction}d text is {result}")


print(logo.logo)

while play_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26
    
    caesar(text, shift, direction)

    response = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()

    if response == 'no':
        print("Goodbye")
        play_game = False