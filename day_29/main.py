import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ------------------------------------------password generator--------------------------------------


def generate_password():
    password_list = []
    for char in range(9):
        password_list.append(random.choice(letters))
    for char in range(3):
        password_list += random.choice(symbols)
    for char in range(3):
        password_list += random.choice(numbers)
    random.shuffle(password_list)
    generated_password = ""
    for char in password_list:
        generated_password += char
    pyperclip.copy(generated_password)
    password_input.insert(0, generated_password)

# -----------------------------------------save password--------------------------------------------
def add_password_to_file():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("error", "you have missing parameters")
    else:
        with open("password_manager.json", 'w') as manager:
            json.dump(new_data, manager, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)


# ------------------------------------------ui setup------------------------------------------------
window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

website = Label(text="Website: ")
website.grid(column=0, row=0)

website_input = Entry(window, width=40)
website_input.grid(column=1, row=0, columnspan=2)
website_input.focus()

username = Label(text="Email/Username: ")
username.grid(column=0, row=1)

username_input = Entry(window, width=40)
username_input.grid(column=1, row=1, columnspan=2)
username_input.insert(0, "npmirzanmiraj5@gmail.com")

password = Label(text="Password: ")
password.grid(column=0, row=2)

password_input = Entry(window)
password_input.grid(column=1, row=2)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=2, sticky=tkinter.W)

add = Button(text="Add", width=50, command=add_password_to_file)
add.grid(columnspan=3)
window.mainloop()
