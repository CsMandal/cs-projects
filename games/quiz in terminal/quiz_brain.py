class Quiz:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.q_list = q_list


    def question_remaining(self):
        return self.question_number < len(self.q_list)


    def next_question(self):
        current_question = self.q_list[self.question_number]
        self.question_number += 1
        answer = input(f"{self.question_number} . {current_question.text} ? (True/False)").lower()
        self.check_answer(answer,current_question.answer)

    def check_answer(self,user_answer,answer):
        if user_answer == answer.lower():
            self.score += 1
            print("thats the right answer")
        else:
            print("You are wrong")
            print(f"the correct answer was {answer}")
        print(f"Your current Score is ({self.score}/{self.question_number})")

