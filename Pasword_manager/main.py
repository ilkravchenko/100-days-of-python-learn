from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()

    if len(website_name) == 0 or len(email_name) == 0 or len(password_name) == 0:
        messagebox.showerror(title='Ooops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f'These are the details entered: \nEmail: {email_name} '
                                                           f'\nPassword: {password_name} \nIs it ok to save?')

        if is_ok:
            with open('passwords.txt', 'a') as file:
                file.write(f"{website_name} | {email_name} | {password_name}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website = Label(text='Website:')
website.grid(column=0, row=1)

email = Label(text='Email/Username:')
email.grid(column=0, row=2)

password = Label(text='Password:')
password.grid(column=0, row=3)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'il.kravcheno115@gmail.com')

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_pass = Button(text='Generate Password', width=14, command=generate_password)
generate_pass.config(padx=0, pady=0)
generate_pass.grid(column=2, row=3)

add_btn = Button(text='Add', width=42, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()