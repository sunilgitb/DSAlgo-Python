# Python Object Oriented Programming
# Checking class types and instances

class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

print("Testing Type and Instance Checking:")
print("=" * 80)

# TODO: use type() to inspect the object type
print("1. Using type() to inspect object types:")
print(f"   type(b1): {type(b1)}")
print(f"   type(n1): {type(n1)}")

print("\n2. Getting type names:")
print(f"   type(b1).__name__: {type(b1).__name__}")
print(f"   type(n1).__name__: {type(n1).__name__}")

print("\n" + "=" * 80)

# TODO: compare two types together
print("3. Comparing types together:")
print(f"   type(b1) == type(b2): {type(b1) == type(b2)}")
print(f"   type(b1) == type(n1): {type(b1) == type(n1)}")

print("\n   More comparisons:")
print(f"   type(n1) == type(n2): {type(n1) == type(n2)}")
print(f"   type(b2) == type(n2): {type(b2) == type(n2)}")

print("\n" + "=" * 80)

# TODO: use isinstance to compare a specific instance to a known type
print("4. Using isinstance() to check instances:")
print(f"   isinstance(b1, Book): {isinstance(b1, Book)}")
print(f"   isinstance(n1, Newspaper): {isinstance(n1, Newspaper)}")
print(f"   isinstance(n2, Book): {isinstance(n2, Book)}")
print(f"   isinstance(b2, object): {isinstance(b2, object)}")

print("\n   Additional isinstance checks:")
print(f"   isinstance(b2, Book): {isinstance(b2, Book)}")
print(f"   isinstance(n2, Newspaper): {isinstance(n2, Newspaper)}")
print(f"   isinstance(n1, object): {isinstance(n1, object)}")

print("\n" + "=" * 80)
print("\n5. Advanced examples with inheritance:")

print("\n   Creating inherited classes:")

class EBook(Book):
    def __init__(self, title, file_format):
        super().__init__(title)
        self.file_format = file_format


class Magazine(Newspaper):
    def __init__(self, name, frequency):
        super().__init__(name)
        self.frequency = frequency


print("\n   Creating instances of inherited classes:")
ebook1 = EBook("Digital Fortress", "PDF")
magazine1 = Magazine("Time Magazine", "Weekly")

print(f"   isinstance(ebook1, Book): {isinstance(ebook1, Book)}")
print(f"   isinstance(ebook1, EBook): {isinstance(ebook1, EBook)}")
print(f"   isinstance(magazine1, Newspaper): {isinstance(magazine1, Newspaper)}")
print(f"   isinstance(magazine1, Magazine): {isinstance(magazine1, Magazine)}")

print(f"\n   type() comparison with inheritance:")
print(f"   type(ebook1) == Book: {type(ebook1) == Book}")
print(f"   type(ebook1) == EBook: {type(ebook1) == EBook}")

print("\n" + "=" * 80)
print("\n6. Practical type checking example:")

class Library:
    def __init__(self):
        self.collection = []
    
    def add_item(self, item):
        """Add item to library with type checking"""
        if isinstance(item, Book):
            self.collection.append(item)
            return f'Added book: "{item.title}"'
        elif isinstance(item, Newspaper):
            self.collection.append(item)
            return f'Added newspaper: "{item.name}"'
        else:
            return f"Cannot add item of type {type(item).__name__}"
    
    def list_books(self):
        """List only books in collection"""
        books = [item for item in self.collection if isinstance(item, Book)]
        if not books:
            return "No books in collection"
        
        result = "Books in library:\n"
        for i, book in enumerate(books, 1):
            book_type = "EBook" if isinstance(book, EBook) else "Book"
            result += f"  {i}. [{book_type}] {book.title}\n"
        return result
    
    def list_newspapers(self):
        """List only newspapers in collection"""
        newspapers = [item for item in self.collection if isinstance(item, Newspaper)]
        if not newspapers:
            return "No newspapers in collection"
        
        result = "Newspapers in library:\n"
        for i, paper in enumerate(newspapers, 1):
            paper_type = "Magazine" if isinstance(paper, Magazine) else "Newspaper"
            result += f"  {i}. [{paper_type}] {paper.name}\n"
        return result

print("\n   Creating a library and adding items:")
my_library = Library()

print("\n   Adding items to library:")
items_to_add = [b1, b2, n1, n2, ebook1, magazine1]
for item in items_to_add:
    print(f"   {my_library.add_item(item)}")

print("\n   Listing books:")
print(my_library.list_books())

print("\n   Listing newspapers:")
print(my_library.list_newspapers())

print("\n" + "=" * 80)
print("\n7. Type checking with multiple types:")

print("\n   Using tuple of types with isinstance:")
print(f"   isinstance(b1, (Book, Newspaper)): {isinstance(b1, (Book, Newspaper))}")
print(f"   isinstance(n1, (Book, Newspaper)): {isinstance(n1, (Book, Newspaper))}")
print(f"   isinstance(ebook1, (Book, Newspaper)): {isinstance(ebook1, (Book, Newspaper))}")

print("\n   Processing different item types:")
def process_item(item):
    if isinstance(item, Book):
        if isinstance(item, EBook):
            return f"EBook: {item.title} ({item.file_format})"
        else:
            return f"Book: {item.title}"
    elif isinstance(item, Newspaper):
        if isinstance(item, Magazine):
            return f"Magazine: {item.name} ({item.frequency})"
        else:
            return f"Newspaper: {item.name}"
    else:
        return f"Unknown item: {type(item).__name__}"

print("\n   Processing each item:")
for item in items_to_add:
    print(f"   {process_item(item)}")

print("\n" + "=" * 80)
print("\n8. Checking the original requirements:")

print("\n   Original example complete output:")
print("   " + "=" * 40)

print(f"\n   type(b1)")
print(f"   {type(b1)}")

print(f"\n   type(n1)")
print(f"   {type(n1)}")

print(f"\n   type(b1) == type(b2)")
print(f"   {type(b1) == type(b2)}")

print(f"\n   type(b1) == type(n2)")
print(f"   {type(b1) == type(n2)}")

print(f"\n   isinstance(b1, Book)")
print(f"   {isinstance(b1, Book)}")

print(f"\n   isinstance(n1, Newspaper)")
print(f"   {isinstance(n1, Newspaper)}")

print(f"\n   isinstance(n2, Book)")
print(f"   {isinstance(n2, Book)}")

print(f"\n   isinstance(n2, object)")
print(f"   {isinstance(n2, object)}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ type() returns the exact class of an object")
print("✓ isinstance() checks if object is instance of a class (including subclasses)")
print("✓ All Python objects inherit from 'object' base class")
print("✓ isinstance() can check multiple types using a tuple")
print("✓ Type checking enables runtime polymorphism")
print("✓ Useful for data validation and handling different object types")