#homework
class Person:
  
   def __init__(self):
       self.name = "anonymous"
       self.byear = "unknown"
  
   def display(self):
       print (self.name + " (b. " + self.byear + ")")

class Book:
  
   def __init__(self):
       self.title = "untitled"
       self.author = Person()
       self.publisher = "unpublished"
  
   def display(self):
       print (self.title + "\n" + "Publisher:" + "\n" + self.publisher + "\n" + "Author:")
       self.author.display()


#This would create first object of Person class
book1 = Book()
book1.display()

print ("\nPlease enter the following:")
book1.author.name = input("Name: ")
book1.author.byear = input("Year: ")
book1.title = input("Title: ")
book1.publisher = input("Publisher: ")
print()
print(book1.title + "\n" + "Publisher:\n" + book1.publisher + "\n" + "Author:\n" + book1.author.name + " (b. " + book1.author.byear + ")")