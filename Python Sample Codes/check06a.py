class Book:
   def __init__(self):
       self.title = ""
       self.author = ""
       self.publication_year = 0

   def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: \n"))
   def display_book_info(self):
        print(f"{self.title} ({self.publication_year}) by {self.author}")

class Textbook(Book):
    def __init__(self):
        super().__init__()
        self.subject = ""
    def prompt_subject(self):
        self.subject = input("Subject: ")
    def display_subject(self):
        print(f"Subject: {self.subject}")

class PictureBook(Book):
    def __init__(self):
        super().__init__()
        self.illustrator = ""
    def prompt_illustrator(self):
        self.illustrator = input("Illuatrator: ")
    def display_illustrator(self):
        print(f"Illustrator: {self.illustrator}")

def main():
    novel = Book()
    novel.prompt_book_info()
    novel.display_book_info()

    textBook = Textbook()
    textBook.prompt_book_info()
    textBook.prompt_subject()
    textBook.display_book_info()
    textBook.display_subject()

    pictureBook = PictureBook()
    pictureBook.prompt_book_info()
    pictureBook.prompt_illustrator()
    pictureBook.display_book_info()
    pictureBook.display_illustrator()
if __name__ == '__main__':
    main()