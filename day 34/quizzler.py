from ui import QuizzInterface
from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

question_interface = QuizzInterface()
quizz = QuizzBrain(question_bank)
question_string = ""
question_string = quizz.next_question()
print(question_string)
