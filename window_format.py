class game_window:

    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        self.window = window
    
    def center(self):
        self.window_width = self.window.winfo_screenwidth() # width of the screen
        self.window_height = self.window.winfo_screenheight() # height of the screen
        self.x_window_center = (self.window_width/2) - (self.width/2)
        self.y_window_center = (self.window_height/2) - (self.height/2)
        self.window.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x_window_center, self.y_window_center))
    

    def question_of_window(self):
        pass

    def button_adder(self):
        pass