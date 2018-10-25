from tkinter import *
from models import model
import threading


class View:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Start", command=self.start)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=master.destroy)
        self.quitButton.pack(side=LEFT)

    def start(self):
        m = model.Model()
        m.process_website()


root = Tk()
b = View(root)
root = mainloop()