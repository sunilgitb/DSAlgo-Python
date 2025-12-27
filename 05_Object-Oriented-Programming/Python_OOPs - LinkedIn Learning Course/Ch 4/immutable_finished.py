# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass, field, replace
from typing import List, Tuple, Dict, Optional, ClassVar
from datetime import datetime
import copy

# Example 1: Basic immutable dataclass
@dataclass(frozen=True)  # The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0
    
    # Methods are allowed but cannot modify instance attributes
    def display(self):
        return f"value1={self.value1}, value2={self.value2}"
    
    def with_changes(self, **kwargs):
        """Return a new instance with updated values."""
        # Use dataclasses.replace to create a modified copy
        from dataclasses import replace
        return replace(self, **kwargs)
    
    # This method would cause an error if it tried to modify attributes
    def invalid_method(self, newval):
        # Uncommenting the next line would raise FrozenInstanceError
        # self.value2 = newval
        return f"Cannot modify - this is a frozen class"


# Example 2: Immutable Book with practical use case
@dataclass(frozen=True)
class ImmutableBook:
    """An immutable book record - once created, cannot be modified."""
    title: str
    author: str
    pages: int
    price: float
    isbn: str = field(default="Unknown", compare=False)
    publication_date: datetime = field(default_factory=datetime.now, compare=False)
    genres: Tuple[str, ...] = field(default_factory=tuple)  # Use tuple instead of list
    
    # Class variable (not frozen, shared across instances)
    total_books_created: ClassVar[int] = 0
    
    def __post_init__(self):
        """Can still run initialization logic, but cannot modify fields."""
        # We can't modify self directly, but we can modify the class
        type(self).total_books_created += 1
        
        # For validation or computation, we can use object.__setattr__
        # but this should be done carefully
        if self.pages <= 0:
            object.__setattr__(self, 'pages', 1)
    
    # Computed properties (read-only)
    @property
    def price_per_page(self) -> float:
        if self.pages > 0:
            return self.price / self.pages
        return 0.0
    
    @property
    def book_info(self) -> str:
        genres_str = f" ({', '.join(self.genres)})" if self.genres else ""
        return f"'{self.title}' by {self.author}{genres_str} - ${self.price:.2f}"
    
    def add_genre(self, genre: str) -> 'ImmutableBook':
        """Return a new book with the added genre."""
        new_genres = self.genres + (genre,)
        return replace(self, genres=new_genres)
    
    def apply_discount(self, percent: float) -> 'ImmutableBook':
        """Return a new book with discounted price."""
        if 0 <= percent <= 100:
            new_price = self.price * (1 - percent/100)
            return replace(self, price=new_price)
        return self
    
    @classmethod
    def create_from_dict(cls, data: Dict) -> 'ImmutableBook':
        """Factory method to create from dictionary."""
        return cls(
            title=data.get('title', 'Untitled'),
            author=data.get('author', 'Unknown'),
            pages=data.get('pages', 0),
            price=data.get('price', 0.0),
            isbn=data.get('isbn', 'Unknown'),
            genres=tuple(data.get('genres', []))
        )


# Example 3: Immutable configuration object
@dataclass(frozen=True)
class AppConfig:
    """Immutable configuration for an application."""
    app_name: str
    version: str
    debug: bool = False
    max_connections: int = 100
    timeout_seconds: float = 30.0
    allowed_hosts: Tuple[str, ...] = ('localhost', '127.0.0.1')
    
    @property
    def is_production(self) -> bool:
        return not self.debug
    
    def with_setting(self, **kwargs) -> 'AppConfig':
        """Return new config with updated settings."""
        return replace(self, **kwargs)


# Example 4: Immutable with nested objects (requires careful handling)
@dataclass(frozen=True)
class Library:
    """Immutable library containing immutable books."""
    name: str
    books: Tuple[ImmutableBook, ...] = field(default_factory=tuple)
    location: str = "Unknown"
    
    def add_book(self, book: ImmutableBook) -> 'Library':
        """Return a new library with the book added."""
        return replace(self, books=self.books + (book,))
    
    def remove_book(self, isbn: str) -> 'Library':
        """Return a new library with the book removed."""
        new_books = tuple(b for b in self.books if b.isbn != isbn)
        return replace(self, books=new_books)
    
    def find_by_author(self, author: str) -> Tuple[ImmutableBook, ...]:
        """Find books by author (returns new tuple)."""
        return tuple(b for b in self.books if b.author.lower() == author.lower())
    
    @property
    def total_value(self) -> float:
        return sum(book.price for book in self.books)
    
    @property
    def book_count(self) -> int:
        return len(self.books)


# Driver code
if __name__ == "__main__":
    print("="*80)
    print("IMMUTABLE DATA CLASSES")
    print("="*80)
    
    print("\n1. BASIC IMMUTABLE DATACLASS")
    print("-"*40)
    
    # Create immutable object
    obj = ImmutableClass()
    print(f"Created: {obj}")
    print(f"Display method: {obj.display()}")
    
    # Try to modify (will fail)
    print("\nAttempting to modify immutable object:")
    try:
        obj.value1 = "Another value"
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}: {e}")
    
    print(f"\nOriginal object unchanged: {obj}")
    
    # Create modified copy
    print("\nCreating modified copy using replace():")
    modified_obj = obj.with_changes(value1="Modified Value", value2=42)
    print(f"Original: {obj}")
    print(f"Modified: {modified_obj}")
    
    print("\n" + "="*80)
    print("2. PRACTICAL EXAMPLE: IMMUTABLE BOOK")
    print("-"*40)
    
    # Create immutable books
    book1 = ImmutableBook(
        title="1984",
        author="George Orwell",
        pages=328,
        price=19.95,
        genres=("Dystopian", "Political")
    )
    
    book2 = ImmutableBook(
        title="To Kill a Mockingbird",
        author="Harper Lee",
        pages=324,
        price=14.99,
        genres=("Fiction", "Classic")
    )
    
    print(f"\nBook 1: {book1.book_info}")
    print(f"Price per page: ${book1.price_per_page:.4f}")
    print(f"Genres: {book1.genres}")
    
    print(f"\nBook 2: {book2.book_info}")
    
    # Try to modify (will fail)
    print("\nAttempting to modify book price:")
    try:
        book1.price = 9.99
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}: {e}")
    
    # Create modified versions
    print("\nCreating modified copies:")
    discounted_book = book1.apply_discount(20)
    print(f"Original: ${book1.price:.2f}")
    print(f"With 20% discount: ${discounted_book.price:.2f}")
    
    book_with_genre = book2.add_genre("Southern Gothic")
    print(f"\nOriginal genres: {book2.genres}")
    print(f"With added genre: {book_with_genre.genres}")
    
    print(f"\nTotal books created: {ImmutableBook.total_books_created}")
    
    print("\n" + "="*80)
    print("3. IMMUTABLE CONFIGURATION OBJECT")
    print("-"*40)
    
    # Create config
    config = AppConfig(
        app_name="MyApp",
        version="1.0.0",
        debug=True,
        max_connections=50
    )
    
    print(f"\nApp Config:")
    print(f"Name: {config.app_name}")
    print(f"Version: {config.version}")
    print(f"Debug: {config.debug}")
    print(f"Production: {config.is_production}")
    print(f"Max connections: {config.max_connections}")
    print(f"Allowed hosts: {config.allowed_hosts}")
    
    # Create production config
    print("\nCreating production config:")
    prod_config = config.with_setting(debug=False, max_connections=200)
    print(f"Original debug: {config.debug}")
    print(f"Production debug: {prod_config.debug}")
    print(f"Production is_production: {prod_config.is_production}")
    
    print("\n" + "="*80)
    print("4. IMMUTABLE LIBRARY WITH NESTED OBJECTS")
    print("-"*40)
    
    # Create library
    library = Library(
        name="City Library",
        location="Main Street"
    )
    
    print(f"\nEmpty library: {library.name}, Books: {library.book_count}")
    
    # Add books (creates new library each time)
    library = library.add_book(book1)
    library = library.add_book(book2)
    
    print(f"\nAfter adding books:")
    print(f"Library: {library.name}")
    print(f"Book count: {library.book_count}")
    print(f"Total value: ${library.total_value:.2f}")
    
    # Find books
    print(f"\nBooks by George Orwell:")
    orwell_books = library.find_by_author("George Orwell")
    for book in orwell_books:
        print(f"  - {book.title}")
    
    # Create from dict
    print("\nCreating book from dictionary:")
    book_data = {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'pages': 218,
        'price': 15.99,
        'genres': ['Fiction', 'Classic']
    }
    book3 = ImmutableBook.create_from_dict(book_data)
    print(f"Created: {book3.book_info}")
    
    print("\n" + "="*80)
    print("5. ADVANTAGES OF IMMUTABLE OBJECTS")
    print("-"*40)
    
    print("""
    Advantages:
    1. Thread Safety: Can be safely shared between threads
    2. Predictable State: Objects don't change unexpectedly
    3. Hashable: Can be used as dictionary keys (if all fields are hashable)
    4. Cache Friendly: Safe to cache since state never changes
    5. Debugging: Easier to reason about
    6. Functional Programming: Works well with functional patterns
    """)
    
    # Demonstrate hashability
    print("\nHashability demonstration:")
    print(f"book1 hash: {hash(book1)}")
    print(f"book2 hash: {hash(book2)}")
    
    # Use as dictionary keys
    book_inventory = {
        book1: 5,
        book2: 3,
        book3: 7
    }
    print(f"\nUsing books as dictionary keys:")
    for book, quantity in book_inventory.items():
        print(f"  {book.title}: {quantity} copies")
    
    print("\n" + "="*80)
    print("6. COMMON PATTERNS & BEST PRACTICES")
    print("-"*40)
    
    print("""
    Immutable Design Patterns:
    
    1. Builder Pattern: Create complex objects step by step
    2. With-methods: Return new instances with changes
    3. Factory Methods: Create instances from different data sources
    4. Flyweight Pattern: Share immutable instances
    
    Best Practices:
    
    1. Use tuples instead of lists for collections
    2. Provide "with_" methods for common modifications
    3. Keep constructors simple
    4. Use @property for computed values
    5. Consider performance for large objects
    6. Document immutability clearly
    """)
    
    # Builder pattern example
    print("\nBuilder Pattern Example:")
    
    @dataclass(frozen=True)
    class DatabaseConfig:
        host: str
        port: int
        database: str
        username: str
        password: str
        pool_size: int = 10
        timeout: int = 30
        
        class Builder:
            def __init__(self):
                self._host = "localhost"
                self._port = 5432
                self._database = ""
                self._username = ""
                self._password = ""
                self._pool_size = 10
                self._timeout = 30
            
            def host(self, host: str) -> 'DatabaseConfig.Builder':
                self._host = host
                return self
            
            def port(self, port: int) -> 'DatabaseConfig.Builder':
                self._port = port
                return self
            
            def database(self, database: str) -> 'DatabaseConfig.Builder':
                self._database = database
                return self
            
            def credentials(self, username: str, password: str) -> 'DatabaseConfig.Builder':
                self._username = username
                self._password = password
                return self
            
            def pool_size(self, size: int) -> 'DatabaseConfig.Builder':
                self._pool_size = size
                return self
            
            def build(self) -> 'DatabaseConfig':
                return DatabaseConfig(
                    host=self._host,
                    port=self._port,
                    database=self._database,
                    username=self._username,
                    password=self._password,
                    pool_size=self._pool_size,
                    timeout=self._timeout
                )
    
    # Use builder
    db_config = (DatabaseConfig.Builder()
                 .host("db.example.com")
                 .port(5432)
                 .database("mydb")
                 .credentials("admin", "secret")
                 .pool_size(20)
                 .build())
    
    print(f"Database Config: {db_config.host}:{db_config.port}/{db_config.database}")
    
    print("\n" + "="*80)
    print("7. WHEN TO USE IMMUTABLE DATACLASSES")
    print("-"*40)
    
    print("""
    Use Immutable Classes When:
    
    1. Configuration objects
    2. Value objects (Money, DateRange, etc.)
    3. Data transfer objects (DTOs)
    4. Cached data
    5. Multi-threaded applications
    6. Functional programming style
    7. Objects used as dictionary keys
    
    Use Mutable Classes When:
    
    1. Objects with complex state transitions
    2. Performance-critical code
    3. Objects that represent real-world mutable entities
    4. When you need in-place modifications
    """)
    
    print("\n" + "="*80)
    print("8. PERFORMANCE CONSIDERATIONS")
    print("-"*40)
    
    print("""
    Performance Notes:
    
    1. Creating many modified copies can be expensive
    2. Consider using __slots__ for memory efficiency
    3. For large objects, consider using copy-on-write patterns
    4. Immutable objects can be safely cached and reused
    5. Python's interning can help with small, frequently used objects
    """)
    
    # Final demonstration
    print("\n" + "="*80)
    print("FINAL DEMONSTRATION: IMMUTABLE VS MUTABLE")
    print("-"*40)
    
    @dataclass
    class MutableBook:
        title: str
        author: str
        price: float
    
    @dataclass(frozen=True)
    class AnotherImmutableBook:
        title: str
        author: str
        price: float
        
        def with_price(self, new_price: float) -> 'AnotherImmutableBook':
            return replace(self, price=new_price)
    
    print("\nMutable book (can modify in-place):")
    mutable = MutableBook("Mutable Book", "Author", 29.99)
    mutable.price = 19.99  # Direct modification
    print(f"Price changed to: ${mutable.price:.2f}")
    
    print("\nImmutable book (must create new instance):")
    immutable = AnotherImmutableBook("Immutable Book", "Author", 29.99)
    new_immutable = immutable.with_price(19.99)  # Returns new instance
    print(f"Original price: ${immutable.price:.2f}")
    print(f"New instance price: ${new_immutable.price:.2f}")
    print(f"Original unchanged: ${immutable.price:.2f}")