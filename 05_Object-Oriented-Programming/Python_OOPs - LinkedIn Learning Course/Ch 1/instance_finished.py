# Python Object Oriented Programming
# Using instance methods and attributes

class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"
        self.__internal_id = id(self)  # Using object's memory address as ID

    # instance methods are defined like any other function, with the
    # first argument as the object ("self" is just a convention)
    def setDiscount(self, amount):
        """Set a discount percentage (0 to 1)"""
        if 0 <= amount <= 1:
            self._discount = amount
            return f"Discount of {amount*100}% set successfully"
        else:
            raise ValueError("Discount must be between 0 and 1")

    def getPrice(self):
        """Get the current price after applying discount if any"""
        if hasattr(self, "_discount"):
            discounted_price = self.price - (self.price * self._discount)
            return round(discounted_price, 2)
        else:
            return self.price

    def apply_tax(self, tax_rate):
        """Calculate price with tax"""
        if 0 <= tax_rate <= 1:
            price_with_tax = self.getPrice() * (1 + tax_rate)
            return round(price_with_tax, 2)
        else:
            raise ValueError("Tax rate must be between 0 and 1")

    def get_book_info(self):
        """Return formatted book information"""
        return f'"{self.title}" by {self.author}, {self.pages} pages, ${self.getPrice()}'

    def __str__(self):
        """String representation of the book"""
        return self.get_book_info()


print("Testing Book Class with Instance Methods and Attributes:")
print("=" * 80)

# create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("1984", "George Orwell", 328, 24.99)
b4 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, 19.99)

print("1. Created book instances:")
print(f"   b1: {b1}")
print(f"   b2: {b2}")
print(f"   b3: {b3}")
print(f"   b4: {b4}")

print("\n2. Testing getPrice() method:")
print(f"   b1.getPrice(): ${b1.getPrice()}")
print(f"   b2.getPrice(): ${b2.getPrice()}")
print(f"   b3.getPrice(): ${b3.getPrice()}")

print("\n3. Setting and testing discounts:")
print("   Setting 25% discount on b2:")
try:
    result = b2.setDiscount(0.25)
    print(f"   {result}")
    print(f"   b2.getPrice() after discount: ${b2.getPrice()}")
    print(f"   Original price: ${b2.price}, Discounted: ${b2.getPrice()}")
    print(f"   Savings: ${b2.price - b2.getPrice():.2f}")
except ValueError as e:
    print(f"   Error: {e}")

print("\n   Setting 50% discount on b3:")
try:
    b3.setDiscount(0.50)
    print(f"   b3.getPrice() after discount: ${b3.getPrice()}")
except ValueError as e:
    print(f"   Error: {e}")

print("\n   Trying to set invalid discount (150%):")
try:
    b4.setDiscount(1.5)
    print(f"   ✗ Unexpectedly succeeded")
except ValueError as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 80)
print("\n4. Testing with taxes:")

print("\n   Calculating prices with 8% sales tax:")
print(f"   b1 with tax: ${b1.apply_tax(0.08)}")
print(f"   b2 with tax: ${b2.apply_tax(0.08)}")
print(f"   b3 with tax: ${b3.apply_tax(0.08)}")

print("\n   Calculating with different tax rates:")
tax_rates = [0.05, 0.10, 0.15]
for rate in tax_rates:
    tax_amount = b1.getPrice() * rate
    total = b1.getPrice() + tax_amount
    print(f"   b1 with {rate*100}% tax: ${total:.2f} (tax: ${tax_amount:.2f})")

print("\n" + "=" * 80)
print("\n5. Testing attribute access:")

print("\n   Public attributes (can be accessed directly):")
print(f"   b1.title: {b1.title}")
print(f"   b1.author: {b1.author}")
print(f"   b1.pages: {b1.pages}")
print(f"   b1.price: ${b1.price}")

print("\n   Protected attribute (single underscore convention):")
print(f"   b2._discount: {b2._discount}")  # Can be accessed but shouldn't be

print("\n   Private attributes (double underscore - name mangling):")
try:
    print(f"   b2.__secret: {b2.__secret}")
except AttributeError as e:
    print(f"   ✓ Cannot access directly: {e}")

print("\n   Name-mangled private attribute (not recommended):")
try:
    # Python does name mangling: __secret becomes _Book__secret
    print(f"   b2._Book__secret: {b2._Book__secret}")
except AttributeError:
    print("   Cannot access even with name mangling")

print("\n   Checking if attributes exist:")
print(f"   hasattr(b1, 'title'): {hasattr(b1, 'title')}")
print(f"   hasattr(b1, '_discount'): {hasattr(b1, '_discount')}")
print(f"   hasattr(b2, '_discount'): {hasattr(b2, '_discount')}")
print(f"   hasattr(b1, '__secret'): {hasattr(b1, '__secret')}")

print("\n" + "=" * 80)
print("\n6. Modifying attributes:")

print("\n   Direct attribute modification:")
print(f"   b1.price before: ${b1.price}")
b1.price = 34.95
print(f"   b1.price after: ${b1.price}")
print(f"   b1.getPrice(): ${b1.getPrice()}")

print("\n   Setting multiple discounts:")
print(f"   b4 price: ${b4.price}")
b4.setDiscount(0.10)
print(f"   After 10% discount: ${b4.getPrice()}")
b4.setDiscount(0.20)  # Overwrites previous discount
print(f"   After 20% discount: ${b4.getPrice()}")

print("\n" + "=" * 80)
print("\n7. Bookstore inventory example:")

class Bookstore:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def add_book(self, book):
        self.inventory.append(book)
        return f'Added "{book.title}" to {self.name} inventory'
    
    def total_inventory_value(self):
        total = sum(book.getPrice() for book in self.inventory)
        return round(total, 2)
    
    def apply_storewide_discount(self, discount_rate):
        """Apply discount to all books in inventory"""
        for book in self.inventory:
            book.setDiscount(discount_rate)
        return f"Applied {discount_rate*100}% discount to all books"
    
    def list_inventory(self):
        if not self.inventory:
            return f"{self.name} has no books in inventory"
        
        result = f"Inventory of {self.name}:\n"
        for i, book in enumerate(self.inventory, 1):
            result += f"  {i}. {book.get_book_info()}\n"
        result += f"\n  Total inventory value: ${self.total_inventory_value()}"
        return result

print("\n   Creating a bookstore:")
my_bookstore = Bookstore("Chapter & Verse")

print("\n   Adding books to bookstore:")
books = [b1, b2, b3, b4]
for book in books:
    print(f"   {my_bookstore.add_book(book)}")

print(f"\n   {my_bookstore.list_inventory()}")

print("\n   Applying storewide discount of 15%:")
print(f"   {my_bookstore.apply_storewide_discount(0.15)}")
print(f"\n   {my_bookstore.list_inventory()}")

print("\n" + "=" * 80)
print("\n8. Additional instance methods:")

print("\n   Creating a specialized book with more methods:")

class EnhancedBook(Book):
    def __init__(self, title, author, pages, price, genre, edition=1):
        super().__init__(title, author, pages, price)
        self.genre = genre
        self.edition = edition
        self.reviews = []
    
    def add_review(self, rating, comment):
        """Add a review to the book"""
        if 1 <= rating <= 5:
            self.reviews.append({
                'rating': rating,
                'comment': comment
            })
            return "Review added successfully"
        else:
            raise ValueError("Rating must be between 1 and 5")
    
    def average_rating(self):
        """Calculate average rating from reviews"""
        if not self.reviews:
            return "No reviews yet"
        total = sum(review['rating'] for review in self.reviews)
        return round(total / len(self.reviews), 1)
    
    def get_book_info(self):
        """Enhanced book information"""
        base_info = super().get_book_info()
        return f"{base_info} | Genre: {self.genre} | Edition: {self.edition}"

print("\n   Creating enhanced book:")
enhanced_book = EnhancedBook(
    "Dune", 
    "Frank Herbert", 
    412, 
    34.99, 
    "Science Fiction", 
    1
)

print(f"   {enhanced_book.get_book_info()}")

print("\n   Adding reviews:")
try:
    print(f"   {enhanced_book.add_review(5, 'Masterpiece!')}")
    print(f"   {enhanced_book.add_review(4, 'Great world-building')}")
    print(f"   {enhanced_book.add_review(5, 'Best sci-fi novel ever')}")
except ValueError as e:
    print(f"   Error: {e}")

print(f"\n   Average rating: {enhanced_book.average_rating()}")

print("\n" + "=" * 80)
print("\n9. Testing the original example code:")

print("\n   Original example output:")
# Recreate original example
orig_b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
orig_b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

print(f"   b1.getPrice(): ${orig_b1.getPrice()}")
print(f"   b2.getPrice(): ${orig_b2.getPrice()}")
orig_b2.setDiscount(0.25)
print(f"   b2.getPrice() after 25% discount: ${orig_b2.getPrice()}")

print(f"\n   Accessing protected attribute: orig_b2._discount = {orig_b2._discount}")

print("\n   Trying to access private attribute (should fail):")
try:
    print(f"   orig_b2.__secret: {orig_b2.__secret}")
except AttributeError as e:
    print(f"   ✓ AttributeError: {e}")

print("\n   Name-mangled access (not recommended but possible):")
try:
    print(f"   orig_b2._Book__secret: {orig_b2._Book__secret}")
except:
    print("   Cannot access")

print("\n" + "=" * 80)
print("\nSummary of Instance Methods and Attributes:")
print("✓ Instance attributes store data specific to each object")
print("✓ Instance methods operate on specific object instances")
print("✓ self parameter refers to the instance being operated on")
print("✓ Public attributes can be accessed directly")
print("✓ Protected attributes (_single_underscore) are a convention")
print("✓ Private attributes (__double_underscore) use name mangling")
print("✓ hasattr() checks if an attribute exists")
print("✓ Methods can modify instance state")
print("✓ Encapsulation protects internal implementation details")