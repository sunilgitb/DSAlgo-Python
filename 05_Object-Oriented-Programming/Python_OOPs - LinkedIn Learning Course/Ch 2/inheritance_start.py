# Python Object Oriented Programming
# Understanding class inheritance

# Current implementation without inheritance
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages
    
    def get_info(self):
        return f'Book: "{self.title}" by {self.author}, {self.pages} pages, ${self.price:.2f}'


class Magazine:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.period = period
        self.publisher = publisher
    
    def get_info(self):
        return f'Magazine: "{self.title}", Publisher: {self.publisher}, Period: {self.period}, ${self.price:.2f}'


class Newspaper:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.period = period
        self.publisher = publisher
    
    def get_info(self):
        return f'Newspaper: "{self.title}", Publisher: {self.publisher}, Period: {self.period}, ${self.price:.2f}'


print("Current Implementation WITHOUT Inheritance:")
print("=" * 80)

# Create instances
b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print("\n1. Current implementation output:")
print(f"   b1.author: {b1.author}")
print(f"   n1.publisher: {n1.publisher}")
print(f"   b1.price, m1.price, n1.price: {b1.price}, {m1.price}, {n1.price}")

print("\n2. Using class methods:")
print(f"   {b1.get_info()}")
print(f"   {n1.get_info()}")
print(f"   {m1.get_info()}")

print("\n" + "=" * 80)
print("\nProblems with current implementation:")
print("• Code duplication - all classes have title and price")
print("• No common interface for publications")
print("• Can't treat different publications uniformly")
print("• Adding new features requires updating all classes")

print("\n" + "=" * 80)
print("\nImproved Implementation WITH Inheritance:")

# Base class with common attributes
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def get_info(self):
        return f'"{self.title}" - ${self.price:.2f}'
    
    def apply_discount(self, discount_percent):
        """Apply discount to price"""
        self.price -= self.price * (discount_percent / 100)
        return self.price


# Book inherits from Publication
class BookWithInheritance(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)  # Call parent constructor
        self.author = author
        self.pages = pages
    
    def get_info(self):
        base_info = super().get_info()
        return f'Book: {base_info}, Author: {self.author}, Pages: {self.pages}'


# Periodical base class for magazines and newspapers
class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period


class MagazineWithInheritance(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)
    
    def get_info(self):
        base_info = super().get_info()
        return f'Magazine: {base_info}, Publisher: {self.publisher}, Period: {self.period}'


class NewspaperWithInheritance(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)
    
    def get_info(self):
        base_info = super().get_info()
        return f'Newspaper: {base_info}, Publisher: {self.publisher}, Period: {self.period}'

print("\n3. Creating instances with inheritance:")
b2 = BookWithInheritance("1984", "George Orwell", 328, 24.99)
n2 = NewspaperWithInheritance("The Guardian", "Guardian Media Group", 3.50, "Daily")
m2 = MagazineWithInheritance("National Geographic", "National Geographic Society", 8.99, "Monthly")

print(f"\n   {b2.get_info()}")
print(f"   {n2.get_info()}")
print(f"   {m2.get_info()}")

print("\n4. Benefits of inheritance:")
print(f"   Common method from Publication: apply_discount()")
print(f"   Original price: ${b2.price}")
print(f"   After 20% discount: ${b2.apply_discount(20):.2f}")
print(f"   After another 10% discount: ${b2.apply_discount(10):.2f}")

print("\n" + "=" * 80)
print("\n5. Polymorphism with inheritance:")

print("\n   Creating a list of different publications:")
publications = [
    BookWithInheritance("To Kill a Mockingbird", "Harper Lee", 324, 29.95),
    MagazineWithInheritance("Time", "Time USA, LLC", 5.99, "Weekly"),
    NewspaperWithInheritance("Wall Street Journal", "News Corp", 4.25, "Daily"),
    BookWithInheritance("The Great Gatsby", "F. Scott Fitzgerald", 180, 19.99),
    MagazineWithInheritance("Scientific American", "Springer Nature", 5.99, "Monthly")
]

print("\n   Processing all publications uniformly:")
for pub in publications:
    print(f"   • {pub.get_info()}")

print("\n   Total value of publications:")
total_value = sum(pub.price for pub in publications)
print(f"   ${total_value:.2f}")

print("\n" + "=" * 80)
print("\n6. Adding more functionality with inheritance:")

class EBook(BookWithInheritance):
    def __init__(self, title, author, pages, price, file_format, file_size):
        super().__init__(title, author, pages, price)
        self.file_format = file_format
        self.file_size = file_size  # in MB
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Format: {self.file_format}, Size: {self.file_size}MB"
    
    def calculate_download_time(self, speed_mbps=10):
        """Calculate download time in seconds"""
        file_size_bits = self.file_size * 8 * 1024 * 1024  # Convert MB to bits
        return file_size_bits / (speed_mbps * 1024 * 1024)  # Convert Mbps to bps

print("\n   Creating EBook (inherits from Book):")
ebook1 = EBook("Digital Fortress", "Dan Brown", 510, 14.99, "EPUB", 2.5)
print(f"   {ebook1.get_info()}")
print(f"   Download time at 10 Mbps: {ebook1.calculate_download_time():.1f} seconds")
print(f"   Download time at 50 Mbps: {ebook1.calculate_download_time(50):.1f} seconds")

print("\n" + "=" * 80)
print("\n7. Library system using inheritance:")

class Library:
    def __init__(self, name):
        self.name = name
        self.collection = []
    
    def add_publication(self, publication):
        """Add any publication to the library"""
        self.collection.append(publication)
        return f'Added "{publication.title}" to {self.name}'
    
    def get_total_value(self):
        """Calculate total value of all publications"""
        return sum(pub.price for pub in self.collection)
    
    def apply_library_discount(self, discount_percent):
        """Apply discount to all publications in library"""
        for pub in self.collection:
            pub.apply_discount(discount_percent)
        return f"Applied {discount_percent}% discount to all items"
    
    def list_collection(self):
        """List all publications in library"""
        if not self.collection:
            return f"{self.name} has no publications"
        
        result = f"Collection at {self.name}:\n"
        for i, pub in enumerate(self.collection, 1):
            result += f"  {i}. {pub.get_info()}\n"
        result += f"\n  Total value: ${self.get_total_value():.2f}"
        return result

print("\n   Creating a library:")
city_library = Library("City Central Library")

print("\n   Adding publications to library:")
library_publications = [
    BookWithInheritance("Brave New World", "Aldous Huxley", 311, 29.0),
    NewspaperWithInheritance("NY Times", "New York Times Company", 6.0, "Daily"),
    MagazineWithInheritance("Scientific American", "Springer Nature", 5.99, "Monthly"),
    BookWithInheritance("1984", "George Orwell", 328, 24.99),
    EBook("The Da Vinci Code", "Dan Brown", 454, 12.99, "PDF", 3.2)
]

for pub in library_publications:
    print(f"   {city_library.add_publication(pub)}")

print(f"\n   {city_library.list_collection()}")

print("\n   Applying library-wide 15% discount:")
print(f"   {city_library.apply_library_discount(15)}")
print(f"\n   {city_library.list_collection()}")

print("\n" + "=" * 80)
print("\n8. Comparing the two approaches:")

print("\n   Without inheritance:")
print("   • Each class defines title and price separately")
print("   • Duplicate code for common attributes")
print("   • No common interface")
print("   • Hard to add new features to all publications")

print("\n   With inheritance:")
print("   • Common attributes in base class")
print("   • Code reuse through inheritance")
print("   • Polymorphism enables uniform treatment")
print("   • Easy to add new features to base class")
print("   • Type hierarchy reflects real-world relationships")

print("\n" + "=" * 80)
print("\n9. Testing type checking with inheritance:")

print("\n   Checking instance types:")
test_pub = BookWithInheritance("Test Book", "Test Author", 100, 9.99)
print(f"   isinstance(test_pub, BookWithInheritance): {isinstance(test_pub, BookWithInheritance)}")
print(f"   isinstance(test_pub, Publication): {isinstance(test_pub, Publication)}")
print(f"   isinstance(test_pub, object): {isinstance(test_pub, object)}")

print(f"\n   Checking EBook inheritance:")
test_ebook = EBook("Test EBook", "Test Author", 200, 14.99, "EPUB", 1.5)
print(f"   isinstance(test_ebook, EBook): {isinstance(test_ebook, EBook)}")
print(f"   isinstance(test_ebook, BookWithInheritance): {isinstance(test_ebook, BookWithInheritance)}")
print(f"   isinstance(test_ebook, Publication): {isinstance(test_ebook, Publication)}")

print("\n" + "=" * 80)
print("\n10. Original example with enhanced output:")

print("\n   Original example recreation:")
orig_b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
orig_n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
orig_m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(f"\n   Original output:")
print(f"   b1.author: {orig_b1.author}")
print(f"   n1.publisher: {orig_n1.publisher}")
print(f"   b1.price, m1.price, n1.price: {orig_b1.price}, {orig_m1.price}, {orig_n1.price}")

print(f"\n   Enhanced output with methods:")
print(f"   {orig_b1.get_info()}")
print(f"   {orig_n1.get_info()}")
print(f"   {orig_m1.get_info()}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Without inheritance: Code duplication, no common interface")
print("✓ With inheritance: Code reuse, polymorphism, type hierarchy")
print("✓ Base class (Publication) defines common attributes/methods")
print("✓ Subclasses specialize base class functionality")
print("✓ super().__init__() calls parent constructor")
print("✓ Methods can be overridden in subclasses")
print("✓ Inheritance enables treating different types uniformly")
print("✓ Real-world relationships are reflected in class hierarchy")