from tkinter import *


class QuizzInterface:
    def __init__(self):
        self.point = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50)
        self.score = Label(text=f"score{self.point}")
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=414)
        self.question_text = self.canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
        self.correct = PhotoImage(file="right.png")
        self.c_button = Button(self.window, image=self.correct, command=self.true, highlightthickness=0)
        self.c_button.grid(row=1, column=0, sticky="e")
        self.wrong = PhotoImage(file="wrong.png")
        self.w_button = Button(self.window, image=self.wrong, highlightthickness=0, command=self.false)
        self.w_button.grid(row=1, column=0, sticky="w")
        self.window.mainloop()

    def true(self):
        pass

    def false(self):
        pass
