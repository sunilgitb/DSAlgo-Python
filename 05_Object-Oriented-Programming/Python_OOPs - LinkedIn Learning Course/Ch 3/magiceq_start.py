# Python Object Oriented Programming by Joe Marini course example
# Implementing comparison magic methods

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

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, value):
        """Check if two books are equal based on all attributes."""
        # First check if we're comparing with a Book instance
        if not isinstance(value, Book):
            # Return NotImplemented to let Python try other comparisons
            return NotImplemented
        
        # Compare all three attributes
        return (self.title == value.title and 
                self.author == value.author and 
                self.price == value.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        """Check if this book's price is greater than or equal to another book's price."""
        if not isinstance(value, Book):
            return NotImplemented
        
        return self.price >= value.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
        """Check if this book's price is less than another book's price."""
        if not isinstance(value, Book):
            return NotImplemented
        
        return self.price < value.price

    # Optional: Implement other comparison methods for completeness
    def __ne__(self, value):
        """Check if two books are not equal."""
        return not self.__eq__(value)

    def __le__(self, value):
        """Check if this book's price is less than or equal to another book's price."""
        if not isinstance(value, Book):
            return NotImplemented
        
        return self.price <= value.price

    def __gt__(self, value):
        """Check if this book's price is greater than another book's price."""
        if not isinstance(value, Book):
            return NotImplemented
        
        return self.price > value.price

    # Add __hash__ to make books usable in sets and as dictionary keys
    def __hash__(self):
        return hash((self.title, self.author, self.price))

# Driver code
if __name__ == "__main__":
    # Create book instances
    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
    b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)
    
    print("=== Book Information ===")
    print(f"b1: {b1}")
    print(f"b2: {b2}")
    print(f"b3: {b3}")
    print(f"b4: {b4}")
    
    print("\n" + "="*60 + "\n")
    
    # TODO: Check for equality
    print("=== Equality Comparisons ===")
    print(f"b1 == b3 (identical books): {b1 == b3}")
    print(f"b1 == b2 (different books): {b1 == b2}")
    print(f"b1 != b2 (inequality): {b1 != b2}")
    print(f"b3 == b4 (different books): {b3 == b4}")
    
    # Test comparing with non-Book objects
    print("\nComparing with non-Book objects:")
    print(f"b1 == 'War and Peace' (book vs string): {b1 == 'War and Peace'}")
    print(f"b1 == 42 (book vs number): {b1 == 42}")
    print(f"b1 == None (book vs None): {b1 == None}")
    
    print("\n" + "="*60 + "\n")
    
    # TODO: Check for greater and lesser value
    print("=== Price Comparisons ===")
    print(f"b1 >= b2 (${b1.price:.2f} >= ${b2.price:.2f}): {b1 >= b2}")
    print(f"b1 > b2 (${b1.price:.2f} > ${b2.price:.2f}): {b1 > b2}")
    print(f"b2 < b1 (${b2.price:.2f} < ${b1.price:.2f}): {b2 < b1}")
    print(f"b2 <= b1 (${b2.price:.2f} <= ${b1.price:.2f}): {b2 <= b1}")
    print(f"b4 <= b2 (${b4.price:.2f} <= ${b2.price:.2f}): {b4 <= b2}")
    print(f"b4 >= b2 (${b4.price:.2f} >= ${b2.price:.2f}): {b4 >= b2}")
    
    # Test chained comparisons
    print(f"\nChained comparison (b4 < b2 < b1): {b4 < b2 < b1}")
    print(f"Chained comparison (b4 <= b2 <= b1): {b4 <= b2 <= b1}")
    
    print("\n" + "="*60 + "\n")
    
    # TODO: Now we can sort them too
    print("=== Sorting Books ===")
    books = [b1, b2, b3, b4]
    
    print("Original order:")
    for i, book in enumerate(books, 1):
        print(f"  {i}. ${book.price:.2f} - {book.title}")
    
    # Sort by price (ascending)
    books.sort()
    print("\nSorted by price (ascending):")
    for i, book in enumerate(books, 1):
        print(f"  {i}. ${book.price:.2f} - {book.title}")
    
    # Sort by price (descending)
    books.sort(reverse=True)
    print("\nSorted by price (descending):")
    for i, book in enumerate(books, 1):
        print(f"  {i}. ${book.price:.2f} - {book.title}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Using Books in Data Structures ===")
    
    # Using books in a set
    print("Creating a set of books (duplicate b1/b3 will be removed):")
    book_set = {b1, b2, b3, b4}
    print(f"Set contains {len(book_set)} unique books:")
    for book in book_set:
        print(f"  - {book}")
    
    # Using books as dictionary keys
    print("\nUsing books as dictionary keys:")
    inventory = {
        b1: 10,
        b2: 5,
        b4: 8
    }
    
    # Note: b3 won't be added as a separate key since it's equal to b1
    inventory[b3] = 15  # This will update b1's value since b3 == b1
    print("Inventory (b3 updates b1 because they're equal):")
    for book, quantity in inventory.items():
        print(f"  {book.title}: {quantity} copies")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Practical Application: Bookstore Operations ===")
    
    # Find the most expensive book
    all_books = [b1, b2, b3, b4]
    most_expensive = max(all_books)
    least_expensive = min(all_books)
    print(f"Most expensive book: {most_expensive}")
    print(f"Least expensive book: {least_expensive}")
    
    # Filter books by price
    affordable_books = [book for book in all_books if book.price <= 30]
    print(f"\nBooks under $30 ({len(affordable_books)} found):")
    for book in affordable_books:
        print(f"  {book}")
    
    # Check if books are in a certain price range
    print("\nChecking price ranges:")
    price_ranges = [
        ("Under $25", lambda b: b.price < 25),
        ("$25-$35", lambda b: 25 <= b.price <= 35),
        ("Over $35", lambda b: b.price > 35)
    ]
    
    for range_name, condition in price_ranges:
        books_in_range = [book for book in all_books if condition(book)]
        print(f"{range_name}: {len(books_in_range)} books")
        for book in books_in_range:
            print(f"  - {book.title} (${book.price:.2f})")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Alternative Implementation: Using @total_ordering ===")
    
    from functools import total_ordering
    
    @total_ordering
    class CompactBook:
        """A more compact implementation using total_ordering decorator."""
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price
        
        def __eq__(self, other):
            if not isinstance(other, CompactBook):
                return NotImplemented
            return (self.title, self.author, self.price) == (other.title, other.author, other.price)
        
        def __lt__(self, other):
            if not isinstance(other, CompactBook):
                return NotImplemented
            return self.price < other.price
        
        def __str__(self):
            return f"'{self.title}' by {self.author}, ${self.price:.2f}"
        
        def __hash__(self):
            return hash((self.title, self.author, self.price))
    
    print("Using @total_ordering decorator (requires only __eq__ and one ordering method):")
    cb1 = CompactBook("Dune", "Frank Herbert", 35.95)
    cb2 = CompactBook("Foundation", "Isaac Asimov", 25.95)
    
    print(f"cb1: {cb1}")
    print(f"cb2: {cb2}")
    print(f"cb1 == cb2: {cb1 == cb2}")
    print(f"cb1 > cb2: {cb1 > cb2}")
    print(f"cb1 <= cb2: {cb1 <= cb2}")
    print(f"cb1 >= cb2: {cb1 >= cb2}")
    
    print("\n" + "="*60 + "\n")
    
    print("=== Key Takeaways ===")
    print("1. __eq__ enables equality comparison (==)")
    print("2. __lt__ enables less-than comparison (<) and sorting")
    print("3. __ge__ enables greater-or-equal comparison (>=)")
    print("4. Implement __hash__ when implementing __eq__ for use in sets/dicts")
    print("5. Return NotImplemented for unsupported comparison types")
    print("6. Use @total_ordering decorator to reduce boilerplate code")
    print("7. Comparison methods enable sorting, min(), max(), and in/not in operations")