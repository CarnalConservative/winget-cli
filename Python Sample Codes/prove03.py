odd = []
even = []

start = int(input("Enter a number (0 to quit): "))
while start != 0:
    if start % 2:
        odd.append(start)
    else:
        even.append(start)
    start = int(input("Enter a number (0 to quit): "))

if start == 0:
    print("\nEven Numbers:")
    for i in even:
        print(f"{i}")
    print("\nOdd Numbers:")
    for i in odd:
        print(f"{i}")