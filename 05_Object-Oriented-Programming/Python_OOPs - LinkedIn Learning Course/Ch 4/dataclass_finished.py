# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects

from dataclasses import dataclass, field, asdict, astuple
from typing import List, Optional, ClassVar
import json

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
    # Class variable (not in __init__)
    book_count: ClassVar[int] = 0
    # Optional field with default value
    genre: Optional[str] = None
    # Field with default factory
    tags: List[str] = field(default_factory=list)
    # Field with custom configuration
    isbn: str = field(default="Unknown", compare=False, repr=False)
    # Private field (convention only, Python doesn't enforce)
    _discount: float = field(default=0.1, repr=False)
    
    def __post_init__(self):
        """Called after __init__ to perform additional initialization."""
        Book.book_count += 1
        self.book_id = f"BOOK-{Book.book_count:03d}"
    
    # You can define methods in a dataclass like any other
    def bookinfo(self):
        return f"{self.title}, by {self.author}"
    
    def get_discounted_price(self):
        return self.price * (1 - self._discount)
    
    def add_tag(self, tag: str):
        self.tags.append(tag)
        return self
    
    @classmethod
    def get_book_count(cls):
        return cls.book_count
    
    @staticmethod
    def format_price(price: float) -> str:
        return f"${price:.2f}"
    
    # Property example
    @property
    def price_per_page(self) -> float:
        return self.price / self.pages if self.pages > 0 else 0
    
    @property
    def page_count_category(self) -> str:
        if self.pages < 200:
            return "Short"
        elif self.pages < 500:
            return "Medium"
        else:
            return "Long"

# Inheritance example
@dataclass
class EBook(Book):
    file_format: str = "PDF"
    file_size_mb: float = 0.0
    drm_protected: bool = False
    
    def __post_init__(self):
        # Call parent's __post_init__ first
        super().__post_init__()
        # EBook specific initialization
        if self.file_format not in ["PDF", "EPUB", "MOBI"]:
            self.file_format = "PDF"
    
    def bookinfo(self):
        base_info = super().bookinfo()
        return f"{base_info} [{self.file_format}, {self.file_size_mb}MB]"

# Immutable dataclass example
@dataclass(frozen=True)
class ImmutableBook:
    title: str
    author: str
    pages: int
    price: float

# Driver code
if __name__ == "__main__":
    print("="*70)
    print("BASIC DATACLASS CREATION")
    print("="*70)
    
    # create some instances
    b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
    
    print("\n1. Accessing fields directly:")
    print(f"b1.title: {b1.title}")
    print(f"b2.author: {b2.author}")
    print(f"b1.pages: {b1.pages}")
    print(f"b2.price: {b2.price}")
    
    print("\n2. Automatic __repr__:")
    print(f"print(b1): {b1}")
    print(f"print(b2): {b2}")
    
    print("\n" + "="*70)
    print("DATACLASS EQUALITY & COMPARISON")
    print("="*70)
    
    b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
    b4 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95, isbn="123-456")
    
    print("\n1. Equality comparison (compares all fields by default):")
    print(f"b1 == b3 (identical data): {b1 == b3}")
    print(f"b1 == b2 (different data): {b1 == b2}")
    print(f"b1 == b4 (different ISBN but compare=False): {b1 == b4}")
    
    print("\n2. Automatic __eq__, __ne__, __hash__:")
    print(f"b1 != b2: {b1 != b2}")
    
    # Using in sets (requires __hash__)
    book_set = {b1, b2, b3}
    print(f"\nSet of books (b1 and b3 are equal): {len(book_set)} unique books")
    
    print("\n" + "="*70)
    print("DATACLASS WITH DEFAULT VALUES")
    print("="*70)
    
    b5 = Book("1984", "George Orwell", 328, 19.95, genre="Dystopian")
    b6 = Book("Brave New World", "Aldous Huxley", 311, 18.95, 
              genre="Science Fiction", tags=["dystopian", "classic"])
    
    print("\nBooks with optional fields and defaults:")
    print(f"b5: {b5}")
    print(f"b5.genre: {b5.genre}")
    print(f"b5.tags: {b5.tags}")
    print(f"b5.isbn: {b5.isbn}")  # repr=False, but we can still access it
    
    print(f"\nb6: {b6}")
    print(f"b6.tags: {b6.tags}")
    
    print("\n" + "="*70)
    print("DATACLASS METHODS & PROPERTIES")
    print("="*70)
    
    print("\n1. Regular methods:")
    print(f"b1.bookinfo(): {b1.bookinfo()}")
    print(f"b2.bookinfo(): {b2.bookinfo()}")
    
    print("\n2. Discounted price (using private field):")
    print(f"b1.get_discounted_price(): ${b1.get_discounted_price():.2f}")
    
    print("\n3. Properties:")
    print(f"b1.price_per_page: ${b1.price_per_page:.4f}")
    print(f"b2.price_per_page: ${b2.price_per_page:.4f}")
    print(f"b1.page_count_category: {b1.page_count_category}")
    print(f"b2.page_count_category: {b2.page_count_category}")
    
    print("\n4. Class and static methods:")
    print(f"Book.get_book_count(): {Book.get_book_count()}")
    print(f"Book.format_price(25.5): {Book.format_price(25.5)}")
    
    print("\n" + "="*70)
    print("MUTABILITY & FIELD MODIFICATION")
    print("="*70)
    
    print("Before modification:")
    print(f"b1: {b1}")
    
    # Dataclasses are mutable by default
    b1.title = "Anna Karenina"
    b1.pages = 864
    b1.add_tag("classic").add_tag("russian")
    
    print("\nAfter modification:")
    print(f"b1: {b1}")
    print(f"b1.tags: {b1.tags}")
    
    print("\n" + "="*70)
    print("IMMUTABLE DATACLASS EXAMPLE")
    print("="*70)
    
    ib1 = ImmutableBook("The Great Gatsby", "F. Scott Fitzgerald", 218, 15.95)
    print(f"ImmutableBook: {ib1}")
    
    try:
        ib1.title = "New Title"  # This will raise an error
    except Exception as e:
        print(f"Cannot modify frozen dataclass: {type(e).__name__}")
    
    print("\n" + "="*70)
    print("INHERITANCE WITH DATACLASSES")
    print("="*70)
    
    ebook1 = EBook("Digital Python", "Python Author", 300, 24.99,
                   file_format="EPUB", file_size_mb=2.5)
    ebook2 = EBook("Kindle Cookbook", "Chef Author", 150, 12.99,
                   genre="Cookbook", drm_protected=True)
    
    print(f"ebook1: {ebook1}")
    print(f"ebook1.bookinfo(): {ebook1.bookinfo()}")
    print(f"ebook1.file_format: {ebook1.file_format}")
    
    print(f"\nebook2: {ebook2}")
    print(f"ebook2.drm_protected: {ebook2.drm_protected}")
    
    print("\n" + "="*70)
    print("DATACLASS UTILITY FUNCTIONS")
    print("="*70)
    
    print("\n1. asdict() - Convert to dictionary:")
    b1_dict = asdict(b1)
    print(f"asdict(b1): {json.dumps(b1_dict, indent=2)}")
    
    print("\n2. astuple() - Convert to tuple:")
    b1_tuple = astuple(b1)
    print(f"astuple(b1): {b1_tuple}")
    
    print("\n3. replace() - Create modified copy:")
    from dataclasses import replace
    b1_cheaper = replace(b1, price=34.95, genre="Classic Literature")
    print(f"Original: {b1}")
    print(f"Modified copy: {b1_cheaper}")
    
    print("\n4. fields() - Get field information:")
    from dataclasses import fields
    print("Book fields:")
    for f in fields(Book):
        print(f"  {f.name}: {f.type} (default={f.default}, "
              f"compare={f.compare}, repr={f.repr})")
    
    print("\n" + "="*70)
    print("DATACLASS ORDERING")
    print("="*70)
    
    @dataclass(order=True)
    class ComparableBook:
        title: str = field(compare=False)  # Not used in ordering
        author: str = field(compare=False)  # Not used in ordering
        price: float  # Used for ordering
        pages: int  # Used for ordering
    
    cb1 = ComparableBook("Book A", "Author A", 29.95, 300)
    cb2 = ComparableBook("Book B", "Author B", 19.95, 250)
    cb3 = ComparableBook("Book C", "Author C", 39.95, 400)
    
    print(f"cb1: {cb1}")
    print(f"cb2: {cb2}")
    print(f"cb3: {cb3}")
    
    print(f"\ncb1 < cb2 (compares price, then pages): {cb1 < cb2}")
    print(f"cb1 > cb2: {cb1 > cb2}")
    print(f"cb1 <= cb3: {cb1 <= cb3}")
    
    comparable_books = [cb1, cb2, cb3]
    comparable_books.sort()
    print("\nSorted by price, then pages:")
    for book in comparable_books:
        print(f"  ${book.price:.2f}, {book.pages} pages: {book.title}")
    
    print("\n" + "="*70)
    print("REAL-WORLD EXAMPLE: LIBRARY SYSTEM")
    print("="*70)
    
    @dataclass
    class LibraryRecord:
        book: Book
        quantity: int = 1
        location: str = "General Section"
        borrowed_copies: int = 0
        
        @property
        def available_copies(self):
            return self.quantity - self.borrowed_copies
        
        def borrow(self):
            if self.available_copies > 0:
                self.borrowed_copies += 1
                return True
            return False
        
        def return_copy(self):
            if self.borrowed_copies > 0:
                self.borrowed_copies -= 1
                return True
            return False
        
        def __str__(self):
            return (f"{self.book.title}: {self.available_copies}/{self.quantity} "
                    f"available at {self.location}")
    
    # Create library inventory
    inventory = [
        LibraryRecord(b1, quantity=5, location="Fiction A"),
        LibraryRecord(b2, quantity=3, location="Fiction B"),
        LibraryRecord(b5, quantity=7, location="Classics"),
        LibraryRecord(b6, quantity=2, location="Sci-Fi")
    ]
    
    print("\nLibrary Inventory:")
    for record in inventory:
        print(f"  {record}")
    
    # Simulate borrowing
    print("\nSimulating borrowing:")
    if inventory[0].borrow():
        print(f"  Borrowed '{inventory[0].book.title}'")
        print(f"  Available: {inventory[0].available_copies}/{inventory[0].quantity}")
    
    print("\n" + "="*70)
    print("DATACLASS VS REGULAR CLASS")
    print("="*70)
    
    print("""
    Dataclass Advantages:
    • Less boilerplate code
    • Automatic __init__, __repr__, __eq__
    • Type hints integrated
    • Easy default values
    • Built-in utility functions (asdict, astuple, replace)
    
    When to use Regular Classes:
    • Complex initialization logic
    • Heavy computation in methods
    • Need to control attribute access
    • Inheritance hierarchies with different __init__ signatures
    """)