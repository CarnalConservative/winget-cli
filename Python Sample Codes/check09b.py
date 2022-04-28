class NegativeNumberError(Exception): 
    pass

def get_inverse(n): 
    if n==0:
        raise ZeroDivisionError() 
    elif n<0:
        raise NegativeNumberError()
    elif isinstance(n,str) == True:
        raise ValueError()
    else:
        n = float(1/n) 
        return n

      

if __name__=="__main__":   
    try:
        n=float(input("Enter a number: ")) 
        print(f"The result is: {get_inverse(n)}")
    except ValueError: 
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except NegativeNumberError:
        print("Error: The value cannot be negative")