from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


# ------------------- Show Translate ----------------------- #
def show_translate():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(canvas_lang, text='Ukrainian', fill='white')
    canvas.itemconfig(canvas_word, text=current_card['Ukrainian'], fill='white')


# ------------------- Working with words ---------------------- #
try:
    data = pd.read_csv('./data/words_to_learn.csv')
except:
    data = pd.read_csv('./data/Words.csv')
dict_of_words = data.to_dict(orient='records')
current_card = {}


def delete_word():
    dict_of_words.remove(current_card)


def save_words():
    data = pd.DataFrame(dict_of_words)
    data.to_csv(path_or_buf="./data/words_to_learn.csv", index=False)


def generate_english_word():
    global current_card
    current_card = random.choice(dict_of_words)
    english_word = current_card['English']

    return english_word


def change_word():
    global flip_timer
    window.after_cancel(flip_timer)
    new_word = generate_english_word()
    canvas.itemconfig(canvas_word, text=new_word, fill='black')
    canvas.itemconfig(canvas_lang, text='English', fill='black')
    canvas.itemconfig(canvas_image, image=card_front_img)

    flip_timer = window.after(3000, show_translate)


# ------------------- User Interface ------------------ #
window = Tk()
window.title('Flashy Learn')
window.config(width=800, height=526, pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, show_translate)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR)
canvas_lang = canvas.create_text(400, 150, text='English', font=('Arial', 40, 'italic'))
canvas_word = canvas.create_text(400, 263, text=generate_english_word(), font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file='./images/wrong.png')
wrong_btn = Button(image=wrong_img, width=100, height=100, highlightthickness=0, command=change_word)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file='./images/right.png')
right_btn = Button(image=right_img, width=100, height=100, highlightthickness=0,
                   command=lambda: [change_word(), delete_word()])
right_btn.grid(column=1, row=1)

window.mainloop()

save_words()
