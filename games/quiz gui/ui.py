from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class GraphicalInterface:
    def __init__(self, quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(pady=30, padx=40, bg=THEME_COLOR)
        self.user_answer = 'false'
        self.score = 0

        self.score_label = Label(text="Score :", fg='white', bg=THEME_COLOR,font=('arial',20,'italic'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question = self.canvas.create_text(150, 125, text='hello', font=('arial',20,'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_image = PhotoImage(file='./images/true.png')
        self.right_button = Button(image=self.right_image, command=self.right)
        self.right_button.grid(row=2, column=0, padx=30)

        self.cross_image = PhotoImage(file='./images/false.png')
        self.cross_button = Button(image=self.cross_image, command=self.wrong)
        self.cross_button.grid(row=2, column=1, padx=30)
        self.next_question()

        self.window.mainloop()

    def right(self):
        self.user_answer = 'true'
        self.next_question()

    def wrong(self):
        self.user_answer = 'false'
        self.next_question()

    def next_question(self):
        q_text, q_num = self.quiz.next_question()
        self.canvas.itemconfig(self.question , text=f"{q_num}. {q_text}", width=280)
        q_ans = self.quiz.check_answer()
        u_ans = self.user_answer
        if q_ans.lower() == u_ans:
            self.score += 1

        self.score_label.config(text=f"{self.score} / {q_num}")












