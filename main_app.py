from window_of_app import *

title_of_game = "Who wants to be a millionaire?"
bool_eng = True
lang_quit_game = "Quit Game"
lang_start_game = "Start Game"
var_menu_language = "Language"
var_menu_eng = "English"
var_menu_deu = "German"
var_menu_info_about_game = "Info about the game"
var_menu_dedication = "Dedication"


def main():
    app = window_of_app(bool_eng, title_of_game, lang_quit_game, lang_start_game, var_menu_language, var_menu_eng, var_menu_deu, var_menu_info_about_game, var_menu_dedication)
    app.start_app()



if __name__ == main():
    main()