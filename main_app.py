from start_window import window_of_app
import os

title_of_game = "Who wants to be a millionaire?"
height_of_window = 600
width_of_window = 400
bool_eng = True
lang_quit_game = "Quit Game"
lang_start_game = "Start Game"
var_menu_language = "Language"
var_menu_eng = "English"
var_menu_deu = "German"
var_menu_info_about_game = "Info about the game"
os.chdir("Change/to/where/the/code/is/and/the/pictures")


def main():
    app = window_of_app(bool_eng,
    title_of_game,
    height_of_window,
    width_of_window,
    lang_quit_game,
    lang_start_game,
    var_menu_language,
    var_menu_eng,
    var_menu_deu,
    var_menu_info_about_game)
    app.start_app()


if __name__ == main():
    main()
