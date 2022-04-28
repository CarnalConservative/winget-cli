#For the Date class:
#Day, month, and year all store integer values.
#The __init__ function should initialize the date to January 1, 2000
#The prompt function should ask for a day, month, and year value.
#The display function should display the date in the format "mm/dd/yyyy"

class Date:
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2000
    
    def prompt(self):
        self.day = int(input("What is the day?\n"))
        self.month = int(input("What is the month?\n"))
        self.year = int(input("What is the year?\n"))

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")