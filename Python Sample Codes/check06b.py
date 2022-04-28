class Phone:
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0
    def prompt_number(self):
        self.area_code = input("Area Code: ")
        self.prefix = input("Prefix: ")
        self.suffix = input("Suffix: ")
    def display(self):
        print("Phone info:")
        print(f"({self.area_code}){self.prefix}-{self.suffix}")

class Smartphone(Phone):
    def __init__(self):
        super().__init__()
        self.email = ""
    def prompt(self):
        Phone.prompt_number(self)
        self.email = input("Email: ")
    def display(self):
        super().display()
        print(f"{self.email}")


def main():
    call = Phone()
    print("Phone:")
    call.prompt_number()
    print()
    call.display()
    print()
    cell = Smartphone()
    print("Smart phone:")
    cell.prompt()
    print()
    cell.display()
if __name__ == '__main__':
    main()