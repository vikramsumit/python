class LibrarySystem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Library item information")

class Book(LibrarySystem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_info(self):
        print("Book Information:")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)

class Magazine(LibrarySystem):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def display_info(self):
        print("Magazine Information:")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Issue Number:", self.issue_number)

book1 = Book("JUNGLE BOOK", "Rudyard kipling", 250)
book2 = Book("AI ENGINEERING", "CANES", 550)
mag1 = Magazine("FORBES LIST", "FOrbes group", 45)

book1.display_info()
book2.display_info()
print()
mag1.display_info()
