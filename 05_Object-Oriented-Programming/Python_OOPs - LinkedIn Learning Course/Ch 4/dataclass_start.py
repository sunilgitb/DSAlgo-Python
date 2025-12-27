# Python Object Oriented Programming by Joe Marini course example
# Converting regular class to data class

from dataclasses import dataclass, field, asdict, astuple, replace
from typing import Optional, List
import json

# Original regular class
class BookRegular:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"BookRegular('{self.title}', '{self.author}', {self.pages}, {self.price})"

# TODO: Convert to dataclass
@dataclass
class BookDataClass:
    """Book class implemented as a dataclass."""
    title: str
    author: str
    pages: int
    price: float
    # Additional fields with defaults
    genre: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    isbn: str = "Unknown"
    
    # You can still add custom methods
    def book_info(self):
        return f"'{self.title}' by {self.author} - {self.pages} pages, ${self.price:.2f}"
    
    @property
    def price_per_page(self):
        return self.price / self.pages if self.pages > 0 else 0
    
    def add_tag(self, tag: str):
        self.tags.append(tag)
        return self

# Driver code
if __name__ == "__main__":
    print("="*70)
    print("COMPARING REGULAR CLASS vs DATACLASS")
    print("="*70)
    
    # Create instances using both classes
    print("\n1. Creating instances:")
    b1_regular = BookRegular("War and Peace", "Leo Tolstoy", 1225, 39.95)
    b1_dataclass = BookDataClass("War and Peace", "Leo Tolstoy", 1225, 39.95)
    
    b2_regular = BookRegular("The Catcher in the Rye", "JD Salinger", 234, 29.95)
    b2_dataclass = BookDataClass("The Catcher in the Rye", "JD Salinger", 234, 29.95)
    
    print("Regular class instances created.")
    print("Dataclass instances created.")
    
    print("\n" + "="*70)
    print("ACCESSING FIELDS (Same for both)")
    print("="*70)
    
    # access fields
    print("\nRegular class:")
    print(f"b1_regular.title: {b1_regular.title}")
    print(f"b2_regular.author: {b2_regular.author}")
    
    print("\nDataclass:")
    print(f"b1_dataclass.title: {b1_dataclass.title}")
    print(f"b2_dataclass.author: {b2_dataclass.author}")
    
    print("\nAdditional dataclass fields with defaults:")
    b3_dataclass = BookDataClass("1984", "George Orwell", 328, 19.95, 
                                 genre="Dystopian", tags=["classic", "political"])
    print(f"b3_dataclass.genre: {b3_dataclass.genre}")
    print(f"b3_dataclass.tags: {b3_dataclass.tags}")
    print(f"b3_dataclass.isbn: {b3_dataclass.isbn}")
    
    print("\n" + "="*70)
    print("TODO: PRINT THE BOOK ITSELF - __repr__ IMPLEMENTATION")
    print("="*70)
    
    print("\nRegular class (custom __repr__ required):")
    print(f"print(b1_regular): {b1_regular}")
    print(f"repr(b1_regular): {repr(b1_regular)}")
    
    print("\nDataclass (automatic __repr__ provided):")
    print(f"print(b1_dataclass): {b1_dataclass}")
    print(f"repr(b1_dataclass): {repr(b1_dataclass)}")
    
    print("\nDataclass with extra fields:")
    print(f"b3_dataclass: {b3_dataclass}")
    
    print("\n" + "="*70)
    print("TODO: COMPARING TWO OBJECTS - __eq__ IMPLEMENTATION")
    print("="*70)
    
    # Create identical books
    b4_regular = BookRegular("War and Peace", "Leo Tolstoy", 1225, 39.95)
    b4_dataclass = BookDataClass("War and Peace", "Leo Tolstoy", 1225, 39.95)
    
    print("\nRegular class (no automatic __eq__):")
    print(f"b1_regular == b4_regular: {b1_regular == b4_regular}")  # False (compares memory addresses)
    
    print("\nDataclass (automatic __eq__ provided):")
    print(f"b1_dataclass == b4_dataclass: {b1_dataclass == b4_dataclass}")  # True (compares field values)
    
    print("\nComparing different books:")
    print(f"b1_dataclass == b2_dataclass: {b1_dataclass == b2_dataclass}")
    
    print("\n" + "="*70)
    print("TODO: CHANGE SOME FIELDS")
    print("="*70)
    
    print("Before changes:")
    print(f"b1_dataclass: {b1_dataclass}")
    print(f"b2_dataclass: {b2_dataclass}")
    
    # change some fields
    b1_dataclass.title = "Anna Karenina"
    b1_dataclass.pages = 864
    b1_dataclass.price = 34.95
    b1_dataclass.add_tag("classic").add_tag("russian")
    
    b2_dataclass.genre = "Coming-of-age"
    b2_dataclass.isbn = "978-0-316-76948-0"
    
    print("\nAfter changes:")
    print(f"b1_dataclass: {b1_dataclass}")
    print(f"b2_dataclass: {b2_dataclass}")
    
    print("\n" + "="*70)
    print("ADDITIONAL DATACLASS BENEFITS")
    print("="*70)
    
    print("\n1. Utility functions:")
    
    # Convert to dictionary
    print("\n  asdict() - Convert to dictionary:")
    book_dict = asdict(b1_dataclass)
    print(f"  asdict(b1_dataclass): {json.dumps(book_dict, indent=2)}")
    
    # Convert to tuple
    print("\n  astuple() - Convert to tuple:")
    book_tuple = astuple(b1_dataclass)
    print(f"  astuple(b1_dataclass): {book_tuple}")
    
    # Create modified copy
    print("\n  replace() - Create modified copy (functional programming style):")
    b1_cheaper = replace(b1_dataclass, price=29.95, genre="Classic Literature")
    print(f"  Original: {b1_dataclass}")
    print(f"  Modified copy: {b1_cheaper}")
    
    print("\n2. Dataclass methods work normally:")
    print(f"  b1_dataclass.book_info(): {b1_dataclass.book_info()}")
    print(f"  b1_dataclass.price_per_page: ${b1_dataclass.price_per_page:.4f}")
    
    print("\n" + "="*70)
    print("DATACLASS WITH ORDERING")
    print("="*70)
    
    @dataclass(order=True)
    class ComparableBook:
        """Dataclass with automatic ordering."""
        # sort_index is not a field, just for ordering
        sort_index: int = field(init=False, repr=False)
        title: str
        price: float
        pages: int
        
        def __post_init__(self):
            # Use price as the sort index
            self.sort_index = self.price
    
    print("\nCreating comparable books:")
    cb1 = ComparableBook("Expensive Book", 49.95, 400)
    cb2 = ComparableBook("Cheap Book", 14.95, 200)
    cb3 = ComparableBook("Medium Book", 29.95, 300)
    
    print(f"cb1: {cb1}")
    print(f"cb2: {cb2}")
    print(f"cb3: {cb3}")
    
    print(f"\ncb1 > cb2: {cb1 > cb2}")
    print(f"cb2 < cb3: {cb2 < cb3}")
    
    books = [cb1, cb2, cb3]
    books.sort()
    print("\nSorted by price:")
    for book in books:
        print(f"  ${book.price:.2f}: {book.title}")
    
    print("\n" + "="*70)
    print("FROZEN DATACLASS (IMMUTABLE)")
    print("="*70)
    
    @dataclass(frozen=True)
    class ImmutableBook:
        title: str
        author: str
        pages: int
        price: float
    
    frozen_book = ImmutableBook("Frozen Book", "Immut Author", 100, 9.99)
    print(f"frozen_book: {frozen_book}")
    
    try:
        frozen_book.title = "New Title"  # This will fail
    except Exception as e:
        print(f"Cannot modify frozen dataclass: {type(e).__name__}")
    
    # But you can use replace() to create a modified copy
    modified_frozen = replace(frozen_book, price=12.99)
    print(f"Modified copy: {modified_frozen}")
    
    print("\n" + "="*70)
    print("REAL-WORLD COMPARISON")
    print("="*70)
    
    # Regular class for complex logic
    class ComplexBook:
        def __init__(self, title, author, pages, price):
            self.title = title
            self.author = author
            self.pages = pages
            self.price = price
            self._validate_input()
        
        def _validate_input(self):
            if self.pages <= 0:
                raise ValueError("Pages must be positive")
            if self.price <= 0:
                raise ValueError("Price must be positive")
        
        def apply_discount(self, percent):
            self.price = self.price * (1 - percent/100)
            return self
        
        def get_reading_time(self, pages_per_hour=50):
            return self.pages / pages_per_hour
        
        def __str__(self):
            return f"'{self.title}' by {self.author}"
        
        def __repr__(self):
            return f"ComplexBook('{self.title}', '{self.author}', {self.pages}, {self.price})"
    
    print("\nWhen to use regular class:")
    print("• Complex validation in __init__")
    print("• Many methods with complex logic")
    print("• Need for precise control")
    
    print("\nWhen to use dataclass:")
    print("• Primarily data storage")
    print("• Want automatic __repr__, __eq__, etc.")
    print("• Simple data transfer objects")
    print("• Configuration objects")
    
    print("\n" + "="*70)
    print("SUMMARY: DATACLASS VS REGULAR CLASS")
    print("="*70)
    
    print("""
    Regular Class (BookRegular):
    + Complete control over implementation
    + Can optimize for performance
    + Flexible inheritance
    - More boilerplate code
    - Manual __init__, __repr__, __eq__ needed
    
    Dataclass (BookDataClass):
    + Less boilerplate (auto __init__, __repr__, __eq__)
    + Type hints integrated
    + Built-in utilities (asdict, astuple, replace)
    + Easy default values
    - Less control over __init__ logic
    - May be slightly slower for complex cases
    
    Recommendation:
    • Use dataclasses for data containers, DTOs, config objects
    • Use regular classes for complex business logic
    • Mix both when appropriate
    """)
    
    # Final demonstration
    print("\n" + "="*70)
    print("FINAL DEMONSTRATION")
    print("="*70)
    
    library = [
        BookDataClass("Dune", "Frank Herbert", 412, 35.95, "Sci-Fi", ["space", "epic"]),
        BookDataClass("Pride and Prejudice", "Jane Austen", 432, 19.95, "Romance", ["classic", "romance"]),
        BookDataClass("The Hobbit", "J.R.R. Tolkien", 310, 24.95, "Fantasy", ["adventure", "fantasy"]),
    ]
    
    print("\nLibrary Catalog (dataclasses make this easy!):")
    for i, book in enumerate(library, 1):
        print(f"\n{i}. {book}")
        print(f"   Genre: {book.genre}")
        print(f"   Tags: {', '.join(book.tags)}")
        print(f"   Price per page: ${book.price_per_page:.4f}")