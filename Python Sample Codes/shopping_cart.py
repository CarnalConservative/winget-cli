items = []
prices = []

item = None
price = 0

print("Welcome to the Shopping Cart Program! ")
start = input("Please select one of the following:\n1. Add Item\n2. View Cart\n3. Remove Item\n4. Compute Total\n5. Quit\nPlease Enter Action: ")
while start != "5":
    if start == "1":
        new_item = input("What item would you like to add? ")
        new_price = input("What is the price of " + new_item + "? ")
        items.append(new_item)
        prices.append(new_price)
        print(new_item + " has been added to the cart.")
        new_item = None
        new_price = 0
        start = input("Please select one of the following:\n1. Add Item\n2. View Cart\n3. Remove Item\n4. Compute Total\n5. Quit\nPlease Enter Action: ")
        
#if start == "2":
    #print("\nThe contents of the shopping cart are:")
    #for (item, price) in (items, prices):
        #print("{item} - {price}")
    #start = input("Please select one of the following:\n1. Add Item\n2. View Cart\n3. Remove Item\n4. Compute Total\n5. Quit\nPlease Enter Action: ")
    
if start == "3":
    remove = input("Which item would you like to remove? ")
for remove in range(len(items)):
    items.pop(items[remove] + "-" + "$" + prices[remove])
start = input("Please select one of the following:\n1. Add Item\n2. View Cart\n3. Remove Item\n4. Compute Total\n5. Quit\nPlease Enter Action: ")