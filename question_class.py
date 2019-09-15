from tkinter import *
from center_window import center_window


class question_class():

    def __init__(self, bool_eng, question, correct_answer, false_answer1, false_answer2, false_answer3):
        self.bool_eng = bool_eng
        self.question = question
        self.correct_answer = correct_answer
        self.false_answer1 = false_answer1
        self.false_answer2 = false_answer2
        self.false_answer3 = false_answer3

        self.window = Tk()

    def start(self):
        self.title_label = Label(self.window, text=self.question, fg = "white", bg = "black")
        self.title_label.config(width = 200)
        self.title_label.config(font = ("Times New Roman", "17"))
        self.title_label.pack()
        cw = center_window(600, 400, self.window)
        cw.center()

        self.buttons()


        self.window.mainloop()
    

    def buttons(self):
        self.correct_answer = Button(self.window, text = self.correct_answer, fg = "white", bg = "black", command=self.test_destroy)
        self.false_answer1 = Button(self.window, text = self.false_answer1,fg = "white", bg = "black", command=self.test_destroy)
        self.false_answer2 = Button(self.window, text = self.false_answer3, fg = "white", bg = "black", command=self.test_destroy)
        self.false_answer3 = Button(self.window, text = self.false_answer3,fg = "white", bg = "black", command=self.test_destroy)

        self.correct_answer.config(height = 2, width = 10)
        self.false_answer1.config(height = 2, width = 10)
        self.false_answer2.config(height = 2, width = 10)
        self.false_answer3.config(height = 2, width = 10)

        #self.correct_answer.grid(row = 0, column = 0)
        #self.correct_answer.grid(row = 0, column = 1)
        #self.correct_answer.grid(row = 1, column = 0)
        #self.correct_answer.grid(row = 1, column = 1)


        self.correct_answer.pack(side = LEFT, padx = 10, pady = 10)
        self.false_answer1.pack(side = LEFT, padx = 10, pady = 10)
        self.false_answer2.pack(side = LEFT, padx = 10, pady = 10)
        self.false_answer3.pack(side = LEFT, padx = 10, pady = 10)

    def test_destroy(self):
        self.window.destroy()