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
        elif option == "3":
            url = self.chooseURL()
            self.resume(url)
        elif option == "4":
            self.settings()

    def chooseURL(self):
        url = input()
        return url

    def start(self, url):
        m = model.Model()
        m.process_website(url, False)

    def resume(self, url):
        m = model.Model()
        m.process_website(url, True)

    def showMainMenu(self):
        print("---- Email Crawler ----")
        print("# Press 1 to start")
        print("# Press 2 to exit")
        print("# Press 3 to resume")
        print("# Press 4 to change settings")

    def settings(self):
        m = settings.Settings()
        print("---- Settings ----")
        print("1. Retry timer: ")
        print("2. Randomize user agent")
        print("3. Max and Min timer")


b = View()

