# Python Object Oriented Programming
# Using class-level and static methods

class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK", "AUDIOBOOK")
    
    # double-underscore properties are hidden from other classes
    __booklist = None
    
    # class methods receive a class as their argument and can only
    # operate on class-level data
    @classmethod
    def getbooktypes(cls):
        """Return all available book types"""
        return cls.BOOK_TYPES
    
    @classmethod
    def get_popular_books(cls):
        """Class method to get predefined popular books"""
        return [
            cls("To Kill a Mockingbird"),
            cls("1984"),
            cls("The Great Gatsby")
        ]
    
    # static methods do not receive class or instance arguments
    # and usually operate on data that is not instance- or class-specific
    @staticmethod
    def getbooklist():
        """Static method to access the singleton booklist"""
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist
    
    @staticmethod
    def get_total_books_count():
        """Static method to get total number of books created"""
        booklist = Book.getbooklist()
        return len(booklist)
    
    @staticmethod
    def search_books(keyword):
        """Static method to search books by keyword"""
        results = []
        booklist = Book.getbooklist()
        for book in booklist:
            if keyword.lower() in book.title.lower():
                results.append(book)
        return results

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        """Instance method to change book title"""
        self.title = newtitle
    
    def get_details(self):
        """Instance method to get book details"""
        return f"Title: {self.title}"
    
    def __init__(self, title, booktype="PAPERBACK"):
        """Initialize a book with title and optional type"""
        self.title = title
        if booktype not in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type. Valid types are: {Book.BOOK_TYPES}")
        self.booktype = booktype
        
        # Add to the shared booklist
        Book.getbooklist().append(self)
    
    def __repr__(self):
        """String representation of the book"""
        return f"Book('{self.title}', '{self.booktype}')"


print("Testing Book Class with Class and Static Methods:")
print("=" * 80)

print("\n1. Accessing class attribute through class method:")
print(f"   Book.getbooktypes() = {Book.getbooktypes()}")

print("\n2. Creating book instances:")
b1 = Book("The Catcher in the Rye", "PAPERBACK")
b2 = Book("Pride and Prejudice", "HARDCOVER")
b3 = Book("Digital Fortress", "EBOOK")
print(f"   {b1}")
print(f"   {b2}")
print(f"   {b3}")

print("\n3. Using the static method to access the singleton booklist:")
thebooks = Book.getbooklist()
print(f"   Book.getbooklist() = {thebooks}")
print(f"   Number of books: {len(thebooks)}")

print("\n" + "=" * 80)
print("\n4. Testing class method for popular books:")

print("\n   Getting popular books using class method:")
popular_books = Book.get_popular_books()
for i, book in enumerate(popular_books, 1):
    print(f"   {i}. {book}")

print("\n   Booklist after adding popular books:")
print(f"   Total books: {Book.get_total_books_count()}")
print(f"   Booklist: {Book.getbooklist()}")

print("\n" + "=" * 80)
print("\n5. Testing static methods for utility functions:")

print("\n   Getting total books count:")
print(f"   Book.get_total_books_count() = {Book.get_total_books_count()}")

print("\n   Searching books by keyword 'the':")
search_results = Book.search_books("the")
for i, book in enumerate(search_results, 1):
    print(f"   {i}. {book}")

print("\n   Searching books by keyword 'digital':")
search_results = Book.search_books("digital")
for i, book in enumerate(search_results, 1):
    print(f"   {i}. {book}")

print("\n" + "=" * 80)
print("\n6. Testing book type validation:")

print("\n   Valid book type (AUDIOBOOK):")
try:
    b4 = Book("Audio Book Example", "AUDIOBOOK")
    print(f"   ✓ Created: {b4}")
except ValueError as e:
    print(f"   ✗ Error: {e}")

print("\n   Invalid book type:")
try:
    b5 = Book("Invalid Type Book", "COMIC")
    print(f"   ✗ Unexpectedly created: {b5}")
except ValueError as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 80)
print("\n7. Testing instance methods:")

print("\n   Using instance methods:")
print(f"   b1.get_details(): {b1.get_details()}")
print(f"   b1.title before: {b1.title}")
b1.setTitle("The Catcher in the Rye - Revised Edition")
print(f"   b1.title after setTitle(): {b1.title}")
print(f"   b1.get_details(): {b1.get_details()}")

print("\n" + "=" * 80)
print("\n8. Testing encapsulation (private class attribute):")

print("\n   Trying to access private __booklist directly:")
try:
    print(f"   Book.__booklist = {Book.__booklist}")
except AttributeError as e:
    print(f"   ✓ Correctly prevented: {e}")

print("\n   Trying to name mangling (still shouldn't work easily):")
try:
    # Python does name mangling for private attributes
    print(f"   Book._Book__booklist exists: {hasattr(Book, '_Book__booklist')}")
    if hasattr(Book, '_Book__booklist'):
        print(f"   But it's still not meant to be accessed directly")
except:
    print("   Cannot access even with name mangling")

print("\n   Proper access through static method:")
print(f"   Book.getbooklist() works: {len(Book.getbooklist()) > 0}")

print("\n" + "=" * 80)
print("\n9. Book collection analysis:")

print("\n   Current book collection:")
booklist = Book.getbooklist()
book_types_count = {}

for book in booklist:
    book_type = book.booktype
    book_types_count[book_type] = book_types_count.get(book_type, 0) + 1

print(f"   Total books: {len(booklist)}")
print(f"   Books by type:")
for book_type in Book.BOOK_TYPES:
    count = book_types_count.get(book_type, 0)
    print(f"     {book_type}: {count}")

print("\n   All book titles:")
for i, book in enumerate(booklist, 1):
    print(f"     {i}. {book.title} ({book.booktype})")

print("\n" + "=" * 80)
print("\n10. Demonstrating different method types:")

print("\n   Class Method (operates on class level):")
print(f"   - Book.getbooktypes(): Returns all book types")
print(f"   - Book.get_popular_books(): Returns predefined books")

print("\n   Static Method (no class/instance reference needed):")
print(f"   - Book.getbooklist(): Returns singleton booklist")
print(f"   - Book.get_total_books_count(): Returns count")
print(f"   - Book.search_books(): Searches by keyword")

print("\n   Instance Method (operates on specific instance):")
print(f"   - book.setTitle(): Changes title of specific book")
print(f"   - book.get_details(): Gets details of specific book")

print("\n   Can call static and class methods from instances:")
print(f"   b1.getbooktypes(): {b1.getbooktypes()}")
print(f"   b1.getbooklist() is Book.getbooklist(): {b1.getbooklist() is Book.getbooklist()}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Class methods (@classmethod) work with class-level data")
print("✓ Static methods (@staticmethod) are utility functions")
print("✓ Instance methods work with specific object data")
print("✓ Private attributes (__booklist) provide encapsulation")
print("✓ Singleton pattern with static method for shared data")
print("✓ Validation ensures data integrity")
print("✓ All method types serve different purposes in OOP")