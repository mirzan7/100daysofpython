from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

score = 0
no_of_question_asked = 0
quizz = QuizzBrain(question_bank)
while quizz.still_has_questions():
    answer = quizz.next_question()
    if quizz.check_answer(answer):
        score += 1
        no_of_question_asked += 1
        print(f" {score}/{no_of_question_asked}  ")
    else:
         no_of_question_asked += 1
         print(f" {score}/{no_of_question_asked}  ")




