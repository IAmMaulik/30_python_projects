from tkinter import *

class application(Frame):
    def __init__(self, master):
        super(self, application).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Defining the Entry
        self.user_input = Entry(self, bg="#5BC8AC", bd=29,
        insertwidth = 4, width = 24, font = ("Verdana", 20, "bold"),
        textvariable = self.UserIn, justify = RIGHT)

        self.user_input.grid(columnspan=4)
        self.user_input.insert(0, "0")

        # Defining the buttons

        # 1
        self.button1 = Button(self, bg="#98DBC6", bd=12, text='1', padx=33,
        pady=25, font=("Belvetics", 20, "bold"), command=lambda : self.button_click(1))
        self.button1.grid(row=0, column=0, sticky=NW)

        # 2
        self.button2 = Button(self, bg="#98DBC6", bd=12, text='2', padx=33,
        pady=25, font=("Belvetics", 20, "bold"), command=lambda : self.button_click(2))
        self.button2.grid(row=0, column=1, sticky=N)
        
        # 3
        self.button3 = Button(self, bg="#98DBC6", bd=12, text='3', padx=33,
        pady=25, font=("Belvetics", 20, "bold"), command=lambda : self.button_click(3))
        self.button3.grid(row=2, column=0, sticky=NE)
        
        # 4
        self.button4 = Button(self, bg="#98DBC6", bd=12, text='4', padx=33,
        pady=25, font=("Belvetics", 20, "bold"), command=lambda : self.button_click(4))
        self.button4.grid(row=1, column=0, sticky=W)
        
        # 5
        self.button5 = Button(self, bg="#98DBC6", bd=12, text='5', padx=33,
        pady=25, font=("Belvetics", 20, "bold"), command=lambda : self.button_click(7))
        self.button5.grid(row=1, column=1, sticky=NSEW)
        
        # 6
        self.button6 = Button(self, bg="#98DBC6", bd=12, text='6', padx=33,
        pady=25, font=("Belvetics", 20, "bold"), command=lambda : self.button_click(6))
        self.button6.grid(row=1, column=2, sticky=E)
        
        # 7
        self.button7 = Button(self, bg="#98DBC6", bd=12, text='7', padx=33,
        pady=25, font=("Belvetics", 20, "bold"), command=lambda : self.button_click(7))
        self.button7.grid(row=2, column=0, sticky=SW)
        
        # 8
        self.button8 = Button(self, bg="#98DBC6", bd=12, text='8', padx=33,
        pady=25, font=("Belvetics", 20, "bold"), command=lambda : self.button_click(8))
        self.button8.grid(row=2, column=1, sticky=S)
        
        # 9
        self.button9 = Button(self, bg="#98DBC6", bd=12, text='9', padx=33,
        pady=25, font=("Belvetics", 20, "bold"), command=lambda : self.button_click(9))
        self.button4.grid(row=2, column=2, sticky=SE)

        # 0
        self.button0 = Button(self, bg="#98DBC6", bd=12, text='0', padx=33,
        pady=25, font=("Belvetics", 20, "bold"), command=lambda : self.button_click(0))
        self.button0.grid(row=3, column=0, sticky=W)