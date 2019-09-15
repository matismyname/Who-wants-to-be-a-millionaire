from tkinter import *
from PIL import ImageTk
from PIL import Image as PilImage
from tkinter import messagebox
from questions import *
from center_window import center_window


class window_of_app:
    
    def __init__(self, bool_eng, title_of_game, lang_quit_game, lang_start_game, var_menu_language, var_menu_eng, var_menu_deu, var_menu_info_about_game, var_menu_dedication):
        self.window = Tk()
        self.bool_eng = bool_eng #If the game is in english, bool is true
        self.title_of_game = title_of_game
        self.lang_quit_game = lang_quit_game
        self.lang_start_game = lang_start_game
        self.var_menu_language = var_menu_language
        self.var_menu_eng = var_menu_eng
        self.var_menu_deu = var_menu_deu
        self.var_menu_info_about_game = var_menu_info_about_game
        self.var_menu_dedication = var_menu_dedication
        

    def start_app(self):
        cw = center_window(600, 400, self.window)
        cw.center()


        #self.center_window(self, self.window)

        #Add in the title of the game at the top
        self.title_label = Label(self.window, text=self.title_of_game, fg = "white", bg = "black")
        self.title_label.config(width = 200)
        self.title_label.config(font = ("Courier", "20"))
        self.title_label.pack()


        #Add in the buttons
        self.button_quit_game = Button(self.window, text = self.lang_quit_game, fg = "white", bg = "black", command=self.window.destroy)
        self.button_start_game = Button(self.window, text = self.lang_start_game,fg = "white", bg = "black", command=self.start_the_game)

        self.button_quit_game.config(height = 2, width = 10)
        self.button_start_game.config(height = 2, width = 10)

        self.button_quit_game.pack(side = LEFT, padx = 100, pady = 160)
        self.button_start_game.pack(side = LEFT, padx = 100, pady = 160)


        #Add in a menu to change language
        self.menu = Menu(self.window)
        self.window.config(menu = self.menu)

        self.lang_menu = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = self.var_menu_language, menu = self.lang_menu)
        self.lang_menu.add_command(label = self.var_menu_eng, command = self.change_lang_eng)
        self.lang_menu.add_command(label = self.var_menu_deu, command = self.change_lang_ger)

        
        #Add in info about the game
        self.info_menu = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = "Info", menu = self.info_menu)
        self.info_menu.add_command(label = self.var_menu_info_about_game, command = self.info_about_game)
        self.info_menu.add_command(label = self.var_menu_dedication, command = self.dedication)

        self.window.mainloop()
    
    



    def change_lang_eng(self):
        self.window.destroy()
        window_of_app.__init__(self, True, "Who wants to be a millionaire?", "Quit Game", "Start Game", "Language", "English", "German", "Info about the game", "Dedication")
        window_of_app.start_app(self)


    def change_lang_ger(self):
        self.window.destroy()
        window_of_app.__init__(self, False, "Wer wir Millionär?", "Spiel beenden", "Spiel Starten", "Sprache", "Englisch", "Deutsch", "Info über das Spiel", "Widmung")
        window_of_app.start_app(self)
    
    def info_about_game(self):
        if self.bool_eng:
            messagebox.showinfo("Info about the game", "In this game you will be asked 15 questions. " +
             "You must get every question correct to win. " + "There are lifelines as well. Good luck!")
        else:
            messagebox.showinfo("Info über das Spiel", "In diesem Spiel werden dir 15 Fragen gestellt. " +
             "Du musst jede korrekt beantworten, um zu gewinnen! " + "Es gibt auch Joker! Viel Erfolg!")
        

    def dedication(self):
        pass
    

    def start_the_game(self):
        self.window.destroy()
        questions(self.bool_eng)