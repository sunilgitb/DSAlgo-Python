# Python Object Oriented Programming
# Using class-level and static methods

class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    
    # double-underscore properties are hidden from other classes
    __booklist = None

    # static methods do not receive class or instance arguments
    # and usually operate on data that is not instance- or class-specific
    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    # class methods receive a class as their argument and can only
    # operate on class-level data
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES
    
    @classmethod
    def create_ebook(cls, title):
        """Class method to create EBOOK type books"""
        return cls(title, "EBOOK")

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle
    
    def __init__(self, title, booktype):
        self.title = title
        if booktype not in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.booktype}')"


print("Testing Book Class with Class and Static Methods:")
print("=" * 80)

print("\n1. Accessing class attribute through class method:")
print(f"   Book.getbooktypes() = {Book.getbooktypes()}")

print("\n2. Creating book instances:")
b1 = Book("The Great Gatsby", "HARDCOVER")
b2 = Book("To Kill a Mockingbird", "PAPERBACK")
print(f"   {b1}")
print(f"   {b2}")

print("\n3. Using the static method to access the singleton booklist:")
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(f"   Book.getbooklist() = {thebooks}")

print("\n" + "=" * 80)
print("\n4. Testing book type validation:")

print("\n   Valid book type:")
try:
    b3 = Book("1984", "PAPERBACK")
    print(f"   ✓ Created: {b3}")
except ValueError as e:
    print(f"   ✗ Error: {e}")

print("\n   Invalid book type:")
try:
    b4 = Book("Invalid Book", "AUDIOBOOK")
    print(f"   ✗ Unexpectedly created: {b4}")
except ValueError as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 80)
print("\n5. Testing the singleton nature of the booklist:")

print("\n   Getting booklist from different places:")
list1 = Book.getbooklist()
list2 = Book.getbooklist()
list3 = b1.getbooklist()  # Can also call static method from instance

print(f"   list1 is list2: {list1 is list2}")
print(f"   list1 is list3: {list1 is list3}")
print(f"   All lists are the same object: {list1 is list2 is list3}")

print(f"\n   Current booklist: {list1}")
print(f"   Number of books: {len(list1)}")

print("\n" + "=" * 80)
print("\n6. Adding more books and demonstrating class method:")

print("\n   Using class method to create EBOOK:")
ebook1 = Book.create_ebook("Digital Fortress")
print(f"   Created using class method: {ebook1}")

ebook1.getbooklist().append(ebook1)  # Add to booklist

print("\n   Creating more books:")
books_data = [
    ("Pride and Prejudice", "PAPERBACK"),
    ("Moby Dick", "HARDCOVER"),
    ("The Hobbit", "PAPERBACK"),
]

for title, booktype in books_data:
    try:
        book = Book(title, booktype)
        book.getbooklist().append(book)
        print(f"   Added: {book}")
    except ValueError as e:
        print(f"   Error: {e}")

print(f"\n   Total books in list: {len(Book.getbooklist())}")
print(f"   Booklist: {Book.getbooklist()}")

print("\n" + "=" * 80)
print("\n7. Testing encapsulation (private class attribute):")

print("\n   Trying to access private __booklist directly:")
try:
    print(f"   Book.__booklist = {Book.__booklist}")
except AttributeError as e:
    print(f"   ✓ Correctly prevented: {e}")

print("\n   Accessing through static method (works):")
print(f"   Book.getbooklist() = {Book.getbooklist()}")

print("\n" + "=" * 80)
print("\n8. Book statistics and analysis:")

print("\n   Analyzing book collection:")
booklist = Book.getbooklist()
book_types_count = {}

for book in booklist:
    book_type = book.booktype
    book_types_count[book_type] = book_types_count.get(book_type, 0) + 1

print(f"   Total books: {len(booklist)}")
print(f"   Books by type:")
for book_type, count in book_types_count.items():
    print(f"     {book_type}: {count}")

print("\n   Book titles:")
for i, book in enumerate(booklist, 1):
    print(f"     {i}. {book.title} ({book.booktype})")

print("\n" + "=" * 80)
print("\n9. Testing instance methods:")

print("\n   Using setTitle instance method:")
print(f"   Before: {b1}")
b1.setTitle("The Great Gatsby: Special Edition")
print(f"   After: {b1}")

print("\n   Current state of b1:")
print(f"   Title: {b1.title}")
print(f"   Type: {b1.booktype}")
print(f"   Is in booklist: {b1 in Book.getbooklist()}")

print("\n" + "=" * 80)
print("\n10. Demonstrating class vs instance vs static methods:")

print("\n   Class method usage:")
print(f"   Book.getbooktypes(): {Book.getbooktypes()}")
print(f"   b1.getbooktypes(): {b1.getbooktypes()}")  # Can call from instance too

print("\n   Static method usage:")
print(f"   Book.getbooklist(): {Book.getbooklist()}")
print(f"   b1.getbooklist(): {b1.getbooklist()}")  # Same from instance

print("\n   Instance method usage:")
print(f"   b1.title before: {b1.title}")
b1.setTitle("Renamed Book")
print(f"   b1.title after setTitle(): {b1.title}")

print("\n   Cannot call instance method from class:")
try:
    Book.setTitle("New Title")
    print("   ✗ Unexpectedly worked")
except TypeError as e:
    print(f"   ✓ Correctly failed: {e}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Class attributes (BOOK_TYPES) are shared by all instances")
print("✓ Class methods (@classmethod) operate on class-level data")
print("✓ Static methods (@staticmethod) don't need class/instance reference")
print("✓ Private class attributes (__booklist) are hidden from outside")
print("✓ Singleton pattern implemented with static method")
print("✓ Instance methods operate on specific object instances")
print("✓ Type validation in constructor ensures data integrity")