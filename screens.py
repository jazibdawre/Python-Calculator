from tkinter import *

home = Tk()

#naming frames
basic = Frame(home, bg = 'black')
basic.grid(row = 0, column =0, sticky='news')
scientific = Frame(home, bg = 'black')
scientific.grid(row=0, column=0, sticky='news')

#helping function
def raise_frame(frame):
    frame.tkraise()

home.title("Calculator")
home.iconbitmap('./icon/favicon.ico')