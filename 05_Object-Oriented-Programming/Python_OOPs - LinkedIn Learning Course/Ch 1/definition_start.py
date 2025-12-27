# Python Object Oriented Programming
# Basic class definitions

# Create a basic class
class Book:
    """A simple Book class to demonstrate basic OOP concepts."""
    
    # Class attribute - shared by all instances
    library_name = "City Central Library"
    
    def __init__(self, title, author, year):
        """
        Initialize a new Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year
        """
        # Instance attributes - unique to each instance
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
    
    def check_out(self):
        """Mark the book as checked out if available."""
        if self.is_available:
            self.is_available = False
            return f'"{self.title}" has been checked out.'
        else:
            return f'"{self.title}" is already checked out.'
    
    def check_in(self):
        """Mark the book as checked in if it was checked out."""
        if not self.is_available:
            self.is_available = True
            return f'"{self.title}" has been checked in.'
        else:
            return f'"{self.title}" was already available.'
    
    def get_age(self):
        """Calculate how old the book is (assuming current year is 2024)."""
        current_year = 2024
        return current_year - self.year
    
    def __str__(self):
        """Return a human-readable string representation."""
        status = "Available" if self.is_available else "Checked Out"
        return f'"{self.title}" by {self.author} ({self.year}) - {status}'
    
    def __repr__(self):
        """Return an unambiguous string representation."""
        return f'Book("{self.title}", "{self.author}", {self.year})'


# Create instances of the class
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print("Basic Class Demonstration:")
print("=" * 80)

print("\n1. Class attribute (shared by all instances):")
print(f"   Book.library_name: {Book.library_name}")
print(f"   book1.library_name: {book1.library_name}")
print(f"   book2.library_name: {book2.library_name}")

print("\n2. Instance attributes (unique to each instance):")
print(f"   book1.title: {book1.title}")
print(f"   book1.author: {book1.author}")
print(f"   book1.year: {book1.year}")

print(f"\n   book2.title: {book2.title}")
print(f"   book2.author: {book2.author}")
print(f"   book2.year: {book2.year}")

print(f"\n   book3.title: {book3.title}")
print(f"   book3.author: {book3.author}")
print(f"   book3.year: {book3.year}")

print("\n3. Using __str__ method (human-readable):")
print(f"   str(book1): {book1}")
print(f"   str(book2): {book2}")
print(f"   str(book3): {book3}")

print("\n4. Using __repr__ method (unambiguous representation):")
print(f"   repr(book1): {repr(book1)}")
print(f"   repr(book2): {repr(book2)}")
print(f"   repr(book3): {repr(book3)}")

print("\n5. Calling instance methods:")
print(f"   book1.check_out(): {book1.check_out()}")
print(f"   book1.check_out() again: {book1.check_out()}")
print(f"   book1.check_in(): {book1.check_in()}")
print(f"   book1.check_in() again: {book1.check_in()}")

print(f"\n   book2.check_out(): {book2.check_out()}")
print(f"   book3.check_out(): {book3.check_out()}")

print("\n6. Current status after operations:")
print(f"   {book1}")
print(f"   {book2}")
print(f"   {book3}")

print("\n7. Additional method - get_age():")
print(f"   book1.get_age(): {book1.get_age()} years old")
print(f"   book2.get_age(): {book2.get_age()} years old")
print(f"   book3.get_age(): {book3.get_age()} years old")

print("\n" + "=" * 80)
print("\nAdvanced Class Features:")

print("\n8. Class inheritance - Creating specialized book types:")

class EBook(Book):
    """A specialized Book class for electronic books."""
    
    def __init__(self, title, author, year, file_size, format_type):
        """
        Initialize an EBook.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year
            file_size (float): File size in MB
            format_type (str): Format (PDF, EPUB, etc.)
        """
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format_type = format_type
        self.download_count = 0
    
    def download(self):
        """Simulate downloading the ebook."""
        self.download_count += 1
        return f'Downloaded "{self.title}" ({self.file_size}MB {self.format_type}). Total downloads: {self.download_count}'
    
    def __str__(self):
        """Enhanced string representation for ebooks."""
        base_str = super().__str__()
        return f"{base_str} [{self.format_type}, {self.file_size}MB, Downloads: {self.download_count}]"


class AudioBook(Book):
    """A specialized Book class for audio books."""
    
    def __init__(self, title, author, year, duration, narrator):
        """
        Initialize an AudioBook.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year
            duration (float): Duration in hours
            narrator (str): Narrator's name
        """
        super().__init__(title, author, year)
        self.duration = duration
        self.narrator = narrator
    
    def play(self):
        """Simulate playing the audiobook."""
        return f'Now playing "{self.title}" narrated by {self.narrator} ({self.duration} hours)'
    
    def __str__(self):
        """Enhanced string representation for audiobooks."""
        base_str = super().__str__()
        return f"{base_str} - Narrated by {self.narrator} ({self.duration} hours)"

print("\n   Creating specialized book instances:")
ebook1 = EBook("Digital Fortress", "Dan Brown", 1998, 2.5, "PDF")
audiobook1 = AudioBook("Harry Potter", "J.K. Rowling", 1997, 8.5, "Jim Dale")

print(f"   EBook: {ebook1}")
print(f"   AudioBook: {audiobook1}")

print(f"\n   Using specialized methods:")
print(f"   {ebook1.download()}")
print(f"   {ebook1.download()}")
print(f"   {audiobook1.play()}")

print("\n9. Type checking and inheritance:")
print(f"   isinstance(ebook1, EBook): {isinstance(ebook1, EBook)}")
print(f"   isinstance(ebook1, Book): {isinstance(ebook1, Book)}")
print(f"   isinstance(audiobook1, AudioBook): {isinstance(audiobook1, AudioBook)}")
print(f"   isinstance(audiobook1, Book): {isinstance(audiobook1, Book)}")

print("\n10. Method Resolution Order (MRO):")
print("   EBook.__mro__:", EBook.__mro__)
print("   AudioBook.__mro__:", AudioBook.__mro__)

print("\n" + "=" * 80)
print("\nPractical Example - Library Management:")

class Library:
    """A simple library management system."""
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        return f'Added "{book.title}" to {self.name}'
    
    def list_books(self):
        """List all books in the library."""
        if not self.books:
            return f"{self.name} has no books."
        
        result = f"Books in {self.name}:\n"
        for i, book in enumerate(self.books, 1):
            result += f"  {i}. {book}\n"
        return result
    
    def find_books_by_author(self, author_name):
        """Find books by a specific author."""
        found_books = [book for book in self.books if author_name.lower() in book.author.lower()]
        
        if not found_books:
            return f"No books found by authors containing '{author_name}'"
        
        result = f"Books by authors containing '{author_name}':\n"
        for i, book in enumerate(found_books, 1):
            result += f"  {i}. {book.title} by {book.author}\n"
        return result
    
    def check_out_book(self, book_title):
        """Check out a book by title."""
        for book in self.books:
            if book.title.lower() == book_title.lower():
                return book.check_out()
        return f'Book "{book_title}" not found in {self.name}'

print("\n   Creating a library:")
my_library = Library("City Public Library")

print("\n   Adding books to library:")
books_to_add = [
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949),
    Book("Animal Farm", "George Orwell", 1945),
    EBook("The Da Vinci Code", "Dan Brown", 2003, 3.2, "EPUB"),
    AudioBook("The Hobbit", "J.R.R. Tolkien", 1937, 11.5, "Rob Inglis"),
]

for book in books_to_add:
    print(f"   {my_library.add_book(book)}")

print(f"\n   {my_library.list_books()}")

print("\n   Finding books by author 'Orwell':")
print(my_library.find_books_by_author("Orwell"))

print("\n   Finding books by author 'Brown':")
print(my_library.find_books_by_author("Brown"))

print("\n   Checking out books:")
print(f"   {my_library.check_out_book('1984')}")
print(f"   {my_library.check_out_book('1984')}")  # Try again
print(f"   {my_library.check_out_book('Unknown Book')}")

print(f"\n   Library status after operations:")
print(my_library.list_books())

print("\n" + "=" * 80)
print("\nSummary of Basic Class Concepts:")
print("✓ Classes define blueprints for objects")
print("✓ __init__() initializes instance attributes")
print("✓ Methods define object behavior")
print("✓ self refers to the instance itself")
print("✓ Class attributes are shared across instances")
print("✓ Instance attributes are unique to each instance")
print("✓ __str__() provides human-readable representation")
print("✓ __repr__() provides unambiguous representation")
print("✓ Inheritance allows creating specialized classes")
print("✓ isinstance() checks object types")
print("✓ Classes enable code organization and reuse")