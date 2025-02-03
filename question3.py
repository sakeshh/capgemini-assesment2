# 3. You are building a Library Management System. 
# Create a `Book` class with properties like `title`, `author`, and `isbn`. 
# Write a method to display book details.
class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print(f"book details:\ntitle:{self.title}\nauthor:{self.author}\nisbn:{self.isbn}")
book=Book("the idea of u","sarfarazz","890")
book.display()
