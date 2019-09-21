from tkinter import *
from PIL import ImageTk
from PIL import Image as PilImage
from tkinter import messagebox
from window_format import game_window
from question_class import question_class
import json


class window_of_app:
    
    def __init__(self,
    bool_eng,
    title_of_game,
    height_of_window,
    width_of_window,
    lang_quit_game,
    lang_start_game,
    var_menu_language,
    var_menu_eng,
    var_menu_deu,
    var_menu_info_about_game):
        self.window = Tk()
        self.window.resizable(False, False)
        self.bool_eng = bool_eng #If the game is in english, bool is true
        self.title_of_game = title_of_game
        self.height_of_window = height_of_window
        self.width_of_window = width_of_window
        self.lang_quit_game = lang_quit_game
        self.lang_start_game = lang_start_game
        self.var_menu_language = var_menu_language
        self.var_menu_eng = var_menu_eng
        self.var_menu_deu = var_menu_deu
        self.var_menu_info_about_game = var_menu_info_about_game


        self.money_pic = ImageTk.PhotoImage(PilImage.open("money_pic.jpg"))
        self.background_pic = Label(self.window, image=self.money_pic)
        self.background_pic.place(x=0, y=0, relwidth=1, relheight=1)
        

    def start_app(self):
        #Center the window
        cw = game_window(self.height_of_window, self.width_of_window, self.window)
        cw.center()
        self.add_title()
        self.add_buttons()
        self.change_lang_menu()
        self.add_info_to_game()

    
    
    #Add in the title of the game at the top
    def add_title(self):
        self.title_label = Label(self.window, text=self.title_of_game, fg = "white", bg = "black")
        self.title_label.config(width = 200)
        self.title_label.config(font = ("Courier", "20"))
        self.title_label.pack()

    
    #Add in the buttons
    def add_buttons(self):
        self.button_quit_game = Button(self.window, text = self.lang_quit_game, fg = "white", bg = "black", command=self.window.destroy)
        self.button_start_game = Button(self.window, text = self.lang_start_game,fg = "white", bg = "black", command=self.start_the_game)

        self.button_quit_game.config(height = 2, width = 10)
        self.button_start_game.config(height = 2, width = 10)

        self.button_quit_game.pack(side = LEFT, padx = 100, pady = 160)
        self.button_start_game.pack(side = LEFT, padx = 100, pady = 160)

    
    #Add in a menu to change language
    def change_lang_menu(self):
        self.menu = Menu(self.window)
        self.window.config(menu = self.menu)
        self.lang_menu = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = self.var_menu_language, menu = self.lang_menu)
        self.lang_menu.add_command(label = self.var_menu_eng, command = self.change_lang_eng)
        self.lang_menu.add_command(label = self.var_menu_deu, command = self.change_lang_ger)


    #Add in info about the game
    def add_info_to_game(self):
        self.info_menu = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = "Info", menu = self.info_menu)
        self.info_menu.add_command(label = self.var_menu_info_about_game, command = self.info_about_game)

        self.window.mainloop()

    def change_lang_eng(self):
        self.window.destroy()
        window_of_app.__init__(self,
        True,
        "Who wants to be a millionaire?",
        "Quit Game",
        "Start Game",
        "Language",
        "English",
        "German",
        "Info about the game")
        window_of_app.start_app(self)


    def change_lang_ger(self):
        self.window.destroy()
        window_of_app.__init__(self,
        False,
        "Wer wir Millionär?",
        600,
        400,
        "Spiel beenden",
        "Spiel Starten",
        "Sprache",
        "Englisch",
        "Deutsch",
        "Info über das Spiel")
        window_of_app.start_app(self)
    
    def info_about_game(self):
        if self.bool_eng:
            messagebox.showinfo("Info about the game", "In this game you will be asked 15 questions. " +
             "You must get every question correct to win. " + "Good luck!")
        else:
            messagebox.showinfo("Info über das Spiel", "In diesem Spiel werden dir 15 Fragen gestellt. " +
             "Du musst jede korrekt beantworten, um zu gewinnen! " + "Viel Erfolg!")
        
    

    def start_the_game(self):
        self.window.destroy()
        question_class(self.bool_eng).start()