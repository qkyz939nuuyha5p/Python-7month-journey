#mini project on Book Library System
class Book:
    def __init__(self, title):
        self.title = title
        self.is_issued = False

    def issue(self):
        if not self.is_issued:
            self.is_issued = True
            print(f"The book '{self.title}' has been issued.")
        else:
            print(f"'{self.title}' is already issued.")

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"'{self.title}' wasn't issued.")

# Testing
b1 = Book("Python Programming")
b1.issue()
b1.return_book()
