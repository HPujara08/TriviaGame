from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.temp_score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", background= THEME_COLOR, fg="white", font=("Arial", 16))
        self.score.grid(row=1, column=2)

        self.canvas = Canvas(background="white", width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20)

        self.question = self.canvas.create_text(150,
                                                125,
                                                text="Test Question",
                                                font=("Arial", 20),
                                                width=280,
                                                fill=THEME_COLOR
                                                )

        true_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=true_image, background=THEME_COLOR, highlightthickness=0,
                                   command=self.answering_true)
        self.check_button.grid(row=3, column=1)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, background=THEME_COLOR, highlightthickness=0,
                                   command=self.answering_false)
        self.false_button.grid(row=3, column=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answering_true(self):
        answer = True
        self.give_feedback(self.quiz.check_answer(answer))

    def answering_false(self):
        answer = False
        self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
            self.temp_score += 1
            self.score.config(text=f"Score: {self.temp_score}")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
