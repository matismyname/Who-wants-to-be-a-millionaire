from tkinter import *
from window_format import game_window
from PIL import ImageTk
from PIL import Image as PilImage
import random
import json
from tkinter import messagebox


class question_class():

    def __init__(self, bool_eng):
        self.window = Tk()
        self.window.resizable(False, False)
        self.bool_eng = bool_eng
        self.question = StringVar()
        self.question_counter = 0
        self.counter = 0
        self.question.set("")
        self.correct_answer = ""
        self.false_answer1 =  ""
        self.false_answer2 =  ""
        self.false_answer3 =  ""
        self.set_background()
        self.bottom_frame = Frame(self.window, bg = "#03fc98", width = 650, height = 450)
        self.bottom_frame.pack(side = BOTTOM, fill= Y)


        self.answer_strings = [self.correct_answer,
                                self.false_answer1,
                                self.false_answer2,
                                self.false_answer3]

        self.answers_buttons = [0, 0, 0, 0]

        self.row_nums = [0, 0, 1, 1]
        self.col_nums = [0, 1, 0, 1]


    def set_background(self):
        self.benfra_pic = ImageTk.PhotoImage(PilImage.open("benfra.jpg"))
        self.background_pic = Label(self.window, image=self.benfra_pic)
        self.background_pic.place(x=0, y=0, relwidth=1, relheight=1)


    def start(self):
        self.next_question()
        self.add_question()
        if self.bool_eng:
            cw = game_window(550, 300, self.window)
        else:
            cw = game_window(600, 300, self.window)
        cw.center()
        
        
        self.window.mainloop()
    

    #Add the question at the top of the window
    def add_question(self):
        self.title_label = Label(self.window, textvariable=self.question, fg = "white", bg = "black", height = 2)
        self.title_label.config(width = 200)
        self.title_label.config(font = ("Times New Roman", "17"))
        self.title_label.pack()


    def buttons(self):
        for i in range(len(self.answer_strings)-1):
            self.answers_buttons[i+1] = Button(self.bottom_frame, text = self.answer_strings[i+1], fg = "white", bg = "black", command = self.lost_game)
            self.answers_buttons[i+1].config(height = 3, width = 15)

        self.answers_buttons[0] = Button(self.bottom_frame, text = self.answer_strings[0], fg = "white", bg = "black", command = self.next_question)
        self.answers_buttons[0].config(height = 3, width = 15)
        
        self.randomise_answers()

        for i in range(len(self.answers_buttons)):
            self.answers_buttons[i].grid(row = self.row_nums[i], column = self.col_nums[i], padx = 15, pady = 15)
        

    def randomise_answers(self):
        self.answers_buttons = random.sample(self.answers_buttons, len(self.answers_buttons))
    

    
    def next_question(self):
        if self.bool_eng:
            if self.question_counter < 15:
                with open("questions_eng.json") as f:
                    data = json.load(f)

                for q in data["Questions"]:
                    self.question.set(list(q.keys())[self.counter])
                    self.answer_strings[0] = list(q.values())[self.counter][0]

                for q in data["False Answers"]:
                    self.answer_strings[1] = list(q.values())[self.counter][0]
                    self.answer_strings[2] = list(q.values())[self.counter][1]
                    self.answer_strings[3] = list(q.values())[self.counter][2]

                self.counter += 1
                self.question_counter += 1
                self.buttons()
            else:
                self.winner()

        else:
            if self.question_counter < 15:
                with open("questions_ger.json") as f:
                    data = json.load(f)

                for q in data["Questions"]:
                    self.question.set(list(q.keys())[self.counter])
                    self.answer_strings[0] = list(q.values())[self.counter][0]

                for q in data["False Answers"]:
                    self.answer_strings[1] = list(q.values())[self.counter][0]
                    self.answer_strings[2] = list(q.values())[self.counter][1]
                    self.answer_strings[3] = list(q.values())[self.counter][2]

                self.counter += 1
                self.question_counter += 1
                self.buttons()
            else:
                self.winner()
            

    def lost_game(self):
        if self.bool_eng:
            res = messagebox.askquestion("You lost!", "Unfortunately, that was the wrong answer! You lost the game! Do you want to play again?")
        else:
            res = messagebox.askquestion("Du hast verloren!", "Leider war das die falsche Antwort! Du hast verloren! Möchtest du nochmal spielen?")

        if res == "yes":
            self.title_label.destroy()
            self.question_counter = 0
            self.counter = 0
            self.start()
        else:
            self.window.destroy()
        
    
    def winner(self):
        if self.bool_eng:
            res = messagebox.askquestion("Congratulations!", "Congratulations, you won this game! Do you want to play again?")
        else:
            res = messagebox.askquestion("Glückwunsch!", "Glückwunsch, du hast gewonnen! Möchtest du nochmal spielen?")

        if res == "yes":
            self.title_label.destroy()
            self.question_counter = 0
            self.counter = 0
            self.start()
        else:
            self.window.destroy()