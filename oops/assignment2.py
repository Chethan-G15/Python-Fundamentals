# Class Name: Library

# Attributes (inside constructor __init__):

# name → name of the library

# books → a  dictionary storing book titles as keys and number of copies as values

# Methods:

# add_book(title, copies) → add a new book or increase copies if it already exists

# show_books() → print all books and their available copies

# borrow_book(title) → reduce the number of copies by 1 if available, otherwise print "Not available"

# return_book(title) → increase the number of copies by 1

class Library:
    def __init__(self,name):
        self.name = name
        self.books = {}
    def add_books(self,title,copies):
        if title in self.books:
            self.books[title]+=copies
        else:
            self.books[title]=copies
        print(f"Added {copies} of Books{title}")

    def show_books(self):
        for title,copy in self.books.items():
            print(f"The book of{title} there are {copy}")

    def borrow_book(self,title):
        if title in self.books and self.books[title]>0:
            self.books[title]-=1
            print(f"You have borrowe the book{title}")
        else:
            print("Not Available")

    def return_book(self,title):
        if title in self.books:
            self.books[title]+=1
        else:
            self.books[title]=1

# -------- Testing --------
library = Library("City Library")
library1 = Library("national library")

library.add_books("1984", 3)
library.add_books("To Kill a Mockingbird", 2)
library.add_books("The Great Gatsby", 1)

library1.add_books("2026",1)

library.show_books()

library1.show_books()

library.borrow_book("1984")
library.borrow_book("The Great Gatsby")
library.borrow_book("The Great Gatsby")  # Not available

library.show_books()

library.return_book("The Great Gatsby")
 
library.show_books()
