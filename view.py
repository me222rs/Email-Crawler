# from tkinter import *
from models import model
import threading


class View:
    def __init__(self):
        self.main()

    def main(self):
        self.showMainMenu()
        option = input()

        if option == "1":
            url = self.chooseURL()
            self.start(url)
        elif option == "2":
            exit(0)

    def chooseURL(self):
        url = input()
        return url

    def start(self, url):
        m = model.Model()
        m.process_website(url)

    def showMainMenu(self):
        print("----- Email Crawler -----")
        print("Press 1 to start")
        print("Press 2 to exit")


b = View()
