#Gavin Murdock
#Guess Number
#3-4-22

from tkinter import *
from settings import *
from game import *
class GuessNumber(Frame):
    def __init__(self):
        super(GuessNumber,self).__init__()
        self.master.title(title)
        self.board = Board()
        self.pack()

def main():
    root=Tk()
    x=GuessNumber()
    root.mainloop()
if __name__ == "__main__":
    main()
