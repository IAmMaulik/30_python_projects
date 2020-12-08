from tkinter import *

class application(Frame):
    def __init__(self, master):
        super(self, application).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()
