from tkinter import *
import pandas
import random
random_word = {}
data = pandas.read_csv("german_english.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(title, text="GERMAN", fill="black")
    random_word = random.choice(to_learn)
    canvas.itemconfig(word, text=random_word["GERMAN"], fill="black")
    window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(title, text="ENGLISH", fill="white")
    canvas.itemconfig(word, text=random_word["ENGLISH"], fill="white")


def is_known():
    to_learn.remove(random_word)
    next_card()
    print(len(to_learn))

BACKGROUND_COLOR = "#b1ddc6"

window = Tk()
window.title("German flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)
correct = PhotoImage(file="right.png")
c_button = Button(window, image=correct, command=is_known, highlightthickness=0)
c_button.grid(row=1, column=0, sticky="e")
wrong = PhotoImage(file="wrong.png")
w_button = Button(window, image=wrong, highlightthickness=0, command=next_card)
w_button.grid(row=1, column=0, sticky="w")
next_card()
window.mainloop()
