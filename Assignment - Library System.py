# ── BOOK CLASS ─────────────────────────────────────────────────
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == True:
            print("This book is already borrowed. Sorry!")
        else:
            self.is_borrowed = True
            print(f"You have successfully borrowed {self.title} by {self.author}. Enjoy reading it! ")

    def return_book(self):
        if self.is_borrowed == False:
            print("ERROR!!! This book has not been borrowed. Please try again.")
        else:
            self.is_borrowed = False
            print(f"{self.title} by {self.author} has been returned. We hope you enjoyed reading it!")

    def __str__(self):
        status = "Borrowed" if self.is_borrowed == True else "Available"
        return f"{self.title} by {self.author} [{status}]"


# ── LIBRARY ────────────────────────────────────────────────────
book1 = Book("Oliver Twist", "Charles Dickens")
book2 = Book("Pride & Prejudice", "Jane Austen")
book3 = Book("Hamlet", "William Shakespeare")

print("=" * 42)
print("         📚  LIBRARY SYSTEM")
print("=" * 42)
print(book1)
print(book2)
print(book3)
print()

book2.borrow()
book3.borrow()
book3.borrow()      # already borrowed
print()

book2.return_book()
book1.return_book()  # was not borrowed
print()

print(book1)
print(book2)
print(book3)