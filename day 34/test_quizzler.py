import tkinter as tk
import random
import requests


class QuizApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a label to display the question
        self.question_label = tk.Label(self, text="Question")
        self.question_label.pack()

        # Create two buttons for the user to answer true or false
        self.true_button = tk.Button(self, text="True", command=self.answer_true)
        self.true_button.pack()

        self.false_button = tk.Button(self, text="False", command=self.answer_false)
        self.false_button.pack()

        # Get a random question from the Open Trivia Database
        self.get_question()

    def get_question(self):
        # Make an API request to the Open Trivia Database
        response = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")

        # Get the question from the response
        question = response.json()["results"][0]["question"]

        # Set the question label to the new question
        self.question_label.config(text=question)

    def answer_true(self):
        # Check if the user's answer is correct
        answer = self.question_label.cget("text")
        correct_answer = \
        requests.get(f"https://opentdb.com/api.php?amount=1&type=boolean&query={answer}").json()["results"][0][
            "correct_answer"]

        # Display a message to the user indicating whether their answer was correct
        if answer == correct_answer:
            tk.messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            tk.messagebox.showerror("Incorrect", "Your answer is incorrect.")

        # Get a new question
        self.get_question()

    def answer_false(self):
        # Check if the user's answer is correct
        answer = self.question_label.cget("text")
        correct_answer = \
        requests.get(f"https://opentdb.com/api.php?amount=1&type=boolean&query={answer}").json()["results"][0][
            "correct_answer"]

        # Display a message to the user indicating whether their answer was correct
        if answer != correct_answer:
            tk.messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            tk.messagebox.showerror("Incorrect", "Your answer is incorrect.")

        # Get a new question
        self.get_question()


if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizApp(root)
    quiz_app.pack()
    root.mainloop()
