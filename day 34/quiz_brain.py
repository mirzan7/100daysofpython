import html


class QuizzBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        q_text = html.unescape(self.current_question.text)
        # answer = input(f"Q.{self.question_number+1}:{q_text} (True/False) ?  ")
        self.question_number += 1
        return f"Q.{self.question_number}:{q_text}"

    def check_answer(self, answer):
        current_question = self.question_list[self.question_number].answer
        if answer.lower() == current_question.lower():
            self.score += 1
            return True
        else:
            return False

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
