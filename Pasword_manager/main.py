from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

    new_data = {
        website_name: {
            'email': email_name,
            'password': password_name
        }
    }

    if len(website_name) == 0 or len(email_name) == 0 or len(password_name) == 0:
        messagebox.showerror(title='Ooops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('passwords.json', 'r') as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open('passwords.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # update old data
            data.update(new_data)

            with open('passwords.json', 'w') as file:
                # saving updating data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH FUNCTIONALITY ------------------- #
def find_password():
    website_name = website_entry.get()
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
        try:
            website_email = data[website_name]['email']
            website_password = data[website_name]['password']
        except KeyError:
            messagebox.showerror(title='Ooops', message='No details for the website exists')
        else:
            messagebox.showinfo(title=website_name, message=f'Email: {website_email}\n'
                                                            f'Password: {website_password}')
    except FileNotFoundError:
        messagebox.showerror(title='File not Found', message='You haven\'t any passwords yet')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
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

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'il.kravcheno115@gmail.com')

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

search_btn = Button(text='Search', width=14, command=find_password)
search_btn.config(padx=0, pady=0)
search_btn.grid(column=2, row=1)

generate_pass = Button(text='Generate Password', width=14, command=generate_password)
generate_pass.config(padx=0, pady=0)
generate_pass.grid(column=2, row=3)

add_btn = Button(text='Add', width=42, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
