class GPA:
    def __init__(self):
        self.__gpa = 0
    def get_gpa(self):
        return self.__gpa
    def set_gpa(self, value):
        if value < 0 or value > 4:
            self.__gpa = 0
        else:
            self.__gpa = value
    def get_letter(self):
        if 0.0 <= self.__gpa <= 0.99:
            return 'F'
        elif 1.0 <= self.__gpa <= 1.99:
            return 'D'
        elif 2.0 <= self.__gpa <= 2.99:
            return 'C'
        elif 3.0 <= self.__gpa <= 3.99:
            return 'B'
        elif self.__gpa == 4.0:
            return 'A'
    def set_letter(self, letter):
        if letter == 'F':
            self.__gpa = 0.0
        elif letter == 'D':
            self.__gpa = 1.0
        elif letter == 'C':
            self.__gpa = 2.0
        elif letter == 'B':
            self.__gpa = 3.0
        elif letter == 'A':
            self.__gpa = 4.0

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()