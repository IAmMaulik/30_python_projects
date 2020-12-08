from tkinter import *

class application(Frame):
    def __init__(self, master):
        super(application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def button_click(self, number):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.display_text = self.answer
            self.task = self.answer

        except:
            self.display_text("Invalid Syntax!")
            self.task = ""
    
    def display_text(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearBoard(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

    def create_widgets(self):
        # Defining the Entry
        self.user_input = Entry(self, bg="#5BC8AC", bd=29,
        insertwidth = 4, width = 24, font = ("Verdana", 20, "bold"),
        textvariable = self.UserIn, justify = RIGHT)

        self.user_input.grid(columnspan=4)
        self.user_input.insert(0, "0")

        # Defining the buttons
        # 7
        self.button1 = Button(self, bg="#98DBC6", bd=12, text='7', padx=33,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click(7))
        self.button1.grid(row=2, column=0, sticky=W)
        
        # 8
        self.button2 = Button(self, bg="#98DBC6", bd=12, text='8', padx=35,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click(8))
        self.button2.grid(row=2, column=1, sticky=W)
        
        # 9
        self.button3 = Button(self, bg="#98DBC6", bd=12, text='9', padx=33,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click(9))
        self.button3.grid(row=2, column=2, sticky=W)
        
        # 4
        self.button4 = Button(self, bg="#98DBC6", bd=12, text='4', padx=33,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click(4))
        self.button4.grid(row=3, column=0, sticky=W)
        
        # 5
        self.button5 = Button(self, bg="#98DBC6", bd=12, text='5', padx=35,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click(5))
        self.button5.grid(row=3, column=1, sticky=W)
        
        # 6
        self.button6 = Button(self, bg="#98DBC6", bd=12, text='6', padx=33,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click(6))
        self.button6.grid(row=3, column=2, sticky=W)

        # 1
        self.button7 = Button(self, bg="#98DBC6", bd=12, text='1', padx=33,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click(1))
        self.button7.grid(row=4, column=0, sticky=W)

        # 2
        self.button8 = Button(self, bg="#98DBC6", bd=12, text='2', padx=35,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click(2))
        self.button8.grid(row=4, column=1, sticky=W)
        
        # 3
        self.button9 = Button(self, bg="#98DBC6", bd=12, text='3', padx=33,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click(3))
        self.button9.grid(row=4, column=2, sticky=W)

        # 0
        self.button0 = Button(self, bg="#98DBC6", bd=12, text='0', padx=33,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click(0))
        self.button0.grid(row=5, column=0, sticky=W)

        # Addition Sign 
        self.AddButton = Button(self, bg="#98DBC6", bd=12, text='+', padx=36,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click("+"))
        self.AddButton.grid(row=2, column=3, sticky=W)

        # Subtraction Sign
        self.SubButton = Button(self, bg="#98DBC6", bd=12, text='-', padx=33,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click("-"))
        self.SubButton.grid(row=3, column=3, sticky=W)

        # Multiplication Sign
        self.MultiButton = Button(self, bg="#98DBC6", bd=12, text='*', padx=39,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click("*"))
        self.MultiButton.grid(row=4, column=2, sticky=W)

        # Division Sign
        self.DiviButton = Button(self, bg="#98DBC6", bd=12, text='/', padx=39,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click("/"))
        self.DiviButton.grid(row=5, column=3, sticky=W)

        # Equal Button
        self.EqualButton = Button(self, bg="#98DBC6", bd=12, text='=', padx=100,
        pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.button_click("="))
        self.EqualButton.grid(row=5, column=1, sticky=W, columnspan=2)

        # Clear Button
        self.ClearButton = Button(self, bg="#98DBC6", bd=12, text='AC',
        font=("Helvetica", 20, "bold"), width=28, padx=7, command=self.ClearBoard)
        self.ClearButton.grid(row=1, columnspan=4, sticky=W)