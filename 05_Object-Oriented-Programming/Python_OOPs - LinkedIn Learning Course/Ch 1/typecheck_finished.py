# Python Object Oriented Programming
# Checking class types and instances

class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


class Magazine:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")
m1 = Magazine("Time Magazine")
m2 = Magazine("National Geographic")

print("Testing Type Checking and Instance Checking:")
print("=" * 80)

# TODO: use type() to inspect the object type
print("1. Using type() to inspect object types:")
print(f"   type(b1): {type(b1)}")
print(f"   type(b2): {type(b2)}")
print(f"   type(n1): {type(n1)}")
print(f"   type(n2): {type(n2)}")
print(f"   type(m1): {type(m1)}")
print(f"   type(m2): {type(m2)}")

print("\n   Getting type names:")
print(f"   type(b1).__name__: {type(b1).__name__}")
print(f"   type(n1).__name__: {type(n1).__name__}")

print("\n" + "=" * 80)

# TODO: compare two types together
print("2. Comparing types together:")
print(f"   type(b1) == type(b2): {type(b1) == type(b2)}")
print(f"   type(n1) == type(n2): {type(n1) == type(n2)}")
print(f"   type(b1) == type(n1): {type(b1) == type(n1)}")
print(f"   type(m1) == type(m2): {type(m1) == type(m2)}")
print(f"   type(b1) == type(m1): {type(b1) == type(m1)}")

print("\n" + "=" * 80)

# TODO: use isinstance to compare a specific instance to a known type
print("3. Using isinstance() to check instances:")
print(f"   isinstance(b1, Book): {isinstance(b1, Book)}")
print(f"   isinstance(b2, Book): {isinstance(b2, Book)}")
print(f"   isinstance(n1, Newspaper): {isinstance(n1, Newspaper)}")
print(f"   isinstance(n2, Newspaper): {isinstance(n2, Newspaper)}")

print(f"\n   isinstance(n2, Book): {isinstance(n2, Book)}")
print(f"   isinstance(b1, Newspaper): {isinstance(b1, Newspaper)}")
print(f"   isinstance(m1, Magazine): {isinstance(m1, Magazine)}")
print(f"   isinstance(m2, Newspaper): {isinstance(m2, Newspaper)}")

print(f"\n   isinstance(n2, object): {isinstance(n2, object)}")
print(f"   isinstance(b1, object): {isinstance(b1, object)}")
print(f"   isinstance('hello', object): {isinstance('hello', object)}")
print(f"   isinstance(42, object): {isinstance(42, object)}")
print(f"   isinstance([1, 2, 3], object): {isinstance([1, 2, 3], object)}")

print("\n" + "=" * 80)
print("\n4. Advanced type checking examples:")

print("\n   Checking multiple types at once:")
print(f"   isinstance(b1, (Book, Newspaper, Magazine)): {isinstance(b1, (Book, Newspaper, Magazine))}")
print(f"   isinstance(n1, (Book, Newspaper, Magazine)): {isinstance(n1, (Book, Newspaper, Magazine))}")
print(f"   isinstance(m1, (Book, Newspaper, Magazine)): {isinstance(m1, (Book, Newspaper, Magazine))}")

print("\n   Type checking with inheritance:")

class EBook(Book):
    def __init__(self, title, file_format):
        super().__init__(title)
        self.file_format = file_format


class AudioBook(Book):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration


print("\n   Creating inherited book types:")
ebook1 = EBook("Digital Fortress", "PDF")
audiobook1 = AudioBook("Harry Potter Audiobook", 8.5)

print(f"   isinstance(ebook1, EBook): {isinstance(ebook1, EBook)}")
print(f"   isinstance(ebook1, Book): {isinstance(ebook1, Book)}")
print(f"   isinstance(audiobook1, AudioBook): {isinstance(audiobook1, AudioBook)}")
print(f"   isinstance(audiobook1, Book): {isinstance(audiobook1, Book)}")
print(f"   isinstance(b1, EBook): {isinstance(b1, EBook)}")
print(f"   isinstance(b1, AudioBook): {isinstance(b1, AudioBook)}")

print("\n   Checking with multiple parent classes:")
print(f"   isinstance(ebook1, (Book, Newspaper)): {isinstance(ebook1, (Book, Newspaper))}")

print("\n" + "=" * 80)
print("\n5. Practical examples of type checking:")

class Library:
    def __init__(self, name):
        self.name = name
        self.collection = []
    
    def add_item(self, item):
        """Add an item to the library collection"""
        if isinstance(item, (Book, EBook, AudioBook)):
            self.collection.append(item)
            return f'Added book: "{item.title}"'
        elif isinstance(item, Newspaper):
            self.collection.append(item)
            return f'Added newspaper: "{item.name}"'
        elif isinstance(item, Magazine):
            self.collection.append(item)
            return f'Added magazine: "{item.name}"'
        else:
            return f"Cannot add item of type {type(item).__name__}"
    
    def list_books(self):
        """List only books in the collection"""
        books = [item for item in self.collection if isinstance(item, (Book, EBook, AudioBook))]
        if not books:
            return "No books in collection"
        
        result = f"Books in {self.name}:\n"
        for i, book in enumerate(books, 1):
            result += f"  {i}. {book.title}"
            if isinstance(book, EBook):
                result += f" (EBook - {book.file_format})"
            elif isinstance(book, AudioBook):
                result += f" (AudioBook - {book.duration} hours)"
            result += "\n"
        return result
    
    def list_periodicals(self):
        """List newspapers and magazines"""
        periodicals = [item for item in self.collection if isinstance(item, (Newspaper, Magazine))]
        if not periodicals:
            return "No periodicals in collection"
        
        result = f"Periodicals in {self.name}:\n"
        for i, item in enumerate(periodicals, 1):
            item_type = "Newspaper" if isinstance(item, Newspaper) else "Magazine"
            result += f"  {i}. [{item_type}] {item.name}\n"
        return result

print("\n   Creating a library and adding items:")
my_library = Library("City Library")

print("\n   Adding various items:")
items_to_add = [b1, b2, n1, n2, m1, m2, ebook1, audiobook1]
for item in items_to_add:
    print(f"   {my_library.add_item(item)}")

print("\n   Trying to add non-library item:")
try:
    print(f"   {my_library.add_item('Not a library item')}")
except Exception as e:
    print(f"   {e}")

print("\n   Listing books:")
print(my_library.list_books())

print("\n   Listing periodicals:")
print(my_library.list_periodicals())

print("\n" + "=" * 80)
print("\n6. Type checking in functions:")

def process_publication(pub):
    """Process different types of publications"""
    if isinstance(pub, Book):
        print(f"   Processing book: {pub.title}")
        if isinstance(pub, EBook):
            print(f"     File format: {pub.file_format}")
        elif isinstance(pub, AudioBook):
            print(f"     Duration: {pub.duration} hours")
    elif isinstance(pub, Newspaper):
        print(f"   Processing newspaper: {pub.name}")
    elif isinstance(pub, Magazine):
        print(f"   Processing magazine: {pub.name}")
    else:
        print(f"   Unknown publication type: {type(pub).__name__}")

print("\n   Processing different publications:")
print("   " + "-" * 40)
for item in items_to_add:
    process_publication(item)
    print("   " + "-" * 40)

print("\n" + "=" * 80)
print("\n7. Comparing type() and isinstance():")

print("\n   Key differences:")
print("   • type() returns the exact class of an object")
print("   • isinstance() checks if object is instance of class or subclass")
print("   • isinstance() works with inheritance hierarchy")
print("   • type() is stricter about exact type matching")

print("\n   Demonstration:")
print(f"   type(ebook1) == Book: {type(ebook1) == Book}")
print(f"   isinstance(ebook1, Book): {isinstance(ebook1, Book)}")

print(f"\n   type(ebook1): {type(ebook1)}")
print(f"   type(ebook1).__name__: {type(ebook1).__name__}")

print("\n   Inheritance chain:")
print(f"   issubclass(EBook, Book): {issubclass(EBook, Book)}")
print(f"   issubclass(AudioBook, Book): {issubclass(AudioBook, Book)}")
print(f"   issubclass(Book, object): {issubclass(Book, object)}")
print(f"   issubclass(Newspaper, object): {issubclass(Newspaper, object)}")

print("\n" + "=" * 80)
print("\n8. Type checking with built-in types:")

print("\n   Checking built-in types:")
data_samples = [
    "Hello World",      # str
    42,                 # int
    3.14159,            # float
    True,               # bool
    [1, 2, 3],          # list
    (1, 2, 3),          # tuple
    {"key": "value"},   # dict
    {1, 2, 3},          # set
    None                # NoneType
]

print("   Type checking built-in objects:")
for item in data_samples:
    print(f"   {repr(item):20} -> type: {type(item).__name__:10} isinstance(item, object): {isinstance(item, object)}")

print("\n   Multiple type checking:")
mixed_list = [b1, n1, "string", 42, [1, 2], ebook1]
print("\n   Processing mixed list:")
for item in mixed_list:
    if isinstance(item, (Book, EBook, AudioBook)):
        print(f"   Book: {getattr(item, 'title', 'Unknown title')}")
    elif isinstance(item, Newspaper):
        print(f"   Newspaper: {item.name}")
    elif isinstance(item, str):
        print(f"   String: {item}")
    elif isinstance(item, int):
        print(f"   Integer: {item}")
    elif isinstance(item, list):
        print(f"   List: {item}")
    else:
        print(f"   Other: {type(item).__name__}")

print("\n" + "=" * 80)
print("\n9. Testing the original requirements:")

print("\n   Original example recreation:")
orig_b1 = Book("The Catcher In The Rye")
orig_b2 = Book("The Grapes of Wrath")
orig_n1 = Newspaper("The Washington Post")
orig_n2 = Newspaper("The New York Times")

print(f"\n   type(orig_b1): {type(orig_b1)}")
print(f"   type(orig_n1): {type(orig_n1)}")

print(f"\n   type(orig_b1) == type(orig_b2): {type(orig_b1) == type(orig_b2)}")
print(f"   type(orig_b1) == type(orig_n2): {type(orig_b1) == type(orig_n2)}")

print(f"\n   isinstance(orig_b1, Book): {isinstance(orig_b1, Book)}")
print(f"   isinstance(orig_n1, Newspaper): {isinstance(orig_n1, Newspaper)}")
print(f"   isinstance(orig_n2, Book): {isinstance(orig_n2, Book)}")
print(f"   isinstance(orig_n2, object): {isinstance(orig_n2, object)}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ type() returns the exact class of an object")
print("✓ isinstance() checks if object is instance of class (including subclasses)")
print("✓ All Python objects inherit from 'object' base class")
print("✓ isinstance() accepts tuple of types for multiple checks")
print("✓ Type checking enables polymorphism and runtime decisions")
print("✓ Useful for validating inputs and handling different object types")
print("✓ issubclass() checks class inheritance relationships")