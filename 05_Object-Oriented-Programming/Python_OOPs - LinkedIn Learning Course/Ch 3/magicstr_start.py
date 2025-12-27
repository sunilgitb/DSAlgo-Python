# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    def __str__(self):
        """Return a user-friendly string representation of the Book."""
        return f"📖 '{self.title}' by {self.author} - ${self.price:.2f}"

    # TODO: use the __repr__ method to return an obj representation
    def __repr__(self):
        """Return an unambiguous string representation of the Book.
        Should ideally allow object recreation with eval()."""
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"

    # Additional optional methods for completeness
    def __format__(self, format_spec):
        """Allow custom formatting of Book objects."""
        if format_spec == "short":
            return self.title
        elif format_spec == "csv":
            return f'"{self.title}","{self.author}",{self.price}'
        elif format_spec == "json":
            return f'{{"title": "{self.title}", "author": "{self.author}", "price": {self.price}}}'
        else:
            # Default to __str__
            return str(self)

# Driver code
if __name__ == "__main__":
    # Create book instances
    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
    b3 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)
    b4 = Book("1984", "George Orwell", 19.95)
    
    print("="*70)
    print("CREATING BOOK OBJECTS")
    print("="*70)
    
    print(f"\nb1 = Book('War and Peace', 'Leo Tolstoy', 39.95)")
    print(f"b2 = Book('The Catcher in the Rye', 'JD Salinger', 29.95)")
    print(f"b3 = Book('To Kill a Mockingbird', 'Harper Lee', 24.95)")
    print(f"b4 = Book('1984', 'George Orwell', 19.95)")
    
    print("\n" + "="*70)
    print("TESTING __str__ METHOD")
    print("="*70)
    
    # Direct printing uses __str__
    print("\nDirect print() statements (uses __str__):")
    print("print(b1):", end=" ")
    print(b1)
    print("print(b2):", end=" ")
    print(b2)
    print("print(b3):", end=" ")
    print(b3)
    print("print(b4):", end=" ")
    print(b4)
    
    print("\nUsing str() function explicitly:")
    print(f"str(b1): {str(b1)}")
    print(f"str(b2): {str(b2)}")
    
    print("\nIn f-strings (uses __str__ by default):")
    print(f"Book on sale: {b1}")
    print(f"Classic novel: {b2}")
    
    print("\n" + "="*70)
    print("TESTING __repr__ METHOD")
    print("="*70)
    
    print("\nUsing repr() function (for debugging/development):")
    print(f"repr(b1): {repr(b1)}")
    print(f"repr(b2): {repr(b2)}")
    print(f"repr(b3): {repr(b3)}")
    print(f"repr(b4): {repr(b4)}")
    
    print("\nIn Python REPL or debuggers, typing 'b1' shows repr():")
    print(">>> b1")
    print(repr(b1))
    
    print("\n" + "="*70)
    print("PRACTICAL DIFFERENCES & USE CASES")
    print("="*70)
    
    print("\n1. In containers (lists, dicts) - uses __repr__:")
    books_list = [b1, b2, b3, b4]
    print(f"books_list = {books_list}")
    
    books_dict = {"classic": b1, "modern": b2}
    print(f"books_dict = {books_dict}")
    
    print("\n2. When __str__ is not available, Python falls back to __repr__:")
    
    class BookWithoutStr:
        def __init__(self, title):
            self.title = title
        
        def __repr__(self):
            return f"BookWithoutStr('{self.title}')"
    
    book_simple = BookWithoutStr("Simple Book")
    print(f"Book without __str__: {book_simple}")
    print(f"str(book_simple): {str(book_simple)}")
    print(f"repr(book_simple): {repr(book_simple)}")
    
    print("\n3. Interactive session example:")
    print("""
    # In Python interactive shell:
    >>> b = Book("Sample", "Author", 9.99)
    >>> b                # Shows repr()
    Book(title='Sample', author='Author', price=9.99)
    >>> print(b)         # Shows str()
    📖 'Sample' by Author - $9.99
    >>> [b]              # Shows repr() in container
    [Book(title='Sample', author='Author', price=9.99)]
    """)
    
    print("\n" + "="*70)
    print("ADVANCED: CUSTOM FORMATTING WITH __format__")
    print("="*70)
    
    print("\nUsing custom format specifiers:")
    print(f"Default format: {b1}")
    print(f"Short format (b1:short): {b1:short}")
    print(f"CSV format (b1:csv): {b1:csv}")
    print(f"JSON format (b1:json): {b1:json}")
    
    print("\nFormatted table using custom formats:")
    print(f"{'Title':<30} {'Author':<20} {'Price':>10}")
    print("-" * 65)
    for book in books_list:
        print(f"{book:short:<30} {book.author:<20} ${book.price:>7.2f}")
    
    print("\n" + "="*70)
    print("IMPLEMENTATION DETAILS & BEST PRACTICES")
    print("="*70)
    
    print("\nGood __str__ implementation should be:")
    print("• Human-readable")
    print("• User-friendly")
    print("• Natural language")
    print("• Can include emojis or formatting")
    
    print("\nGood __repr__ implementation should be:")
    print("• Unambiguous")
    print("• Complete (show all important attributes)")
    print("• Ideally recreatable with eval()")
    print("• Include class name")
    
    print("\nExample of eval() recreation (conceptual):")
    print(f"repr(b1) = {repr(b1)}")
    print("# eval(repr(b1)) would create a similar Book object")
    
    print("\n" + "="*70)
    print("COMPARISON WITH OTHER OBJECTS")
    print("="*70)
    
    print("\nBuilt-in objects also have str and repr:")
    num = 42
    print(f"Number: num = {num}")
    print(f"str(num): {str(num)}")
    print(f"repr(num): {repr(num)}")
    
    lst = [1, 2, 3]
    print(f"\nList: lst = {lst}")
    print(f"str(lst): {str(lst)}")
    print(f"repr(lst): {repr(lst)}")
    
    print("\n" + "="*70)
    print("REAL-WORLD EXAMPLE: LIBRARY SYSTEM")
    print("="*70)
    
    class LibraryBook(Book):
        def __init__(self, title, author, price, isbn, genre=None):
            super().__init__(title, author, price)
            self.isbn = isbn
            self.genre = genre
            self.checked_out = False
        
        def __str__(self):
            """User-friendly display for library patrons."""
            status = "📗 Available" if not self.checked_out else "📕 Checked Out"
            genre_info = f" ({self.genre})" if self.genre else ""
            return f"{super().__str__()}{genre_info} | {status}"
        
        def __repr__(self):
            """Complete representation for librarians."""
            return (f"LibraryBook(title='{self.title}', author='{self.author}', "
                    f"price={self.price}, isbn='{self.isbn}', genre='{self.genre}')")
        
        def checkout(self):
            self.checked_out = True
            return self
        
        def return_book(self):
            self.checked_out = False
            return self
    
    print("\nCreating library books:")
    lb1 = LibraryBook("Dune", "Frank Herbert", 35.95, 
                     "978-0441172719", "Science Fiction")
    lb2 = LibraryBook("Pride and Prejudice", "Jane Austen", 19.95,
                     "978-0141439518", "Romance")
    
    print("\nFor library patrons (__str__):")
    print(f"Display: {lb1}")
    print(f"Display: {lb2}")
    
    print("\nFor library staff (__repr__):")
    print(f"Debug: {repr(lb1)}")
    print(f"Debug: {repr(lb2)}")
    
    print("\nAfter checkout:")
    lb1.checkout()
    print(f"After checkout: {lb1}")
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    print("""
    Key Points:
    1. __str__: For end-users (print(), str(), f-strings)
    2. __repr__: For developers (REPL, containers, debugging)
    3. Always implement __repr__ at minimum
    4. Make __repr__ unambiguous and ideally eval()-able
    5. __str__ can be more creative and user-friendly
    6. If only __repr__ exists, it's used for both
    
    Remember:
    • print(obj) → __str__
    • [obj1, obj2] → __repr__
    • In REPL: typing obj → __repr__
    • f"{obj}" → __str__
    """)