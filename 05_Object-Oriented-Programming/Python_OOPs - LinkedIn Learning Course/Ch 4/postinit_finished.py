# Python Object Oriented Programming by Joe Marini course example
# Using the postinit function in data classes

from dataclasses import dataclass, field, fields
from typing import List, Optional, ClassVar
import random
from datetime import datetime


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
    
    # Class variables (not part of __init__)
    total_books_created: ClassVar[int] = 0
    genres: ClassVar[List[str]] = ["Fiction", "Non-Fiction", "Sci-Fi", "Fantasy", "Mystery"]
    
    # Fields that will be initialized in __post_init__
    description: str = field(init=False)  # Not in __init__, will be set in __post_init__
    book_id: str = field(init=False)      # Generated ID
    isbn: str = field(default="Unknown")  # Regular field with default
    tags: List[str] = field(default_factory=list)  # Mutable field with factory
    date_added: datetime = field(default_factory=datetime.now)
    
    # Computed fields (will be calculated in __post_init__)
    price_per_page: float = field(init=False)
    page_count_category: str = field(init=False)
    
    # the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    def __post_init__(self):
        """Initialize computed fields and perform validation/setup."""
        
        # 1. Update class variable
        Book.total_books_created += 1
        
        # 2. Generate unique book ID
        author_initials = ''.join([name[0].upper() for name in self.author.split()])
        self.book_id = f"BK-{author_initials}-{Book.total_books_created:04d}"
        
        # 3. Set description
        self.description = f"{self.title} by {self.author}, {self.pages} pages"
        
        # 4. Compute derived fields
        if self.pages > 0:
            self.price_per_page = self.price / self.pages
        else:
            self.price_per_page = 0.0
        
        # 5. Categorize by page count
        if self.pages < 200:
            self.page_count_category = "Short"
        elif self.pages < 500:
            self.page_count_category = "Medium"
        else:
            self.page_count_category = "Long"
        
        # 6. Validation
        if self.price < 0:
            raise ValueError(f"Price cannot be negative: ${self.price}")
        
        if self.pages <= 0:
            raise ValueError(f"Pages must be positive: {self.pages}")
        
        # 7. Auto-generate ISBN if not provided
        if self.isbn == "Unknown":
            self.isbn = f"978-{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"
        
        # 8. Add default tags based on page count
        if not self.tags:
            self.tags.append(self.page_count_category.lower())
            self.tags.append("general")
    
    # Additional methods
    def apply_discount(self, percent: float):
        """Apply discount and update computed fields."""
        if 0 <= percent <= 100:
            self.price = self.price * (1 - percent/100)
            # Recompute price per page
            if self.pages > 0:
                self.price_per_page = self.price / self.pages
        return self
    
    def add_tag(self, tag: str):
        self.tags.append(tag)
        return self
    
    def book_info(self) -> str:
        """Return formatted book information."""
        return f"{self.title} (ID: {self.book_id}) - ${self.price:.2f}"
    
    @classmethod
    def create_short_book(cls, title: str, author: str, price: float) -> 'Book':
        """Factory method to create a short book."""
        return cls(title=title, author=author, pages=150, price=price)
    
    @property
    def is_expensive(self) -> bool:
        """Computed property."""
        return self.price > 30


# Example with inheritance
@dataclass
class EBook(Book):
    file_format: str = "PDF"
    file_size_mb: float = 0.0
    drm_protected: bool = False
    
    def __post_init__(self):
        """Extend parent's __post_init__."""
        # First call parent's __post_init__
        super().__post_init__()
        
        # Then add EBook-specific initialization
        if self.file_size_mb == 0.0:
            # Estimate file size (approx 50KB per page)
            self.file_size_mb = round(self.pages * 0.05, 2)
        
        # Add ebook-specific tag
        self.tags.append("digital")
        self.tags.append(self.file_format.lower())
        
        # Update description for ebooks
        self.description = f"{self.title} by {self.author}, {self.pages} pages [{self.file_format}]"


# Example with validation and transformation
@dataclass
class ValidatedBook:
    title: str
    author: str
    pages: int = field(default=100)
    price: float = field(default=0.0)
    
    # Computed fields
    normalized_title: str = field(init=False)
    normalized_author: str = field(init=False)
    
    def __post_init__(self):
        """Normalize and validate data."""
        # Normalize strings
        self.normalized_title = self.title.strip().title()
        self.normalized_author = self.author.strip().title()
        
        # Validate pages
        if self.pages <= 0:
            raise ValueError(f"Pages must be positive, got {self.pages}")
        
        # Validate price
        if self.price < 0:
            raise ValueError(f"Price cannot be negative, got ${self.price:.2f}")
        
        # Auto-correct common issues
        if self.price == 0.0:
            # Set default price based on pages
            self.price = self.pages * 0.1  # $0.10 per page
    
    def __str__(self):
        return f"'{self.normalized_title}' by {self.normalized_author}"


# Driver code
if __name__ == "__main__":
    print("="*80)
    print("DATACLASS __post_init__ METHOD DEMONSTRATION")
    print("="*80)
    
    print("\n1. BASIC __post_init__ USAGE")
    print("-"*40)
    
    # create some Book objects
    b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
    
    print(f"\nBook 1 created:")
    print(f"  Description: {b1.description}")
    print(f"  Book ID: {b1.book_id}")
    print(f"  ISBN: {b1.isbn}")
    print(f"  Price per page: ${b1.price_per_page:.4f}")
    print(f"  Page category: {b1.page_count_category}")
    print(f"  Tags: {b1.tags}")
    print(f"  Date added: {b1.date_added.strftime('%Y-%m-%d %H:%M:%S')}")
    
    print(f"\nBook 2 created:")
    print(f"  Description: {b2.description}")
    print(f"  Book ID: {b2.book_id}")
    print(f"  Is expensive? {b2.is_expensive}")
    
    print(f"\nTotal books created: {Book.total_books_created}")
    
    print("\n" + "="*80)
    print("2. VALIDATION IN __post_init__")
    print("-"*40)
    
    print("\nTrying to create invalid book:")
    try:
        bad_book = Book("Bad Book", "Bad Author", -100, -10.0)
    except ValueError as e:
        print(f"  ❌ Validation error: {e}")
    
    print("\nTrying to create book with zero pages:")
    try:
        zero_page_book = Book("Zero Pages", "Some Author", 0, 19.99)
    except ValueError as e:
        print(f"  ❌ Validation error: {e}")
    
    print("\n" + "="*80)
    print("3. COMPUTED FIELDS AND PROPERTIES")
    print("-"*40)
    
    # Create another book
    b3 = Book("1984", "George Orwell", 328, 19.95)
    
    print(f"\nBook: {b3.title}")
    print(f"  Price per page: ${b3.price_per_page:.4f}")
    print(f"  Page category: {b3.page_count_category}")
    print(f"  Is expensive? {b3.is_expensive}")
    
    # Apply discount
    print("\nApplying 20% discount:")
    b3.apply_discount(20)
    print(f"  New price: ${b3.price:.2f}")
    print(f"  New price per page: ${b3.price_per_page:.4f}")
    
    print("\n" + "="*80)
    print("4. INHERITANCE AND __post_init__")
    print("-"*40)
    
    # Create EBook
    ebook = EBook(
        title="Digital Python",
        author="Python Expert",
        pages=300,
        price=24.99,
        file_format="EPUB"
    )
    
    print(f"\nEBook created:")
    print(f"  Description: {ebook.description}")
    print(f"  File format: {ebook.file_format}")
    print(f"  File size: {ebook.file_size_mb} MB")
    print(f"  Tags: {ebook.tags}")
    print(f"  Inherited Book ID: {ebook.book_id}")
    
    print("\n" + "="*80)
    print("5. DATA NORMALIZATION EXAMPLE")
    print("-"*40)
    
    # Create validated book with messy input
    messy_book = ValidatedBook(
        title="  the great gatsby  ",
        author="  f. scott fitzgerald  ",
        pages=218
        # Price will be auto-calculated
    )
    
    print(f"\nOriginal input:")
    print(f"  Title: '  the great gatsby  '")
    print(f"  Author: '  f. scott fitzgerald  '")
    print(f"  Pages: 218")
    print(f"  Price: Not provided (will be auto-calculated)")
    
    print(f"\nAfter __post_init__ normalization:")
    print(f"  Book: {messy_book}")
    print(f"  Normalized title: '{messy_book.normalized_title}'")
    print(f"  Normalized author: '{messy_book.normalized_author}'")
    print(f"  Auto-calculated price: ${messy_book.price:.2f}")
    
    print("\n" + "="*80)
    print("6. FACTORY METHODS AND __post_init__")
    print("-"*40)
    
    # Use factory method
    short_book = Book.create_short_book(
        title="Python Quick Guide",
        author="A. Programmer",
        price=14.99
    )
    
    print(f"\nFactory-created short book:")
    print(f"  {short_book.book_info()}")
    print(f"  Pages: {short_book.pages}")
    print(f"  Page category: {short_book.page_count_category}")
    
    print("\n" + "="*80)
    print("7. REAL-WORLD EXAMPLE: INVENTORY SYSTEM")
    print("-"*40)
    
    @dataclass
    class InventoryItem:
        book: Book
        quantity: int = 0
        reorder_point: int = 5
        
        # Computed fields
        needs_reorder: bool = field(init=False)
        total_value: float = field(init=False)
        item_id: str = field(init=False)
        
        def __post_init__(self):
            """Initialize computed inventory fields."""
            # Generate item ID
            self.item_id = f"INV-{self.book.book_id}-{datetime.now().strftime('%Y%m%d')}"
            
            # Compute needs_reorder
            self.needs_reorder = self.quantity <= self.reorder_point
            
            # Compute total value
            self.total_value = self.book.price * self.quantity
            
            # Validate
            if self.quantity < 0:
                raise ValueError(f"Quantity cannot be negative: {self.quantity}")
        
        def sell(self, amount: int = 1):
            """Sell items from inventory."""
            if amount <= self.quantity:
                self.quantity -= amount
                # Update computed fields
                self.total_value = self.book.price * self.quantity
                self.needs_reorder = self.quantity <= self.reorder_point
                return True
            return False
        
        def restock(self, amount: int):
            """Restock inventory."""
            self.quantity += amount
            # Update computed fields
            self.total_value = self.book.price * self.quantity
            self.needs_reorder = self.quantity <= self.reorder_point
            return self
        
        def __str__(self):
            status = "📦 REORDER" if self.needs_reorder else "✅ OK"
            return f"{self.book.title}: {self.quantity} units (${self.total_value:.2f}) - {status}"
    
    # Create inventory
    inventory = [
        InventoryItem(b1, quantity=3, reorder_point=2),
        InventoryItem(b2, quantity=10, reorder_point=5),
        InventoryItem(b3, quantity=1, reorder_point=3),
    ]
    
    print("\nBookstore Inventory:")
    for item in inventory:
        print(f"  {item}")
        print(f"    Item ID: {item.item_id}")
    
    # Simulate sales
    print("\nSimulating sales:")
    if inventory[0].sell(2):
        print(f"  Sold 2 copies of '{inventory[0].book.title}'")
        print(f"  Remaining: {inventory[0].quantity} units")
        print(f"  Needs reorder? {inventory[0].needs_reorder}")
    
    print("\n" + "="*80)
    print("8. COMMON USE CASES FOR __post_init__")
    print("-"*40)
    
    print("""
    Common __post_init__ Use Cases:
    
    1. Validation: Check field values are valid
    2. Normalization: Clean up input data
    3. Computed Fields: Calculate derived values
    4. Default Generation: Auto-generate IDs, timestamps, etc.
    5. Relationship Setup: Initialize connections between objects
    6. Caching Setup: Prepare cached properties
    7. State Initialization: Set up initial state
    8. Dependency Injection: Initialize dependent objects
    """)
    
    print("\n" + "="*80)
    print("9. BEST PRACTICES")
    print("-"*40)
    
    print("""
    Best Practices for __post_init__:
    
    1. Keep it focused: One responsibility - initialization
    2. Call super().__post_init__() in inheritance chains
    3. Validate early: Check constraints as soon as possible
    4. Be careful with exceptions: They occur after __init__
    5. Document what you're doing: Complex logic needs comments
    6. Consider performance: Heavy computation might be better elsewhere
    7. Use for initialization only: Not for business logic
    8. Test thoroughly: __post_init__ logic needs testing
    """)
    
    print("\n" + "="*80)
    print("10. PITFALLS TO AVOID")
    print("-"*40)
    
    print("""
    Common Pitfalls:
    
    1. Modifying init-only fields: Use field(init=False) for computed fields
    2. Forgetting super().__post_init__() in inheritance
    3. Heavy computation slowing down object creation
    4. Side effects that affect other objects
    5. Not handling exceptions properly
    6. Circular dependencies in computed fields
    7. Assuming __post_init__ runs in __new__ (it doesn't)
    """)
    
    # Demonstrate a pitfall
    print("\nPitfall Example - Modifying non-init fields carelessly:")
    
    @dataclass
    class ProblematicBook:
        title: str
        pages: int
        
        def __post_init__(self):
            # This modifies a field that WAS in __init__
            # It works but can be confusing
            self.title = self.title.upper()  # Modifying init field
    
    pb = ProblematicBook("test book", 100)
    print(f"  Created with 'test book', but title is now: {pb.title}")
    
    print("\n" + "="*80)
    print("FINAL SUMMARY")
    print("="*80)
    
    # Show all books created
    all_books = [b1, b2, b3, short_book]
    
    print(f"\nTotal books in session: {Book.total_books_created}")
    print("\nAll books created:")
    for i, book in enumerate(all_books, 1):
        print(f"\n{i}. {book.book_info()}")
        print(f"   ID: {book.book_id}")
        print(f"   Pages: {book.pages} ({book.page_count_category})")
        print(f"   Price/page: ${book.price_per_page:.4f}")
        print(f"   Tags: {', '.join(book.tags)}")