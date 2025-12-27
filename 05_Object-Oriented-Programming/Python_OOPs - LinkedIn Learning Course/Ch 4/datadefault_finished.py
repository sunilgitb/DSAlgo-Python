# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field, fields
import random
from typing import List, Optional, ClassVar
from datetime import datetime


def price_func():
    """Function to generate a random price between 20 and 40."""
    return float(random.randrange(20, 40))


def generate_isbn():
    """Generate a fake ISBN number."""
    return f"978-{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"


def default_tags():
    """Default factory for tags list."""
    return ["unclassified"]


@dataclass
class Book:
    # Class variable (not an instance field)
    BOOK_TYPES: ClassVar[List[str]] = ["Fiction", "Non-Fiction", "Poetry", "Drama"]
    
    # Different ways to define default values:
    
    # 1. Simple default value
    title: str = "No Title"
    
    # 2. Another simple default
    author: str = "No Author"
    
    # 3. Integer default
    pages: int = 0
    
    # 4. Using field() with default_factory for dynamic defaults
    price: float = field(default_factory=price_func)
    
    # 5. Optional field with None default
    genre: Optional[str] = None
    
    # 6. List with default_factory (avoids mutable default problem)
    tags: List[str] = field(default_factory=default_tags)
    
    # 7. Field with default_factory for complex generation
    isbn: str = field(default_factory=generate_isbn)
    
    # 8. Field that's excluded from __repr__
    internal_id: int = field(default=0, repr=False)
    
    # 9. Field that's excluded from comparisons
    last_updated: datetime = field(default_factory=datetime.now, compare=False)
    
    # 10. Field with metadata
    rating: float = field(default=0.0, metadata={"min": 0.0, "max": 5.0, "description": "User rating"})
    
    def __post_init__(self):
        """Initialize computed fields after regular initialization."""
        if self.internal_id == 0:
            self.internal_id = id(self) % 1000000  # Simple ID based on object ID
    
    # Method using default values
    def book_info(self):
        genre_info = f" ({self.genre})" if self.genre else ""
        return f"'{self.title}' by {self.author}{genre_info} - {self.pages} pages, ${self.price:.2f}"


# Example with inheritance and defaults
@dataclass
class EBook(Book):
    # Additional fields for EBook
    file_format: str = "PDF"
    file_size_mb: float = 0.0
    
    # Override parent default
    tags: List[str] = field(default_factory=lambda: ["digital", "ebook"])
    
    def __post_init__(self):
        """Call parent's __post_init__ and add EBook-specific initialization."""
        super().__post_init__()
        # Set default file size based on pages
        if self.file_size_mb == 0.0 and self.pages > 0:
            self.file_size_mb = self.pages * 0.05  # Approx 50KB per page


# Immutable dataclass with defaults
@dataclass(frozen=True)
class ImmutableBook:
    title: str = "Untitled"
    author: str = "Unknown"
    pages: int = 100
    price: float = 19.99


# Driver code
if __name__ == "__main__":
    print("="*80)
    print("DATACLASS DEFAULT VALUES DEMONSTRATION")
    print("="*80)
    
    print("\n1. CREATING INSTANCES WITH DIFFERENT DEFAULT COMBINATIONS")
    print("-"*60)
    
    # Create a completely default book
    print("\na) Completely default book:")
    default_book = Book()
    print(f"   Book() = {default_book}")
    print(f"   Price was randomly generated: ${default_book.price:.2f}")
    print(f"   ISBN was generated: {default_book.isbn}")
    print(f"   Tags: {default_book.tags}")
    
    # Create book with some values provided
    print("\nb) Partial defaults (title and author provided):")
    partial_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    print(f"   Book('The Great Gatsby', 'F. Scott Fitzgerald') = {partial_book}")
    print(f"   Pages defaulted to: {partial_book.pages}")
    print(f"   Price generated: ${partial_book.price:.2f}")
    
    # Create book with all values provided
    print("\nc) All values provided (overrides defaults):")
    custom_book = Book("1984", "George Orwell", 328, 19.95, "Dystopian")
    print(f"   Book('1984', 'George Orwell', 328, 19.95, 'Dystopian') = {custom_book}")
    
    # Create from your example
    print("\nd) Your example books:")
    b1 = Book("War and Peace", "Leo Tolstoy", 1225)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 234)
    print(f"   b1 = {b1}")
    print(f"   b2 = {b2}")
    print(f"   Note: Prices were randomly generated: ${b1.price:.2f} and ${b2.price:.2f}")
    
    print("\n" + "="*80)
    print("2. MUTABLE DEFAULT PATTERNS & PITFALLS")
    print("-"*60)
    
    print("\n⚠️  The Problem with Mutable Defaults:")
    
    @dataclass
    class BadBook:
        """Example of problematic mutable default."""
        title: str
        # ❌ DANGER: Mutable default as direct value
        tags: List[str] = []
    
    @dataclass  
    class GoodBook:
        """Example of correct mutable default handling."""
        title: str
        # ✅ CORRECT: Use default_factory for mutable defaults
        tags: List[str] = field(default_factory=list)
    
    print("\nCreating books with mutable defaults:")
    bad1 = BadBook("Book 1")
    bad2 = BadBook("Book 2")
    
    bad1.tags.append("fiction")
    
    print(f"   BadBook('Book 1').tags.append('fiction')")
    print(f"   bad1.tags: {bad1.tags}")
    print(f"   bad2.tags: {bad2.tags} ← OOPS! This also has 'fiction'!")
    print("   Reason: Both books share the same list instance.")
    
    good1 = GoodBook("Book 1")
    good2 = GoodBook("Book 2")
    
    good1.tags.append("fiction")
    
    print(f"\n   GoodBook('Book 1').tags.append('fiction')")
    print(f"   good1.tags: {good1.tags}")
    print(f"   good2.tags: {good2.tags} ← Correct! This is empty.")
    print("   Reason: Each book gets its own list instance.")
    
    print("\n" + "="*80)
    print("3. FIELD() FUNCTION OPTIONS")
    print("-"*60)
    
    print("\nField parameters demonstrated in Book class:")
    book_fields = fields(Book)
    for f in book_fields:
        print(f"\n   {f.name}:")
        print(f"     Type: {f.type}")
        print(f"     Default: {f.default if f.default is not field.MISSING else 'No default'}")
        print(f"     Default Factory: {f.default_factory if f.default_factory is not field.MISSING else 'No factory'}")
        print(f"     Compare: {f.compare}")
        print(f"     Repr: {f.repr}")
        if f.metadata:
            print(f"     Metadata: {f.metadata}")
    
    print("\n" + "="*80)
    print("4. INHERITANCE WITH DEFAULTS")
    print("-"*60)
    
    print("\nCreating EBook instances (inherits from Book):")
    
    # EBook with all defaults
    ebook_default = EBook()
    print(f"\na) EBook() = {ebook_default}")
    print(f"   File format default: {ebook_default.file_format}")
    print(f"   Tags (overridden): {ebook_default.tags}")
    
    # EBook with custom values
    ebook_custom = EBook(
        title="Digital Python",
        author="Python Expert",
        pages=300,
        genre="Programming"
    )
    print(f"\nb) EBook with custom values = {ebook_custom}")
    print(f"   File size calculated: {ebook_custom.file_size_mb:.1f}MB")
    print(f"   Book info: {ebook_custom.book_info()}")
    
    print("\n" + "="*80)
    print("5. IMMUTABLE DATACLASS WITH DEFAULTS")
    print("-"*60)
    
    immutable1 = ImmutableBook()
    immutable2 = ImmutableBook("Custom Book", "Custom Author", 250, 29.99)
    
    print(f"\na) ImmutableBook() = {immutable1}")
    print(f"b) ImmutableBook('Custom Book', ...) = {immutable2}")
    
    try:
        immutable1.title = "New Title"
    except Exception as e:
        print(f"\n⚠️  Cannot modify: {type(e).__name__} - {e}")
    
    print("\n" + "="*80)
    print("6. REAL-WORLD DEFAULT SCENARIOS")
    print("-"*60)
    
    @dataclass
    class LibraryBook:
        """Real-world example with practical defaults."""
        # Required fields (no defaults)
        title: str
        author: str
        
        # Sensible defaults
        pages: int = 300
        price: float = 24.99
        language: str = "English"
        publication_year: int = field(default_factory=lambda: datetime.now().year)
        
        # System defaults
        date_added: datetime = field(default_factory=datetime.now)
        available: bool = True
        times_borrowed: int = 0
        
        # Computed defaults
        catalog_id: str = field(init=False)
        
        def __post_init__(self):
            """Generate catalog ID."""
            author_initials = ''.join([name[0] for name in self.author.split()])
            year_last_two = str(self.publication_year)[-2:]
            self.catalog_id = f"{author_initials}-{year_last_two}-{self.title[:3].upper()}"
        
        def borrow(self):
            if self.available:
                self.times_borrowed += 1
                self.available = False
                return True
            return False
        
        def return_book(self):
            self.available = True
            return True
    
    print("\nLibrary system with sensible defaults:")
    
    # New book with minimal info
    new_book = LibraryBook("The Hobbit", "J.R.R. Tolkien")
    print(f"\na) New arrival (minimal info):")
    print(f"   {new_book}")
    print(f"   Catalog ID generated: {new_book.catalog_id}")
    print(f"   Added on: {new_book.date_added.strftime('%Y-%m-%d')}")
    
    # Book with full details
    detailed_book = LibraryBook(
        title="Advanced Python",
        author="David Beazley",
        pages=600,
        price=49.99,
        language="English",
        publication_year=2022
    )
    print(f"\nb) Detailed book entry:")
    print(f"   {detailed_book}")
    print(f"   Price per page: ${detailed_book.price/detailed_book.pages:.3f}")
    
    print("\n" + "="*80)
    print("7. DEFAULT VALUE PATTERNS & BEST PRACTICES")
    print("-"*60)
    
    print("""
    Best Practices for Defaults:
    
    1. Use simple defaults for common values:
       title: str = "Untitled"
    
    2. Use None for optional fields:
       subtitle: Optional[str] = None
    
    3. Use field(default_factory=...) for:
       - Mutable defaults (lists, dicts, sets)
       - Dynamic values (current time, random numbers)
       - Complex object creation
    
    4. Avoid mutable direct defaults:
       ❌ tags: List[str] = []  # WRONG
       ✅ tags: List[str] = field(default_factory=list)  # CORRECT
    
    5. Use __post_init__ for computed defaults
    
    6. Consider using ClassVar for class-level constants
    
    7. Document unusual defaults in docstrings
    
    8. Test edge cases with default values
    """)
    
    print("\n" + "="*80)
    print("8. TESTING DIFFERENT CONSTRUCTOR CALLS")
    print("-"*60)
    
    test_cases = [
        ("No arguments", "Book()"),
        ("Title only", "Book('Python Guide')"),
        ("Title and author", "Book('Python Guide', 'Python Expert')"),
        ("Title, author, pages", "Book('Python Guide', 'Python Expert', 400)"),
        ("All fields", "Book('Python Guide', 'Python Expert', 400, 39.99, 'Programming')"),
    ]
    
    print("\nTesting various constructor calls:")
    for description, code in test_cases:
        try:
            result = eval(code)
            print(f"\n{description}:")
            print(f"  {code} = {result}")
            print(f"  Price: ${result.price:.2f}, Tags: {result.tags}")
        except Exception as e:
            print(f"\n{description}:")
            print(f"  {code} raised {type(e).__name__}: {e}")
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    print("""
    Key Takeaways:
    
    1. Dataclasses support multiple default strategies:
       - Simple literals (title="No Title")
       - None for optional fields
       - field(default=value) for explicit control
       - field(default_factory=function) for dynamic defaults
    
    2. Always use default_factory for mutable defaults
       to avoid shared state between instances.
    
    3. Use __post_init__ for computed defaults that
       depend on other fields.
    
    4. Defaults make your API more flexible and
       reduce required arguments for common cases.
    
    5. Consider readability: Too many defaults can
       make code harder to understand.
    
    6. Document your defaults so users know what
       to expect when they don't provide values.
    """)