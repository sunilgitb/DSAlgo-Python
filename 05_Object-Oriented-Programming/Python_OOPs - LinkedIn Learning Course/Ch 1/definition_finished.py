# Python Object Oriented Programming
# Basic class definitions

class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title):
        self.title = title


# Create instances of the class
book1 = Book("Brave New World")
book2 = Book("War and Peace")

# Print the class and property
print(book1)
print(book1.title)

print("\n" + "=" * 60)
print("Exploring Basic Python Classes:")
print("=" * 60)

print("\n1. Basic class instantiation and attribute access:")
print(f"   book1 = Book('Brave New World')")
print(f"   book2 = Book('War and Peace')")

print(f"\n   book1 object: {book1}")
print(f"   book1.title: {book1.title}")
print(f"   book2.title: {book2.title}")

print("\n" + "=" * 60)
print("\n2. Adding more functionality to the Book class:")

class EnhancedBook:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
    
    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.year})'
    
    def __repr__(self):
        return f'EnhancedBook("{self.title}", "{self.author}", {self.year})'
    
    def check_out(self):
        if self.is_available:
            self.is_available = False
            return f'"{self.title}" has been checked out.'
        else:
            return f'"{self.title}" is already checked out.'
    
    def check_in(self):
        if not self.is_available:
            self.is_available = True
            return f'"{self.title}" has been checked in.'
        else:
            return f'"{self.title}" was already available.'

print("\n   Creating EnhancedBook instances:")
book3 = EnhancedBook("To Kill a Mockingbird", "Harper Lee", 1960)
book4 = EnhancedBook("1984", "George Orwell", 1949)
book5 = EnhancedBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print(f"\n   Using __str__ method (print):")
print(f"   {book3}")
print(f"   {book4}")
print(f"   {book5}")

print(f"\n   Using __repr__ method (representation):")
print(f"   repr(book3): {repr(book3)}")
print(f"   repr(book4): {repr(book4)}")

print("\n" + "=" * 60)
print("\n3. Working with book instances:")

print("\n   Checking out books:")
print(f"   {book3.check_out()}")
print(f"   {book3.check_out()}")  # Try to check out again
print(f"   {book4.check_out()}")

print(f"\n   Checking in books:")
print(f"   {book3.check_in()}")
print(f"   {book3.check_in()}")  # Try to check in again

print("\n" + "=" * 60)
print("\n4. Class attributes and instance attributes:")

class LibraryBook:
    # Class attribute - shared by all instances
    total_books = 0
    library_name = "City Central Library"
    
    def __init__(self, title, author):
        # Instance attributes - unique to each instance
        self.title = title
        self.author = author
        self.id = LibraryBook.total_books + 1
        
        # Increment class attribute
        LibraryBook.total_books += 1
    
    @classmethod
    def get_library_info(cls):
        return f"{cls.library_name} - Total books: {cls.total_books}"
    
    def __str__(self):
        return f"#{self.id}: {self.title} by {self.author}"

print("\n   Creating LibraryBook instances:")
lib_book1 = LibraryBook("Pride and Prejudice", "Jane Austen")
lib_book2 = LibraryBook("Moby Dick", "Herman Melville")
lib_book3 = LibraryBook("The Hobbit", "J.R.R. Tolkien")

print(f"\n   Instance details:")
print(f"   {lib_book1}")
print(f"   {lib_book2}")
print(f"   {lib_book3}")

print(f"\n   Class information:")
print(f"   LibraryBook.total_books: {LibraryBook.total_books}")
print(f"   LibraryBook.get_library_info(): {LibraryBook.get_library_info()}")

print("\n" + "=" * 60)
print("\n5. Inheritance - Creating specialized book classes:")

class EBook(EnhancedBook):
    def __init__(self, title, author, year, file_size, format_type):
        super().__init__(title, author, year)
        self.file_size = file_size  # in MB
        self.format_type = format_type
        self.download_count = 0
    
    def download(self):
        self.download_count += 1
        return f'Downloaded "{self.title}" ({self.file_size}MB {self.format_type}). Total downloads: {self.download_count}'
    
    def __str__(self):
        return f'{super().__str__()} [{self.format_type}, {self.file_size}MB]'

class AudioBook(EnhancedBook):
    def __init__(self, title, author, year, duration, narrator):
        super().__init__(title, author, year)
        self.duration = duration  # in hours
        self.narrator = narrator
    
    def __str__(self):
        return f'{super().__str__()} - Narrated by {self.narrator} ({self.duration} hours)'

print("\n   Creating specialized book types:")
ebook1 = EBook("Digital Fortress", "Dan Brown", 1998, 2.5, "PDF")
audiobook1 = AudioBook("Harry Potter", "J.K. Rowling", 1997, 8.5, "Jim Dale")

print(f"\n   EBook: {ebook1}")
print(f"   AudioBook: {audiobook1}")

print(f"\n   Using specialized methods:")
print(f"   {ebook1.download()}")
print(f"   {ebook1.download()}")

print("\n" + "=" * 60)
print("\n6. Practical example - Simple Library System:")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        return f'Added "{book.title}" to {self.name}'
    
    def list_books(self):
        if not self.books:
            return f"{self.name} has no books."
        
        result = f"Books in {self.name}:\n"
        for i, book in enumerate(self.books, 1):
            result += f"  {i}. {book}\n"
        return result
    
    def find_books_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if not found_books:
            return f"No books by {author} found in {self.name}"
        
        result = f"Books by {author} in {self.name}:\n"
        for i, book in enumerate(found_books, 1):
            result += f"  {i}. {book.title} ({book.year})\n"
        return result

print("\n   Creating a library and adding books:")
my_library = Library("My Personal Library")

# Add some books
books_to_add = [
    EnhancedBook("To Kill a Mockingbird", "Harper Lee", 1960),
    EnhancedBook("1984", "George Orwell", 1949),
    EnhancedBook("Animal Farm", "George Orwell", 1945),
    EnhancedBook("The Catcher in the Rye", "J.D. Salinger", 1951),
]

for book in books_to_add:
    print(f"   {my_library.add_book(book)}")

print(f"\n   {my_library.list_books()}")
print(f"\n   {my_library.find_books_by_author('George Orwell')}")
print(f"\n   {my_library.find_books_by_author('J.K. Rowling')}")

print("\n" + "=" * 60)
print("\n7. Testing the original Book class from the example:")

print("\n   Original Book class demonstration:")
print(f"   book1 object reference: {book1}")
print(f"   book1 memory address: {hex(id(book1))}")
print(f"   book1.title attribute: {book1.title}")

print(f"\n   book2 object reference: {book2}")
print(f"   book2 memory address: {hex(id(book2))}")
print(f"   book2.title attribute: {book2.title}")

print("\n   Modifying book titles:")
book1.title = "Brave New World - Updated Edition"
book2.title = "War and Peace - Abridged Version"
print(f"   Updated book1.title: {book1.title}")
print(f"   Updated book2.title: {book2.title}")

print("\n" + "=" * 60)
print("\nSummary of Basic Class Concepts:")
print("✓ __init__() initializes new instances")
print("✓ self refers to the instance being created")
print("✓ Attributes store data specific to each instance")
print("✓ Methods define behavior of instances")
print("✓ __str__() provides readable string representation")
print("✓ __repr__() provides unambiguous representation")
print("✓ Classes can inherit from other classes")
print("✓ Class attributes are shared across all instances")
print("✓ Instance attributes are unique to each instance")
print("✓ OOP enables modeling real-world entities effectively")