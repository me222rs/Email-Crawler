from models import model, Util
import threading


class View:
    def __init__(self):
        self.main()

    def main(self):
        self.showMainMenu()
        option = input()

        if option == "1":
            print("Type the url you want to crawl.")
            url = self.chooseURL()
            print("Use image recognition in order to find emails on images? This option is slower, but a must on sites "
                  "with emails embedded in pictures.")
            print("--- Yes or No ---")
            image_recognition = input()
            self.start(url, image_recognition)
        elif option == "2":
            exit(0)
        elif option == "3":
            print("Type the url you want to resume.")
            url = self.chooseURL()
            print("Are you sure you want to resume the task?")
            print("--- Yes or No ---")
            resume_task = input()
            print("Use image recognition in order to find emails on images? This option is slower, but a must on sites "
                  "with emails embedded in pictures.")
            print("--- Yes or No ---")
            image_recognition = input()
            self.resume(url, image_recognition)
        elif option == "4":
            self.experimental()

    def experimental(self):
        m = Util.Util()
        m.run()

    def chooseURL(self):
        url = input()
        return url

    def start(self, url, image_recognition):
        m = model.Model()
        m.process_website(url, False, image_recognition)

    def resume(self, url, image_recognition):
        m = model.Model()
        m.process_website(url, True, image_recognition)

    def showMainMenu(self):
        print("---- Email Crawler ----")
        print("# Press 1 to start Email Crawler")
        print("# Press 2 to exit")
        print("# Press 3 to resume")
        print("# Press 4 to Experimental stuff")

    def settings(self):
        m = settings.Settings()
        print("---- Settings ----")
        print("1. Retry timer: ")
        print("2. Randomize user agent")
        print("3. Max and Min timer")


b = View()

