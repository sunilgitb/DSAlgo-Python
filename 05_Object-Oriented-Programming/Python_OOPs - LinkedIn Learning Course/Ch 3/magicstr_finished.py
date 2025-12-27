# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"📚 '{self.title}' by {self.author} - ${self.price:.2f}"

    # The __repr__ function is used to return a developer-friendly string
    # representation of the object
    def __repr__(self):
        # A good repr should ideally allow recreating the object
        # Using eval(repr(obj)) should create a similar object
        return f"Book('{self.title}', '{self.author}', {self.price})"

    # Additional magic method: __format__ for custom formatting
    def __format__(self, format_spec):
        if format_spec == "short":
            return f"{self.title}"
        elif format_spec == "author_first":
            return f"{self.author}: {self.title}"
        elif format_spec == "price":
            return f"${self.price:.2f}"
        elif format_spec == "csv":
            return f'"{self.title}","{self.author}",{self.price}'
        else:
            # Default format
            return str(self)

# Driver code
if __name__ == "__main__":
    print("=== Creating Book Objects ===")
    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
    b3 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)
    
    print("\n" + "="*60 + "\n")
    
    print("=== Basic Usage: print() uses __str__ ===")
    print("Direct print() calls:")
    print(b1)  # Uses __str__
    print(b2)  # Uses __str__
    print(b3)  # Uses __str__
    
    print("\n" + "="*60 + "\n")
    
    print("=== Explicit str() and repr() Calls ===")
    print("Using str() function (user-friendly):")
    print(f"str(b1): {str(b1)}")
    print(f"str(b2): {str(b2)}")
    
    print("\nUsing repr() function (developer-friendly):")
    print(f"repr(b1): {repr(b1)}")
    print(f"repr(b2): {repr(b2)}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Where __str__ and __repr__ are Used ===")
    
    # In containers (lists, tuples, dicts) - uses __repr__
    print("\n1. In containers (uses __repr__):")
    books_list = [b1, b2, b3]
    print(f"List of books: {books_list}")
    
    books_dict = {1: b1, 2: b2, 3: b3}
    print(f"Dictionary values: {books_dict}")
    
    # In f-strings - uses __str__ by default
    print("\n2. In f-strings (uses __str__ by default):")
    print(f"Book 1: {b1}")
    print(f"Book 2: {b2}")
    
    # Explicit conversion in f-strings
    print("\n3. Explicit conversion in f-strings:")
    print(f"User view: {str(b1)}")
    print(f"Debug view: {repr(b1)}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Testing eval() with repr() ===")
    print("A good __repr__ should allow object recreation with eval():")
    b1_repr = repr(b1)
    print(f"repr(b1) = {b1_repr}")
    
    # In real code, be careful with eval() due to security risks
    # This is just to demonstrate the concept
    print("\nManually creating similar object from repr string:")
    print(f"Book{repr(b1)}")  # Shows what eval() would evaluate to
    
    print("\n" + "="*60 + "\n")
    
    print("=== When __str__ is not defined ===")
    
    class BookWithoutStr:
        def __init__(self, title, author):
            self.title = title
            self.author = author
        
        # Only __repr__ is defined
        def __repr__(self):
            return f"BookWithoutStr('{self.title}', '{self.author}')"
    
    book_no_str = BookWithoutStr("1984", "George Orwell")
    print(f"Book without __str__: {book_no_str}")  # Falls back to __repr__
    print(f"str(book_no_str): {str(book_no_str)}")  # Also uses __repr__
    
    print("\n" + "="*60 + "\n")
    
    print("=== Best Practices Comparison ===")
    
    class GoodBook:
        """Example of proper __str__ and __repr__ implementation."""
        def __init__(self, title, author, price, isbn=None):
            self.title = title
            self.author = author
            self.price = price
            self.isbn = isbn
        
        def __str__(self):
            """User-friendly representation."""
            price_str = f"${self.price:.2f}"
            if self.isbn:
                return f"'{self.title}' by {self.author} ({price_str}) [ISBN: {self.isbn}]"
            return f"'{self.title}' by {self.author} ({price_str})"
        
        def __repr__(self):
            """Developer-friendly representation that can recreate object."""
            args = [f"'{self.title}'", f"'{self.author}'", str(self.price)]
            if self.isbn:
                args.append(f"'{self.isbn}'")
            return f"GoodBook({', '.join(args)})"
    
    class BadBook:
        """Example of poor __str__ and __repr__ implementation."""
        def __init__(self, title, author):
            self.title = title
            self.author = author
        
        def __str__(self):
            """Too verbose for users."""
            return f"This is a book object with the following properties: title={self.title}, author={self.author}, and it's stored at memory address {id(self)}"
        
        def __repr__(self):
            """Doesn't allow recreation and is not helpful for debugging."""
            return f"<Book>"
    
    print("Good implementation:")
    gb = GoodBook("Pride and Prejudice", "Jane Austen", 19.95, "978-0141439518")
    print(f"  str(): {str(gb)}")
    print(f"  repr(): {repr(gb)}")
    
    print("\nBad implementation:")
    bb = BadBook("Bad Example", "Bad Author")
    print(f"  str(): {str(bb)}")
    print(f"  repr(): {repr(bb)}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Advanced: Custom Formatting with __format__ ===")
    print("Using custom format specifications:")
    
    print(f"\nDefault format: {b1}")
    print(f"Short format: {b1:short}")
    print(f"Author first: {b1:author_first}")
    print(f"Price only: {b1:price}")
    print(f"CSV format: {b1:csv}")
    
    # Using in loops
    print("\nFormatted list:")
    books = [b1, b2, b3]
    for book in books:
        print(f"  • {book:author_first}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Interactive Session Example ===")
    print("In an interactive Python session (like IPython or Jupyter):")
    print("""
    >>> b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    >>> b1  # This uses __repr__
    Book('War and Peace', 'Leo Tolstoy', 39.95)
    
    >>> print(b1)  # This uses __str__
    📚 'War and Peace' by Leo Tolstoy - $39.95
    
    >>> [b1, b2]  # Container uses __repr__
    [Book('War and Peace', 'Leo Tolstoy', 39.95), 
     Book('The Catcher in the Rye', 'JD Salinger', 29.95)]
    """)
    
    print("\n" + "="*60 + "\n")
    
    print("=== Key Differences Summary ===")
    print("""
    __str__ (str()):
    • Meant for end-users
    • Should be human-readable
    • Used by print(), str(), format(), and f-strings (by default)
    • Informal representation
    
    __repr__ (repr()):
    • Meant for developers
    • Should be unambiguous
    • Ideally should allow object recreation with eval()
    • Used in containers, debuggers, and when evaluating in REPL
    • Official representation
    """)
    
    print("\n=== Golden Rule ===")
    print("Always implement __repr__ (for debugging)")
    print("Implement __str__ if you need a user-friendly version")
    print("If only __repr__ is defined, it will be used for both")