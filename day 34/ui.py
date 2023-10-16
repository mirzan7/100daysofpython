from tkinter import *
from quiz_brain import QuizzBrain

BACKGROUND_COLOR = "#b1ddc6"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizzBrain):
        self.point = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.score = Label(self.window, text=f"score = {self.point}", bg=BACKGROUND_COLOR, padx=50, pady=50)
        self.score.grid(row=0, column=1, sticky="e")
        self.canvas = Canvas(width=400, height=263, bg="white")
        self.word = self.canvas.create_text(150, 75, width=300, text="word", font=("Ariel", 16, "italic"))
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=2, column=1)
        self.correct = PhotoImage(file="right.png")
        self.c_button = Button(self.window, image=self.correct, command=self.true, highlightthickness=0, padx=50,
                               pady=50)
        self.c_button.grid(row=3, column=1, sticky="e")
        self.wrong = PhotoImage(file="wrong.png")
        self.w_button = Button(self.window, image=self.wrong, highlightthickness=0, command=self.false, padx=50,
                               pady=50)
        self.w_button.grid(row=3, column=1, sticky="w")
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        print(q_text)
        self.canvas.itemconfig(self.word, text=q_text)

    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.point += 1
            self.update_score()
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def update_score(self):
        self.score.config(text=f"score = {self.point}", bg=BACKGROUND_COLOR, padx=50, pady=50)
