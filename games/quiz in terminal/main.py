from question_data import question_data
from question_model import Question
from quiz_brain import Quiz
question_bank=[]
for question in question_data:
    q_text=question['question']
    q_answer=question['correct_answer']
    question=Question(q_text,q_answer)
    question_bank.append(question)

user=Quiz(question_bank)

while user.question_remaining():
    user.next_question()

print(f"the final score is ({user.score}/{user.question_number})")

