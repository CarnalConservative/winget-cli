while True:
    try:
        a = int(input("Enter a Number: "))
        a=a*2
        print("The result is:", a)
        break
    except ValueError:
        print("The value entered is not valid")