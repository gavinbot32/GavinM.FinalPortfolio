#Gavin Murdock
#Calculator
#3-4-22

from tkinter import *
from setting import *
from calculator import *
class Calculator(Frame):
    def __init__(self):
        super(Calculator,self).__init__()
        self.master.title(title)
        self.board = Board()
        self.pack()

def main():
    root=Tk()
    x=Calculator()
    root.mainloop()
if __name__ == "__main__":
    main()
