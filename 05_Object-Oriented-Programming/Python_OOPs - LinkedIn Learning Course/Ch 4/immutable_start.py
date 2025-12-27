# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass, field, replace
from typing import List, Tuple, ClassVar
import copy

# TODO: "The "frozen" parameter makes the class immutable
@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0
    value3: List[str] = field(default_factory=list)  # Use tuple for truly immutable, but list with default_factory works
    
    # Class variables are NOT immutable (they're shared across instances)
    instance_count: ClassVar[int] = 0
    
    def __post_init__(self):
        """Called after initialization. Can't modify instance attributes!"""
        # We can modify class variables
        type(self).instance_count += 1
        
        # But we CANNOT modify instance attributes, even here
        # The following would cause FrozenInstanceError:
        # self.value1 = "Modified in post_init"
    
    def display(self):
        """Read-only method - can access but not modify."""
        return f"value1={self.value1}, value2={self.value2}, value3={self.value3}"
    
    def attempt_modification(self, new_value):
        """This method will fail if it tries to modify attributes."""
        print(f"  Attempting to modify value2 from {self.value2} to {new_value}...")
        # This would cause FrozenInstanceError:
        # self.value2 = new_value
        return "Cannot modify - object is immutable"
    
    def create_modified_copy(self, **changes):
        """Proper way to 'modify' an immutable object - create a new one."""
        return replace(self, **changes)


# Another example showing practical immutability
@dataclass(frozen=True)
class ImmutableBook:
    title: str
    author: str
    pages: int
    price: float
    genres: Tuple[str, ...] = field(default_factory=tuple)  # Tuple is immutable
    
    def __post_init__(self):
        """Validation can still be done, carefully."""
        if self.pages <= 0:
            # We can't do: self.pages = 1
            # Instead, we need to use object.__setattr__ for post-init setup
            object.__setattr__(self, 'pages', 1)
    
    @property
    def price_per_page(self):
        return self.price / self.pages if self.pages > 0 else 0
    
    def with_discount(self, percent: float):
        """Return a new book with discounted price."""
        new_price = self.price * (1 - percent/100)
        return replace(self, price=new_price)
    
    def add_genre(self, genre: str):
        """Return a new book with added genre."""
        new_genres = self.genres + (genre,)
        return replace(self, genres=new_genres)


# Driver code
if __name__ == "__main__":
    print("="*80)
    print("IMMUTABLE DATA CLASS DEMONSTRATION")
    print("="*80)
    
    # Create an instance
    obj = ImmutableClass()
    print(f"\n1. CREATED OBJECT: {obj}")
    print(f"   Class variable (instance_count): {ImmutableClass.instance_count}")
    
    # Access attribute
    print(f"\n2. ACCESSING ATTRIBUTE: obj.value1 = {obj.value1}")
    
    print("\n3. ATTEMPTING TO MODIFY ATTRIBUTES DIRECTLY")
    print("-"*40)
    
    # TODO: attempting to change the value of an immutable class throws an exception
    print("\na) Trying to modify value1:")
    try:
        obj.value1 = "Another value"
        print(f"   Successfully changed to: {obj.value1}")
    except Exception as e:
        print(f"   ❌ ERROR: {type(e).__name__}: {e}")
    
    print("\nb) Trying to modify value2:")
    try:
        obj.value2 = 42
        print(f"   Successfully changed to: {obj.value2}")
    except Exception as e:
        print(f"   ❌ ERROR: {type(e).__name__}: {e}")
    
    print("\nc) Trying to modify the list value3:")
    try:
        obj.value3.append("new item")  # This might work since list is mutable internally
        print(f"   List after append: {obj.value3}")
        print("   ⚠️  Note: The list itself is mutable, but obj.value3 reference is frozen")
    except Exception as e:
        print(f"   ❌ ERROR: {type(e).__name__}: {e}")
    
    print("\n" + "="*80)
    print("4. METHODS CAN'T MODIFY ATTRIBUTES EITHER")
    print("-"*40)
    
    # TODO: even functions within the class can't change anything
    print("\nCalling method that attempts modification:")
    result = obj.attempt_modification(99)
    print(f"   Result: {result}")
    print(f"   value2 is still: {obj.value2}")
    
    print("\n" + "="*80)
    print("5. PROPER WAY TO WORK WITH IMMUTABLE OBJECTS")
    print("-"*40)
    
    print("\na) Creating a modified copy using replace():")
    modified_obj = obj.create_modified_copy(value1="Modified Value", value2=100)
    print(f"   Original object: {obj}")
    print(f"   Modified copy: {modified_obj}")
    print(f"   Are they the same object? {obj is modified_obj}")
    print(f"   Are they equal? {obj == modified_obj}")
    
    print(f"\nb) Instance count (should be 2 now): {ImmutableClass.instance_count}")
    
    print("\n" + "="*80)
    print("6. PRACTICAL EXAMPLE: IMMUTABLE BOOK")
    print("-"*40)
    
    # Create an immutable book
    book = ImmutableBook(
        title="1984",
        author="George Orwell",
        pages=328,
        price=19.95,
        genres=("Dystopian", "Political")
    )
    
    print(f"\nCreated book: {book}")
    print(f"Price per page: ${book.price_per_page:.4f}")
    
    print("\nTrying to modify book directly:")
    try:
        book.price = 9.99
    except Exception as e:
        print(f"   ❌ ERROR: {type(e).__name__}: {e}")
    
    print("\nCreating modified copies properly:")
    
    # Apply discount (creates new book)
    discounted_book = book.with_discount(20)
    print(f"\na) Applying 20% discount:")
    print(f"   Original price: ${book.price:.2f}")
    print(f"   Discounted price: ${discounted_book.price:.2f}")
    print(f"   Original unchanged: ${book.price:.2f}")
    
    # Add genre (creates new book)
    book_with_genre = book.add_genre("Classic")
    print(f"\nb) Adding 'Classic' genre:")
    print(f"   Original genres: {book.genres}")
    print(f"   New genres: {book_with_genre.genres}")
    
    print("\n" + "="*80)
    print("7. WHY USE IMMUTABLE CLASSES?")
    print("-"*40)
    
    print("""
    Benefits of Immutability:
    
    1. Thread Safety: Multiple threads can read without synchronization
    2. Predictable State: Objects don't change unexpectedly
    3. Hashable: Can be used as dictionary keys (if all fields are hashable)
    4. Cache Friendly: Safe to cache since state never changes
    5. Easier Debugging: No side effects to track
    6. Functional Programming: Works well with functional patterns
    
    Common Use Cases:
    • Configuration/settings objects
    • Data transfer objects (DTOs)
    • Value objects (Money, DateRange, etc.)
    • Cache keys
    • Multi-threaded applications
    """)
    
    # Demonstrate hashability
    print("\n8. HASHABILITY (for dictionary keys):")
    
    @dataclass(frozen=True)
    class HashablePoint:
        x: int
        y: int
    
    @dataclass  # Not frozen
    class MutablePoint:
        x: int
        y: int
    
    # Create instances
    immutable_point = HashablePoint(1, 2)
    mutable_point = MutablePoint(1, 2)
    
    print(f"\nImmutable point hash: {hash(immutable_point)}")
    
    try:
        print(f"Mutable point hash: {hash(mutable_point)}")
    except Exception as e:
        print(f"Mutable point hash: ❌ {type(e).__name__}: {e}")
        print("  (Mutable objects can't be hashed by default)")
    
    # Use as dictionary keys
    print("\nUsing as dictionary keys:")
    point_dict = {immutable_point: "Immutable point"}
    print(f"  Dictionary with immutable key: {point_dict}")
    
    print("\n" + "="*80)
    print("9. COMPARISON: MUTABLE VS IMMUTABLE")
    print("-"*40)
    
    @dataclass
    class MutableConfig:
        host: str = "localhost"
        port: int = 8080
        timeout: int = 30
    
    @dataclass(frozen=True)
    class ImmutableConfig:
        host: str = "localhost"
        port: int = 8080
        timeout: int = 30
        
        def with_changes(self, **kwargs):
            return replace(self, **kwargs)
    
    print("\nMutable config (can be modified in-place):")
    mutable_config = MutableConfig()
    mutable_config.port = 9000
    print(f"  Changed port to: {mutable_config.port}")
    
    print("\nImmutable config (must create new instance):")
    immutable_config = ImmutableConfig()
    new_config = immutable_config.with_changes(port=9000)
    print(f"  Original port: {immutable_config.port}")
    print(f"  New config port: {new_config.port}")
    
    print("\n" + "="*80)
    print("10. COMMON PITFALLS AND SOLUTIONS")
    print("-"*40)
    
    print("""
    Pitfall 1: Mutable fields in immutable classes
    Solution: Use tuples or frozen dataclasses for nested objects
    
    Pitfall 2: Trying to modify in __post_init__
    Solution: Use object.__setattr__ carefully, or validate in factory method
    
    Pitfall 3: Performance when creating many copies
    Solution: Consider using copy-on-write or builder patterns
    
    Pitfall 4: Forgetting @dataclass(frozen=True)
    Solution: Always test immutability in your tests
    """)
    
    # Demonstrate pitfall with mutable fields
    print("\nDemonstrating mutable field pitfall:")
    
    @dataclass(frozen=True)
    class ProblematicImmutable:
        name: str
        items: List[str] = field(default_factory=list)  # List is mutable!
    
    obj1 = ProblematicImmutable("Object 1")
    print(f"\nCreated: {obj1}")
    
    # Even though the class is frozen, the list inside can be modified!
    # This is because the list object itself is mutable
    obj1.items.append("item1")  # This might work!
    print(f"After appending to list: {obj1}")
    
    print("\n" + "="*80)
    print("11. BEST PRACTICES FOR TRUE IMMUTABILITY")
    print("-"*40)
    
    print("""
    For True Immutability:
    
    1. Always use @dataclass(frozen=True)
    2. Use tuples instead of lists
    3. Use frozenset instead of set
    4. Use immutable types for all fields
    5. For nested objects, ensure they're also immutable
    6. Provide 'with_' methods for common modifications
    7. Use factory methods for complex construction
    8. Document immutability clearly
    """)
    
    # Final demonstration
    print("\n" + "="*80)
    print("FINAL TEST: VERIFYING IMMUTABILITY")
    print("-"*40)
    
    test_obj = ImmutableClass(value1="Test", value2=123)
    
    print(f"\nCreated test object: {test_obj}")
    
    # Test all modification attempts
    modification_attempts = [
        ("Direct assignment", lambda: setattr(test_obj, 'value1', 'Changed')),
        ("Attribute assignment", lambda: exec("test_obj.value2 = 999")),
        ("Dictionary assignment", lambda: test_obj.__dict__.update({'value1': 'Hacked'})),
        ("Del attribute", lambda: delattr(test_obj, 'value1')),
    ]
    
    for description, attempt in modification_attempts:
        print(f"\n{description}:")
        try:
            attempt()
            print(f"  ✅ Modification succeeded (unexpected!)")
            print(f"  Object is now: {test_obj}")
        except Exception as e:
            print(f"  ❌ {type(e).__name__}: {e}")
            print(f"  Object unchanged: {test_obj}")
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    print(f"""
    Key Takeaways:
    
    1. Use @dataclass(frozen=True) to make classes immutable
    2. Once created, instance attributes cannot be modified
    3. Even class methods cannot modify instance attributes
    4. To "modify", create a new instance using replace()
    5. Immutable objects are thread-safe and hashable
    6. Watch out for mutable fields inside immutable classes
    
    In your code:
    • Added frozen=True parameter to @dataclass
    • Demonstrated that modification attempts throw FrozenInstanceError
    • Showed that methods also cannot modify attributes
    • Provided proper patterns for working with immutable objects
    """)