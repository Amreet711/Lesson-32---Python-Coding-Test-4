class Book: 
    #define __init__ for author, title and is_borrwed
    def __init__(self, author, title, is_borrowed):
        self.author = author
        self.title = title
        self.is_borrowed = is_borrowed
    #define borrow()
    def borrow(self):
        self.is_borrowed = True
        print ("This book has been borrowed. Enjoy reading!")
    #define return_book()
    def return_book(self):
        self.is_borrowed = False
        print ("This book has been returned. Thank you!")
#Three Book objects
book1=Book("Di Walker", "Saving Charlie", False)
book2=Book("Hayley Lawrence", "What They Told Me", False)
book3=Book("J.K. Rowling", "Harry Potter and the Chamber of Secrets", False)
#Actions
action=input("Are you borrowing or returning a book?")
if action == "borrowing":
    choice=input(f"Which book would you like to borrow: {book1.title}, {book2.title} or {book3.title}?")
    if choice == book1.title:
        book1.borrow()
    elif choice == book2.title:
        book2.borrow() 
    else:
        book3.borrow()    
else:
    choice=input(f"Which book would you like to return: {book1.title}, {book2.title} or {book3.title}?")
    if choice == book1.title:
        book1.return_book()
    elif choice == book2.title:
        book2.return_book() 
    else:
        book3.return_book()

    