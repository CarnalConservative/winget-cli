#Homework
class Student:
    def __init__(self,first_name="",last_name="",id=0): # then creating the init function
        self.first_name = first_name # then initialising the variables and 
        self.last_name = last_name # setting it's initial values 
        self.id = id

def prompt_student(): # then creating the prompt_student function
    student = Student()  # then creating the student object 
    student.first_name = input("Please enter your first name: ") # taking the input from the user 
    student.last_name = input("Please enter your last name: ") # and setting it to variables 
    student.id = int(input("Please enter your id number: "))
    return student # returning the student object 

def display_student(student):  # then in the display function printing the variables 
    print(f"\nYour information:\n{student.id} - {student.first_name} {student.last_name}")

if __name__ == '__main__':  # in the main function calling the methods
    user = prompt_student()
    display_student(user)