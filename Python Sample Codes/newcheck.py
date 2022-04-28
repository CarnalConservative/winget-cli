#Homework
class Complex:
    # Setting real and imaginary values to zero initially
    def __init__(self):
        self.real = 0
        self.imaginary = 0
  
    # Prompting the user for the values of real and imaginary
    def prompt(self):
        self.real = int(input("\nPlease enter the real part: "))
        self.imaginary = int(input("Please enter the imaginary part: "))
  
    # Diplaying the complex number in the form x + yi
    def display(self):
        print(str(self.real) + " + " + str(self.imaginary) + "i")
  
  
# Main Function
if __name__ == "__main__":
    # Creating the two complex numbers as complex1 and complex2
    complex1 = Complex()
    complex2 = Complex()
  
    #Printing their initial values
    print("The values are:")
    complex1.display()
    complex2.display()
    
  
    # Prompting the user for new values for complex1 and complex2
    complex1.prompt()
    complex2.prompt()
  
    # Printing the new values
    print("\nThe values are:")
    complex1.display()
    complex2.display()
