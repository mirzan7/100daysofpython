import tkinter
from tkinter import *


# ------------------------------------------password generator--------------------------------------

# -----------------------------------------save password--------------------------------------------
def add_password_to_file():
    with open("password_manager.txt", 'a') as manager:
        manager.write(f"{website_input.get()}|{username_input.get()}|{password_input.get()}\n")
    website_input.delete(0,END)
    password_input.delete(0,END)


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

generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row=2, sticky=tkinter.W)

add = Button(text="Add", width=50, command=add_password_to_file)
add.grid(columnspan=3)
window.mainloop()
