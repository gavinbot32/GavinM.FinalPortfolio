from settings import *
import random
from tkinter import *
from main import *

class Board(Canvas):

    def __init__(self):
        super(Board, self).__init__(width = GAME_SIZE, height = GAME_SIZE, background = "white")
        self.minimum = 1
        self.maximum = 10
        self.initDefault()
        self.pack()

    def assignList(self):
        guess = self.guess_field.get()
        guess = int(guess)
        self.message = ""
        if guess in self.guesses:
            self.message = "Already Guessed!"
        else:
            if guess > self.maximum:
                self.message = "Too Big!"
            elif guess < self.minimum:
                self.message = "Too Small!"
            else:
                self.guesses.append(guess)
                if guess > self.corNumber:
                    self.grGuesses.append(guess)
                elif guess < self.corNumber:
                    self.lsGuesses.append(guess)
                elif guess == self.corNumber:
                    self.message = "Correct!"
                    self.continue_button.place(x=220, y=280)



    def continuecom(self):
        self.continue_button.place_forget()
        self.initDefault()
    def initDefault(self):
        self.corNumber = random.randint(self.minimum,self.maximum)
        self.continue_button = Button(self, text='Continue', fg='gray', bg='black', command=lambda: self.continuecom(),height=1, width=7)
        self.continue_button.place_forget()
        self.entry_field = ""
        self.guesses = []
        self.grGuesses = []
        self.lsGuesses = []
        self.message = ""
        self.build()
    def enter(self):
        try:
            self.assignList()
        except:
            self.message = "Invalid"
        self.entry_field = ""
        self.build()
    def difficulty(self,MIN,MAX):
        self.minimum = MIN
        self.maximum = MAX
        self.initDefault()
    def build(self):
        self.guess_field = Entry(self, textvariable = self.entry_field)
        self.enter_button = Button(self, text='Enter', fg='gray', bg='black',command=lambda: self.enter(), height=1, width=7)
        self.greater_field = Label(self, text=self.grGuesses)
        self.less_field = Label(self, text=self.lsGuesses)
        self.guess_field.place(x=0,y=0,width=500,height=50)
        self.greater_field.place(x=300,y=100,width=200,height=400)
        self.less_field.place(x=0, y=100, width=200,height=400)
        lessSign = Label(self, text="Too Small", font=("Arial Bold",25))
        lessSign.place(x=0,y=70,width=200,height=50)
        greaterSign = Label(self, text="Too Big", font=("Arial Bold", 25))
        greaterSign.place(x=300, y=70, width=200, height=50)
        messageSign = Label(self, text=self.message, font=("Arial Bold", 20))
        messageSign.place(x=150, y=220, width=200, height=50)
        self.enter_button.place(x=220,y=50)
        self.easy_button = Button(self, text='(1-10)', fg="Black", bg='Green', command=lambda: self.difficulty(1,10), height=1,
                                   width=7)
        self.med_button = Button(self, text='(1-50)', fg='black', bg='Yellow', command=lambda: self.difficulty(1,50), height=1,
                                  width=7)
        self.hard_button = Button(self, text='(1-100)', fg='black', bg='Red', command=lambda: self.difficulty(1,100), height=1,
                                  width=7)
        self.easy_button.place(x=220, y=300)
        self.med_button.place(x=220, y=330)
        self.hard_button.place(x=220, y=360)