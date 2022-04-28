from date_class import Date

class Assignment:

    def __init__(self):
        self.name = "Untitled"
        self.start_date = Date()
        self.due_date = Date()
        self.end_date = Date()

    def prompt(self):
        self.name = input('Please enter the Assignment name: ')
        print('Please enter Start date: ')
        self.start_date.prompt()
        print('Please enter Due date: ')
        self.due_date.prompt()
        print('Please enter End date: ')
        self.end_date.prompt()

    def display(self):
        print(str(self.name))
        print('Start date: ')
        self.start_date.display()
        print('Due date: ')
        self.due_date.display()
        print('End date: ')
        self.end_date.display()
