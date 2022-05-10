from tkinter import *

def next_line(file):
    line = file.readline()
    line = line.replace("/","\n")
    return line

class Application(Frame):
    test_file = "exampleText.txt" # replace with test file
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.test = open_file_safe(Application.test_file, "r")
        self.title = read_line_striped(self.test)
        self.category = ""
        self.question = ""
        self.answers = []
        self.correct = ""

    def create_widgets(self):















def main():
    root = Tk()
    app =Application(root)
    root.mainloop()

main()
