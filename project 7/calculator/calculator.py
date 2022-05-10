from setting import *
import random
from tkinter import *
from main import *

class Board(Canvas):

    def __init__(self):
        super(Board, self).__init__(width = BOARD_SIZE, height = BOARD_SIZE, background = "white")
        self.initDefault()
        self.pack()

    def initDefault(self):
        self.equation = StringVar()
        self.clear()
        self.buildGrid()

    def press(self,num):

        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    def equalPress(self):
        try:
            total = eval(self.expression)
            self.equation.set(total)
            self.expression = ""
        except:
            self.equation.set(" error ")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")

    def buildGrid(self):
        expression_field = Entry(self, textvariable=self.equation)
        expression_field.grid(columnspan=4, ipadx=70)
        button1 = Button(self, text=' 1 ', fg='gray', bg='black',command=lambda: self.press(1), height=1, width=7)
        button1.grid(row=2, column=0)
        button2 = Button(self, text=' 2 ', fg='gray', bg='black',command=lambda: self.press(2), height=1, width=7)
        button2.grid(row=2, column=1)
        button3 = Button(self, text=' 3 ', fg='gray', bg='black',command=lambda: self.press(3), height=1, width=7)
        button3.grid(row=2, column=2)
        button4 = Button(self, text=' 4 ', fg='gray', bg='black',command=lambda: self.press(4), height=1, width=7)
        button4.grid(row=3, column=0)
        button5 = Button(self, text=' 5 ', fg='gray', bg='black',command=lambda: self.press(5), height=1, width=7)
        button5.grid(row=3, column=1)
        button6 = Button(self, text=' 6 ', fg='gray', bg='black',command=lambda: self.press(6), height=1, width=7)
        button6.grid(row=3, column=2)
        button7 = Button(self, text=' 7 ', fg='gray', bg='black',command=lambda: self.press(7), height=1, width=7)
        button7.grid(row=4, column=0)
        button8 = Button(self, text=' 8 ', fg='gray', bg='black',command=lambda: self.press(8), height=1, width=7)
        button8.grid(row=4, column=1)
        button9 = Button(self, text=' 9 ', fg='gray', bg='black',command=lambda: self.press(9), height=1, width=7)
        button9.grid(row=4, column=2)
        button0 = Button(self, text=' 0 ', fg='gray', bg='black',command=lambda: self.press(0), height=1, width=7)
        button0.grid(row=5, column=0)
        plus = Button(self, text=' + ', fg='gray', bg='black',command=lambda: self.press("+"), height=1, width=7)
        plus.grid(row=2, column=3)
        minus = Button(self, text=' - ', fg='gray', bg='black',command=lambda: self.press("-"), height=1, width=7)
        minus.grid(row=3, column=3)
        multiply = Button(self, text=' * ', fg='gray', bg='black',command=lambda: self.press("*"), height=1, width=7)
        multiply.grid(row=4, column=3)
        divide = Button(self, text=' / ', fg='gray', bg='black',command=lambda: self.press("/"), height=1, width=7)
        divide.grid(row=5, column=3)
        equal = Button(self, text=' = ', fg='gray', bg='black',command=lambda: self.equalPress(), height=1, width=7)
        equal.grid(row=5, column=2)
        clear = Button(self, text='Clear', fg='gray', bg='black',command=lambda: self.clear(), height=1, width=7)
        clear.grid(row=5, column='1')
        Decimal = Button(self, text='.', fg='gray', bg='black',command=lambda: self.press('.'), height=1, width=7)
        Decimal.grid(row=6, column=0)