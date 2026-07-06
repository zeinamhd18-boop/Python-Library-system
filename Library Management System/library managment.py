class Book:
    def __init__(self, title, author):
        self.title = title
        self.author =  author    
        self.is_borrowed = False
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - Status:{status}" 
class library:
     def __init__(self):
          self.books =[]     
     def add_book(self, book):
           self.books.append(book)
           print(f"Added book: {book.title}")

     def list_books(self):
          print("\n___ Library Catalog ___")  
          for book in self.books:
              print(book) 
     def borrow_book(self, title):
         for book in self.books:              
              if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"you have successfully borrowed:{title}")
                    return
                else:
                    print("Book is already borrowed: ") 
                    return
     print("Book not found.")     




 # Create an instanc) 

# Add a book to the library 
book1 = Book("The Alchemist", "Paulo Coelho ")  
my_library.add_book(book1) 

#List all books
my_library.list_books()

#Try to borrow the book
my_library.borrow_book("The Alchemist")

#Try to borrow a book that does not exist
my_library.borrow_book("Harry")
