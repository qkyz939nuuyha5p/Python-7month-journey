# mini project on Library Book Tracker
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"📚 You borrowed '{self.title}'")
        else:
            print("❌ Book not available")

    def return_book(self):
        self.available = True
        print(f"✅ Returned '{self.title}'")

book1 = Book("Python 101", "John Smith")
book1.borrow()
book1.borrow()
book1.return_book()
