# Python Object Oriented Programming by Joe Marini course example
# Using comparison magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"'{self.title}' by {self.author}, ${self.price:.2f}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"

    # the __eq__ method checks for equality between two objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")
        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    # the __ne__ method checks for inequality (not strictly necessary as Python provides default)
    def __ne__(self, value):
        return not self.__eq__(value)

    # the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")
        return self.price >= value.price

    # the __le__ establishes <= relationship with another obj
    def __le__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")
        return self.price <= value.price

    # the __gt__ establishes > relationship with another obj
    def __gt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")
        return self.price > value.price

    # the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")
        return self.price < value.price

    # __hash__ method to make books hashable (for use in sets and as dict keys)
    def __hash__(self):
        return hash((self.title, self.author, self.price))

# Driver code
if __name__ == "__main__":
    print("=== Creating Book Objects ===")
    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
    b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)
    b5 = Book("1984", "George Orwell", 19.95)
    
    print(f"b1: {b1}")
    print(f"b2: {b2}")
    print(f"b3: {b3}")
    print(f"b4: {b4}")
    print(f"b5: {b5}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Testing Equality Comparisons (__eq__) ===")
    print(f"b1 == b3 (same title, author, price): {b1 == b3}")
    print(f"b1 == b2 (different books): {b1 == b2}")
    print(f"b1 != b2 (inequality): {b1 != b2}")
    print(f"b2 == b4 (different books): {b2 == b4}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Testing Invalid Comparisons ===")
    try:
        print(f"b1 == 42 (book vs integer): ", end="")
        print(b1 == 42)
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        print(f"b1 == 'string' (book vs string): ", end="")
        print(b1 == 'string')
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Testing Greater/Less Than Comparisons ===")
    print(f"b1 >= b2 (${b1.price:.2f} >= ${b2.price:.2f}): {b1 >= b2}")
    print(f"b1 > b2 (${b1.price:.2f} > ${b2.price:.2f}): {b1 > b2}")
    print(f"b2 < b1 (${b2.price:.2f} < ${b1.price:.2f}): {b2 < b1}")
    print(f"b2 <= b1 (${b2.price:.2f} <= ${b1.price:.2f}): {b2 <= b1}")
    print(f"b4 <= b5 (${b4.price:.2f} <= ${b5.price:.2f}): {b4 <= b5}")
    print(f"b4 >= b5 (${b4.price:.2f} >= ${b5.price:.2f}): {b4 >= b5}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Sorting Books (uses __lt__) ===")
    books = [b1, b2, b3, b4, b5]
    print("Unsorted books:")
    for book in books:
        print(f"  ${book.price:.2f}: {book.title}")
    
    books.sort()
    print("\nSorted by price (ascending):")
    for book in books:
        print(f"  ${book.price:.2f}: {book.title}")
    
    books.sort(reverse=True)
    print("\nSorted by price (descending):")
    for book in books:
        print(f"  ${book.price:.2f}: {book.title}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Using Books in Data Structures ===")
    
    # Using books in a set (requires __hash__ method)
    print("Creating a set of books (removes duplicates):")
    book_set = {b1, b2, b3, b4, b5}
    print(f"Set size: {len(book_set)} (b1 and b3 are equal, so only one is kept)")
    for book in book_set:
        print(f"  {book}")
    
    # Using books as dictionary keys (requires __hash__ method)
    print("\nUsing books as dictionary keys:")
    inventory = {
        b1: 5,
        b2: 3,
        b4: 7,
        b5: 2
    }
    for book, quantity in inventory.items():
        print(f"  {book.title}: {quantity} in stock")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Testing All Comparison Operators ===")
    test_cases = [
        ("b1 < b2", b1 < b2),
        ("b1 <= b2", b1 <= b2),
        ("b1 > b2", b1 > b2),
        ("b1 >= b2", b1 >= b2),
        ("b1 == b3", b1 == b3),
        ("b1 != b2", b1 != b2),
        ("b4 < b5", b4 < b5),
        ("b4 <= b5", b4 <= b5),
        ("b4 > b5", b4 > b5),
        ("b4 >= b5", b4 >= b5),
    ]
    
    for test, result in test_cases:
        print(f"{test:15} → {result}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Advanced Example: Multi-criteria Comparison ===")
    
    class EnhancedBook(Book):
        def __lt__(self, other):
            """Compare by author first, then title, then price."""
            if not isinstance(other, EnhancedBook):
                raise ValueError("Can't compare EnhancedBook to non-EnhancedBook")
            
            # Compare authors
            if self.author != other.author:
                return self.author < other.author
            
            # If authors are equal, compare titles
            if self.title != other.title:
                return self.title < other.title
            
            # If titles are equal, compare prices
            return self.price < other.price
        
        def __eq__(self, other):
            """Enhanced equality check."""
            if not isinstance(other, EnhancedBook):
                return False
            return (self.title == other.title and
                    self.author == other.author and
                    self.price == other.price)
    
    print("Creating EnhancedBook objects with multi-criteria comparison:")
    eb1 = EnhancedBook("War and Peace", "Leo Tolstoy", 39.95)
    eb2 = EnhancedBook("Anna Karenina", "Leo Tolstoy", 34.95)
    eb3 = EnhancedBook("1984", "George Orwell", 19.95)
    eb4 = EnhancedBook("Animal Farm", "George Orwell", 14.95)
    eb5 = EnhancedBook("The Hobbit", "J.R.R. Tolkien", 29.95)
    
    enhanced_books = [eb1, eb2, eb3, eb4, eb5]
    enhanced_books.sort()
    
    print("Sorted by author, then title:")
    for book in enhanced_books:
        print(f"  Author: {book.author:20} Title: {book.title:25} Price: ${book.price:6.2f}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Best Practices Summary ===")
    print("1. Implement __eq__ for equality comparisons")
    print("2. Implement __lt__ and __le__ (or __gt__ and __ge__) for ordering")
    print("3. Python can infer the reverse comparisons from what you implement")
    print("4. Always validate input types in comparison methods")
    print("5. Implement __hash__ if you implement __eq__ (for use in sets/dicts)")
    print("6. Be consistent: if a == b is True, then hash(a) == hash(b) should be True")
    print("7. Comparison methods should return NotImplemented for unsupported types")