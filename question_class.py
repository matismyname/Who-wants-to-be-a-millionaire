from tkinter import *
from window_format import game_window
import random


class question_class():

    def __init__(self, bool_eng, question, correct_answer, false_answer1, false_answer2, false_answer3):
        self.window = Tk()
        self.bool_eng = bool_eng
        self.question = question
        self.correct_answer = correct_answer
        self.false_answer1 = false_answer1
        self.false_answer2 = false_answer2
        self.false_answer3 = false_answer3
        self.bottom_frame = Frame(self.window, bg = "red", width = 650, height = 450)
        self.bottom_frame.pack(side = BOTTOM, fill= Y)


    def start(self):
        self.add_question()
        self.buttons()
        cw = game_window(500, 300, self.window)
        cw.center()
        
        
        self.window.mainloop()
    

    #Add the question at the top of the window
    def add_question(self):
        self.title_label = Label(self.window, text=self.question, fg = "white", bg = "black", height = 2)
        self.title_label.config(width = 200)
        self.title_label.config(font = ("Times New Roman", "17"))
        self.title_label.pack()


    def buttons(self):
        self.correct_answer = Button(self.bottom_frame, text = self.correct_answer, fg = "white", bg = "black", command=self.test_destroy)
        self.false_answer1 = Button(self.bottom_frame, text = self.false_answer1,fg = "white", bg = "black", command=self.test_destroy)
        self.false_answer2 = Button(self.bottom_frame, text = self.false_answer3, fg = "white", bg = "black", command=self.test_destroy)
        self.false_answer3 = Button(self.bottom_frame, text = self.false_answer3,fg = "white", bg = "black", command=self.test_destroy)

        self.correct_answer.config(height = 3, width = 15)
        self.false_answer1.config(height = 3, width = 15)
        self.false_answer2.config(height = 3, width = 15)
        self.false_answer3.config(height = 3, width = 15)

        self.randomise_answers()

        self.correct_answer.grid(row = 0, column = 0, padx = 15, pady = 15)
        self.false_answer1.grid(row = 0, column = 1, padx = 15, pady = 15)
        self.false_answer2.grid(row = 1, column = 0, padx = 15, pady = 15)
        self.false_answer3.grid(row = 1, column = 1, padx = 15, pady = 15)


    def randomise_answers(self):
        pass



            

    def test_destroy(self):
        self.window.destroy()