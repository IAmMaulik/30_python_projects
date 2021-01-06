from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - MS Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
        ("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(f"{os.path.basename(file)} - MS Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")

        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt", filetypes=[
        ("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(f"{os.path.basename(file)} - MS Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("MS Notepad", "This is a replica of the original Notepad by Microsoft, "+
    "but this one is made in Python by Maulik Shah. Pretty Cool right?")

if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - MS Notepad")
    root.wm_iconbitmap('./images/icon.ico')
    root.geometry("644x788")

    TextArea = Text(root, font=("lucida", 13))
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    MenuBar = Menu(root)

    # File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)    
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)

    FileMenu.add_separator()

    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    root.config(menu=MenuBar)

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)

    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # Help Menu Starts
    HelpMemu = Menu(MenuBar, tearoff=0)
    HelpMemu.add_command(label="About MS NotePad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMemu)


    Scroll = Scrollbar(TextArea)    
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)

    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
