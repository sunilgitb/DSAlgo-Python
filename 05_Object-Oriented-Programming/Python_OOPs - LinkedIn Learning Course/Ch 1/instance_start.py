# Python Object Oriented Programming
# Using instance methods and attributes

class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author="Unknown", pages=0, price=0.0):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret_id = hash(title + author)  # Private attribute
        self._discount = 0.0  # Protected attribute (convention)

    # TODO: create instance methods
    def set_discount(self, discount_percent):
        """Set a discount percentage (0-100)"""
        if 0 <= discount_percent <= 100:
            self._discount = discount_percent / 100.0
            return f"Discount set to {discount_percent}%"
        else:
            raise ValueError("Discount must be between 0 and 100")

    def get_price(self):
        """Get price after applying discount if any"""
        if self._discount > 0:
            discounted_price = self.price * (1 - self._discount)
            return round(discounted_price, 2)
        return self.price

    def get_book_info(self):
        """Return formatted book information"""
        price_info = f"${self.get_price()}"
        if self._discount > 0:
            price_info += f" (Original: ${self.price}, Save: {self._discount*100:.0f}%)"
        
        return f'"{self.title}" by {self.author}, {self.pages} pages, {price_info}'

    def apply_tax(self, tax_rate=0.08):
        """Calculate price with tax"""
        price_with_tax = self.get_price() * (1 + tax_rate)
        return round(price_with_tax, 2)

    def __str__(self):
        """String representation of the book"""
        return self.get_book_info()


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("1984", "George Orwell", 328, 24.99)
b4 = Book("Pride and Prejudice", "Jane Austen", 432, 19.99)

print("Testing Book Class with Instance Methods and Attributes:")
print("=" * 80)

# TODO: print the price of book1
print("1. Book instances created:")
print(f"   b1: {b1}")
print(f"   b2: {b2}")
print(f"   b3: {b3}")
print(f"   b4: {b4}")

print("\n2. Getting prices:")
print(f"   b1.get_price(): ${b1.get_price()}")
print(f"   b2.get_price(): ${b2.get_price()}")
print(f"   b3.get_price(): ${b3.get_price()}")

print("\n" + "=" * 80)

# TODO: try setting the discount
print("3. Setting and testing discounts:")

print("\n   Setting 25% discount on b2:")
try:
    result = b2.set_discount(25)
    print(f"   {result}")
    print(f"   b2.get_price() after discount: ${b2.get_price()}")
except ValueError as e:
    print(f"   Error: {e}")

print("\n   Setting 50% discount on b3:")
try:
    b3.set_discount(50)
    print(f"   b3.get_price() after discount: ${b3.get_price()}")
except ValueError as e:
    print(f"   Error: {e}")

print("\n   Trying invalid discount (150%):")
try:
    b4.set_discount(150)
    print(f"   ✗ Unexpectedly succeeded")
except ValueError as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 80)
print("\n4. Current book information:")
print(f"   b1: {b1}")
print(f"   b2: {b2}")
print(f"   b3: {b3}")
print(f"   b4: {b4}")

print("\n5. Testing with taxes:")
print(f"   b1 with 8% tax: ${b1.apply_tax(0.08)}")
print(f"   b2 with 8% tax: ${b2.apply_tax(0.08)}")
print(f"   b3 with 8% tax: ${b3.apply_tax(0.08)}")

print("\n" + "=" * 80)

# TODO: properties with double underscores are hidden by the interpreter
print("6. Testing attribute visibility:")

print("\n   Public attributes (accessible):")
print(f"   b1.title: {b1.title}")
print(f"   b1.author: {b1.author}")
print(f"   b1.pages: {b1.pages}")
print(f"   b1.price: ${b1.price}")

print("\n   Protected attribute (single underscore - convention):")
print(f"   b2._discount: {b2._discount}")

print("\n   Private attribute (double underscore - name mangling):")
try:
    print(f"   b1.__secret_id: {b1.__secret_id}")
except AttributeError as e:
    print(f"   ✓ Cannot access directly: {e}")

print("\n   Name-mangled private attribute (not recommended):")
# Python does name mangling: __secret_id becomes _Book__secret_id
print(f"   Has attribute _Book__secret_id: {hasattr(b1, '_Book__secret_id')}")

print("\n   Checking attribute existence:")
print(f"   hasattr(b1, 'title'): {hasattr(b1, 'title')}")
print(f"   hasattr(b1, '_discount'): {hasattr(b1, '_discount')}")
print(f"   hasattr(b2, '_discount'): {hasattr(b2, '_discount')}")
print(f"   hasattr(b1, '__secret_id'): {hasattr(b1, '__secret_id')}")

print("\n" + "=" * 80)
print("\n7. Advanced example - Bookstore inventory:")

class Bookstore:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def add_book(self, book, quantity=1):
        for _ in range(quantity):
            self.inventory.append(book)
        return f'Added {quantity} copy/copies of "{book.title}"'
    
    def total_value(self):
        total = sum(book.get_price() for book in self.inventory)
        return round(total, 2)
    
    def apply_storewide_discount(self, discount_percent):
        for book in self.inventory:
            try:
                book.set_discount(discount_percent)
            except ValueError:
                pass  # Skip books that can't have this discount
        return f"Storewide discount of {discount_percent}% applied"
    
    def list_inventory(self):
        if not self.inventory:
            return f"{self.name} has no books in stock"
        
        # Count unique books
        book_counts = {}
        for book in self.inventory:
            key = f"{book.title} by {book.author}"
            book_counts[key] = book_counts.get(key, 0) + 1
        
        result = f"Inventory of {self.name}:\n"
        for book_info, count in book_counts.items():
            result += f"   {count}x {book_info}\n"
        result += f"\n   Total value: ${self.total_value()}"
        return result

print("\n   Creating a bookstore:")
chapter_verse = Bookstore("Chapter & Verse")

print("\n   Adding books to inventory:")
print(f"   {chapter_verse.add_book(b1, 3)}")
print(f"   {chapter_verse.add_book(b2, 2)}")
print(f"   {chapter_verse.add_book(b3, 1)}")
print(f"   {chapter_verse.add_book(b4, 4)}")

print(f"\n   {chapter_verse.list_inventory()}")

print("\n   Applying storewide 20% discount:")
print(f"   {chapter_verse.apply_storewide_discount(20)}")
print(f"\n   {chapter_verse.list_inventory()}")

print("\n" + "=" * 80)
print("\n8. Demonstrating encapsulation benefits:")

print("\n   Creating a book with validation:")

class ValidatedBook(Book):
    def __init__(self, title, author="Unknown", pages=0, price=0.0, isbn=""):
        # Validate inputs
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")
        if pages < 0:
            raise ValueError("Pages cannot be negative")
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        super().__init__(title, author, pages, price)
        self.isbn = isbn
    
    def set_discount(self, discount_percent):
        """Override with additional validation"""
        if discount_percent > 50:
            raise ValueError("Discount cannot exceed 50% for this book")
        return super().set_discount(discount_percent)

print("\n   Testing validated book:")
try:
    validated_book = ValidatedBook("Valid Book", "Author Name", 300, 29.99, "123-4567890123")
    print(f"   Created: {validated_book}")
    
    print("\n   Setting 40% discount:")
    validated_book.set_discount(40)
    print(f"   Price after discount: ${validated_book.get_price()}")
    
    print("\n   Trying 60% discount (should fail):")
    validated_book.set_discount(60)
    print(f"   ✗ Unexpectedly succeeded")
except ValueError as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n   Testing invalid book creation:")
try:
    invalid_book = ValidatedBook("", "Author", -100, -10)
    print(f"   ✗ Unexpectedly created: {invalid_book}")
except ValueError as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 80)
print("\n9. Testing the original requirements:")

print("\n   Original example recreation:")
original_b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
original_b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

print(f"\n   Price of book1: ${original_b1.get_price()}")
print(f"   Price of book2 before discount: ${original_b2.get_price()}")

original_b2.set_discount(25)
print(f"   Price of book2 after 25% discount: ${original_b2.get_price()}")

print(f"\n   Protected attribute access: original_b2._discount = {original_b2._discount}")

print("\n   Trying to access private attribute (should fail):")
try:
    print(f"   original_b2.__secret_id: {original_b2.__secret_id}")
except AttributeError as e:
    print(f"   ✓ AttributeError: {e}")

print("\n   Name-mangled access attempt:")
print(f"   Has attribute _Book__secret_id: {hasattr(original_b2, '_Book__secret_id')}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Instance attributes store object-specific data")
print("✓ Instance methods operate on individual objects")
print("✓ self refers to the current instance")
print("✓ Public attributes are freely accessible")
print("✓ Protected attributes (_single) are a naming convention")
print("✓ Private attributes (__double) use name mangling for privacy")
print("✓ Encapsulation protects internal implementation")
print("✓ Methods can validate and control attribute access")