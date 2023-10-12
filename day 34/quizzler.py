import requests
from tkinter import *
from question_model import Question
from quiz_brain import QuizzBrain
score = 0
no_of_question_asked = 0


def true():
    global score
    global no_of_question_asked
    if quizz.check_answer("true"):
        score += 1
        no_of_question_asked += 1
        print(f" {score}/{no_of_question_asked}  ")
    else:
        no_of_question_asked += 1
        print(f" {score}/{no_of_question_asked}  ")


def false():
    global score
    global no_of_question_asked
    if quizz.check_answer("false"):
        score += 1
        no_of_question_asked += 1
        print(f" {score}/{no_of_question_asked}  ")
    else:
        no_of_question_asked += 1
        print(f" {score}/{no_of_question_asked}  ")


response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
data = response.json()
questions = data["results"]
# for question_data in questions:
#     question = question_data["question"]
#     print(question)

question_bank = []
for question_data in questions:
    question_text = question_data["question"]
    question_answer = question_data["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quizz = QuizzBrain(question_bank)

window = Tk()
window.title("Quizzler")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
quote_text = canvas.create_text(150, 207, text=quizz.next_question(), width=250)
canvas.grid(row=0, column=0)
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
correct = PhotoImage(file="right.png")
c_button = Button(window, image=correct, command=true, highlightthickness=0)
c_button.grid(row=1, column=0, sticky="e")
wrong = PhotoImage(file="wrong.png")
w_button = Button(window, image=wrong, highlightthickness=0, command=false)
w_button.grid(row=1, column=0, sticky="w")

window.mainloop()

