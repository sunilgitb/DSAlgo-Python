# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random
from typing import List, Optional, ClassVar
from datetime import datetime


# Helper functions for default factories
def generate_random_price():
    """Generate a random price between 15 and 50."""
    return round(random.uniform(15.0, 50.0), 2)


def generate_isbn():
    """Generate a fake ISBN number."""
    return f"978-{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"


def default_tags():
    """Return default tags for a new book."""
    return ["new-arrival"]


@dataclass
class Book:
    # TODO: Define default values for attributes
    
    # Class variables (shared by all instances, not part of __init__)
    total_books: ClassVar[int] = 0
    genres: ClassVar[List[str]] = [
        "Fiction", "Non-Fiction", "Science Fiction", 
        "Fantasy", "Mystery", "Biography", "Poetry"
    ]
    
    # Instance fields with various default value strategies:
    
    # 1. Required fields without defaults (must be provided)
    title: str  # No default - must be provided
    
    # 2. Field with simple default value
    author: str = "Unknown Author"
    
    # 3. Field with integer default
    pages: int = 0
    
    # 4. Field with float default
    price: float = 0.0
    
    # 5. Optional field with None as default
    subtitle: Optional[str] = None
    
    # 6. Field with default_factory for dynamic default
    isbn: str = field(default_factory=generate_isbn)
    
    # 7. List field with default_factory to avoid mutable default issue
    tags: List[str] = field(default_factory=default_tags)
    
    # 8. Field excluded from string representation
    internal_id: int = field(default=0, repr=False)
    
    # 9. Field excluded from equality comparisons
    date_added: datetime = field(default_factory=datetime.now, compare=False)
    
    # 10. Field with metadata
    rating: float = field(default=0.0, metadata={
        "min": 0.0,
        "max": 5.0,
        "description": "Average user rating"
    })
    
    # 11. Optional field with specific default
    genre: Optional[str] = field(default=None, metadata={
        "choices": ["Fiction", "Non-Fiction", "Sci-Fi", "Fantasy", "Other"]
    })
    
    # 12. Computed field (initialized in __post_init__)
    price_per_page: float = field(init=False, default=0.0)
    
    def __post_init__(self):
        """Initialize computed fields after the main initialization."""
        # Update class variable
        Book.total_books += 1
        
        # Generate internal ID if not set
        if self.internal_id == 0:
            self.internal_id = Book.total_books
        
        # Compute price per page
        if self.pages > 0:
            self.price_per_page = self.price / self.pages
        
        # Set default genre if not provided
        if self.genre is None:
            self.genre = "Fiction"  # Default genre
    
    # Instance method
    def book_info(self):
        """Return formatted book information."""
        subtitle_info = f": {self.subtitle}" if self.subtitle else ""
        genre_info = f" [{self.genre}]" if self.genre else ""
        return f"'{self.title}{subtitle_info}' by {self.author}{genre_info}"
    
    def apply_discount(self, percent: float):
        """Apply a discount to the book price."""
        if 0 <= percent <= 100:
            self.price = self.price * (1 - percent/100)
            # Recompute price per page
            if self.pages > 0:
                self.price_per_page = self.price / self.pages
        return self
    
    @classmethod
    def get_genres(cls):
        """Return available genres."""
        return cls.genres
    
    @staticmethod
    def format_price(price: float) -> str:
        """Format price as currency string."""
        return f"${price:.2f}"


# Example with inheritance
@dataclass
class EBook(Book):
    """Extended Book class for electronic books."""
    # Override parent default
    tags: List[str] = field(default_factory=lambda: ["ebook", "digital"])
    
    # New fields with defaults
    file_format: str = "PDF"
    file_size_mb: float = 0.0
    drm_protected: bool = False
    
    def __post_init__(self):
        """Initialize EBook-specific fields."""
        super().__post_init__()
        # Estimate file size if not provided (approx 50KB per page)
        if self.file_size_mb == 0.0 and self.pages > 0:
            self.file_size_mb = round(self.pages * 0.05, 2)


# Immutable dataclass example
@dataclass(frozen=True)
class ImmutableBook:
    """Immutable book with defaults."""
    title: str = "Untitled"
    author: str = "Unknown"
    pages: int = 100
    price: float = 19.99


# Driver code
if __name__ == "__main__":
    print("="*80)
    print("DATACLASS DEFAULT VALUES IMPLEMENTATION")
    print("="*80)
    
    print("\n1. CREATING BOOKS WITH DIFFERENT DEFAULT COMBINATIONS")
    print("-"*60)
    
    # Test Case 1: Minimal information (only required field)
    print("\na) Minimal book (only title provided):")
    try:
        minimal_book = Book("The Great Unknown")
        print(f"   Book('The Great Unknown') = {minimal_book}")
        print(f"   Author defaulted to: {minimal_book.author}")
        print(f"   Pages defaulted to: {minimal_book.pages}")
        print(f"   Price defaulted to: ${minimal_book.price:.2f}")
        print(f"   ISBN generated: {minimal_book.isbn}")
        print(f"   Tags: {minimal_book.tags}")
        print(f"   Price per page computed: ${minimal_book.price_per_page:.4f}")
    except Exception as e:
        print(f"   Error: {type(e).__name__}: {e}")
    
    # Test Case 2: Partial information
    print("\nb) Partial information (title and author):")
    partial_book = Book("Python Programming", "John Doe")
    print(f"   Book('Python Programming', 'John Doe') = {partial_book}")
    print(f"   Internal ID (not in repr): {partial_book.internal_id}")
    print(f"   Date added: {partial_book.date_added.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Test Case 3: More complete information
    print("\nc) More complete book:")
    complete_book = Book(
        title="Data Science Handbook",
        author="Jane Smith",
        pages=450,
        price=49.99,
        genre="Non-Fiction"
    )
    print(f"   Complete book = {complete_book}")
    print(f"   Price per page: ${complete_book.price_per_page:.4f}")
    print(f"   Book info: {complete_book.book_info()}")
    
    # Test Case 4: Full customization
    print("\nd) Fully customized book:")
    custom_book = Book(
        title="The Art of Programming",
        author="Donald Knuth",
        pages=650,
        price=79.99,
        subtitle="Volume 1: Fundamental Algorithms",
        genre="Computer Science",
        tags=["programming", "algorithms", "classic"]
    )
    print(f"   Custom book = {custom_book}")
    print(f"   Subtitle: {custom_book.subtitle}")
    print(f"   Rating metadata: {field(Book, 'rating').metadata}")
    
    print("\n" + "="*80)
    print("2. TESTING EQUALITY WITH DEFAULTS")
    print("-"*60)
    
    # Create two books with same data but different dynamic fields
    book1 = Book("Same Book", "Same Author", 100, 29.99)
    book2 = Book("Same Book", "Same Author", 100, 29.99)
    
    print(f"\nbook1 = {book1}")
    print(f"book2 = {book2}")
    print(f"\nbook1 == book2 (compares fields with compare=True): {book1 == book2}")
    print(f"ISBNs are different: {book1.isbn} vs {book2.isbn}")
    print(f"Dates are different but compare=False: {book1.date_added != book2.date_added}")
    
    print("\n" + "="*80)
    print("3. MUTABLE DEFAULTS DEMONSTRATION")
    print("-"*60)
    
    print("\nTesting list defaults (each book gets its own list):")
    book_a = Book("Book A", "Author A")
    book_b = Book("Book B", "Author B")
    
    book_a.tags.append("fiction")
    book_b.tags.append("non-fiction")
    
    print(f"book_a.tags: {book_a.tags}")
    print(f"book_b.tags: {book_b.tags}")
    print("✓ Each book has its own independent tags list")
    
    print("\n" + "="*80)
    print("4. METHODS AND PROPERTIES")
    print("-"*60)
    
    # Test methods
    test_book = Book("Test Book", "Test Author", 200, 39.99)
    
    print(f"\nOriginal book: {test_book.book_info()}")
    print(f"Original price: {Book.format_price(test_book.price)}")
    
    # Apply discount
    test_book.apply_discount(20)  # 20% discount
    print(f"After 20% discount: {Book.format_price(test_book.price)}")
    print(f"Price per page after discount: ${test_book.price_per_page:.4f}")
    
    # Class method
    print(f"\nAvailable genres: {Book.get_genres()}")
    
    print("\n" + "="*80)
    print("5. INHERITANCE WITH DEFAULTS")
    print("-"*60)
    
    print("\nCreating EBook instances:")
    
    # EBook with minimal info
    ebook1 = EBook("Digital Revolution")
    print(f"\na) Minimal EBook:")
    print(f"   {ebook1}")
    print(f"   File format: {ebook1.file_format}")
    print(f"   File size (estimated): {ebook1.file_size_mb}MB")
    print(f"   Tags (overridden): {ebook1.tags}")
    
    # EBook with more info
    ebook2 = EBook(
        title="Python E-Book",
        author="Python Expert",
        pages=300,
        price=29.99,
        file_format="EPUB",
        drm_protected=True
    )
    print(f"\nb) Complete EBook:")
    print(f"   {ebook2}")
    print(f"   DRM Protected: {ebook2.drm_protected}")
    print(f"   File size: {ebook2.file_size_mb}MB")
    
    print("\n" + "="*80)
    print("6. CLASS VARIABLES VS INSTANCE DEFAULTS")
    print("-"*60)
    
    print(f"\nClass variables (shared by all books):")
    print(f"Total books created: {Book.total_books}")
    print(f"Available genres: {Book.genres}")
    
    # Modify class variable
    Book.genres.append("Historical Fiction")
    print(f"After adding genre: {Book.genres}")
    
    print("\n" + "="*80)
    print("7. PRACTICAL EXAMPLE: BOOKSTORE INVENTORY")
    print("-"*60)
    
    @dataclass
    class InventoryItem:
        book: Book
        quantity: int = 0
        reorder_threshold: int = 5
        last_restock: datetime = field(default_factory=datetime.now)
        
        def needs_reorder(self) -> bool:
            return self.quantity <= self.reorder_threshold
        
        def sell(self, amount: int = 1) -> bool:
            if self.quantity >= amount:
                self.quantity -= amount
                return True
            return False
        
        def restock(self, amount: int):
            self.quantity += amount
            self.last_restock = datetime.now()
            return self
        
        def __str__(self):
            status = "📦 Needs reorder" if self.needs_reorder() else "✅ In stock"
            return f"{self.book.title}: {self.quantity} units - {status}"
    
    # Create inventory
    inventory = [
        InventoryItem(
            Book("Python Basics", "A. Programmer", 350, 34.99, genre="Programming"),
            quantity=10
        ),
        InventoryItem(
            Book("Advanced Algorithms", "B. Scientist", 500, 59.99),
            quantity=3  # Below threshold
        ),
        InventoryItem(
            Book("Data Visualization", "C. Analyst", 280, 44.99),
            quantity=15
        ),
    ]
    
    print("\nBookstore Inventory:")
    for item in inventory:
        print(f"  {item}")
    
    # Simulate sales
    print("\nSimulating sales:")
    if inventory[0].sell(2):
        print(f"  Sold 2 copies of '{inventory[0].book.title}'")
        print(f"  Remaining: {inventory[0].quantity}")
    
    print("\n" + "="*80)
    print("8. BEST PRACTICES SUMMARY")
    print("-"*60)
    
    print("""
    Default Value Best Practices:
    
    1. Required Fields:
       - Don't provide defaults for truly required data
       - Example: title: str (no default)
    
    2. Simple Defaults:
       - Use for common, static values
       - Example: author: str = "Unknown"
    
    3. Dynamic Defaults:
       - Use field(default_factory=...) for values that change
       - Example: date_added: datetime = field(default_factory=datetime.now)
    
    4. Mutable Defaults:
       - ALWAYS use default_factory for lists, dicts, sets
       - Example: tags: List[str] = field(default_factory=list)
    
    5. Optional Fields:
       - Use Optional[Type] = None for truly optional data
       - Example: subtitle: Optional[str] = None
    
    6. Computed Fields:
       - Use field(init=False) and compute in __post_init__
       - Example: price_per_page: float = field(init=False)
    
    7. Metadata:
       - Use field(metadata=...) for additional field info
       - Useful for validation, documentation
    
    8. Class Variables:
       - Use ClassVar for data shared across all instances
       - Example: total_books: ClassVar[int] = 0
    """)
    
    print("\n" + "="*80)
    print("9. ERROR SCENARIOS TO CONSIDER")
    print("-"*60)
    
    print("\na) Missing required field:")
    try:
        # This will fail because title is required
        bad_book = Book()  # Missing required argument 'title'
    except TypeError as e:
        print(f"   TypeError: {e}")
    
    print("\nb) Wrong type for field with default:")
    try:
        # This works because defaults are used
        weird_book = Book("Weird Book", pages="not a number")  # Wrong type, but default kicks in
        print(f"   Created: {weird_book}")
        print(f"   Pages used default: {weird_book.pages}")
    except Exception as e:
        print(f"   Error: {type(e).__name__}: {e}")
    
    print("\n" + "="*80)
    print("FINAL DEMONSTRATION")
    print("="*80)
    
    # Show all books created
    all_books = [minimal_book, partial_book, complete_book, custom_book, 
                 test_book, book1, book2, book_a, book_b]
    
    print(f"\nTotal books created in session: {Book.total_books}")
    print("\nAll books created:")
    for i, book in enumerate(all_books, 1):
        if hasattr(book, 'title'):  # Skip None if any creation failed
            print(f"\n{i}. {book.book_info()}")
            print(f"   Price: ${book.price:.2f}, Pages: {book.pages}")
            print(f"   ISBN: {book.isbn}")