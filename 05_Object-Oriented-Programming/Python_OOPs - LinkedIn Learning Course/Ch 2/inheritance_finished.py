# Python Object Oriented Programming
# Understanding class inheritance

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def get_info(self):
        return f'"{self.title}" - ${self.price:.2f}'
    
    def __str__(self):
        return self.get_info()


class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Published by: {self.publisher}, Period: {self.period}"


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Author: {self.author}, Pages: {self.pages}"
    
    def calculate_reading_time(self, pages_per_hour=30):
        """Estimate reading time in hours"""
        return self.pages / pages_per_hour


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)
    
    def get_info(self):
        base_info = super().get_info()
        return f"[Magazine] {base_info}"


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)
    
    def get_info(self):
        base_info = super().get_info()
        return f"[Newspaper] {base_info}"


class EBook(Book):
    def __init__(self, title, author, pages, price, file_format, file_size):
        super().__init__(title, author, pages, price)
        self.file_format = file_format
        self.file_size = file_size  # in MB
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Format: {self.file_format}, Size: {self.file_size}MB"


print("Testing Class Inheritance Hierarchy:")
print("=" * 80)

print("\n1. Creating instances of different publication types:")
b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")
ebook1 = EBook("Digital Fortress", "Dan Brown", 510, 14.99, "EPUB", 2.5)

print(f"   Book: {b1}")
print(f"   Newspaper: {n1}")
print(f"   Magazine: {m1}")
print(f"   EBook: {ebook1}")

print("\n" + "=" * 80)
print("\n2. Accessing attributes from original example:")

print(f"\n   b1.author: {b1.author}")
print(f"   n1.publisher: {n1.publisher}")
print(f"   b1.price, m1.price, n1.price: {b1.price}, {m1.price}, {n1.price}")

print("\n" + "=" * 80)
print("\n3. Exploring the inheritance hierarchy:")

print(f"\n   Checking instance types:")
print(f"   isinstance(b1, Book): {isinstance(b1, Book)}")
print(f"   isinstance(b1, Publication): {isinstance(b1, Publication)}")
print(f"   isinstance(n1, Periodical): {isinstance(n1, Periodical)}")
print(f"   isinstance(n1, Publication): {isinstance(n1, Publication)}")
print(f"   isinstance(m1, Magazine): {isinstance(m1, Magazine)}")
print(f"   isinstance(m1, Periodical): {isinstance(m1, Periodical)}")

print(f"\n   Checking class relationships:")
print(f"   issubclass(Book, Publication): {issubclass(Book, Publication)}")
print(f"   issubclass(Magazine, Periodical): {issubclass(Magazine, Periodical)}")
print(f"   issubclass(Newspaper, Publication): {issubclass(Newspaper, Publication)}")
print(f"   issubclass(EBook, Book): {issubclass(EBook, Book)}")
print(f"   issubclass(EBook, Publication): {issubclass(EBook, Publication)}")

print("\n" + "=" * 80)
print("\n4. Method overriding and super() calls:")

print("\n   Using overridden get_info() method:")
print(f"   b1.get_info(): {b1.get_info()}")
print(f"   n1.get_info(): {n1.get_info()}")
print(f"   m1.get_info(): {m1.get_info()}")
print(f"   ebook1.get_info(): {ebook1.get_info()}")

print(f"\n   Book-specific method:")
print(f"   b1.calculate_reading_time(): {b1.calculate_reading_time():.1f} hours")
print(f"   b1.calculate_reading_time(40): {b1.calculate_reading_time(40):.1f} hours (faster reader)")

print("\n" + "=" * 80)
print("\n5. Creating more publications:")

print("\n   Creating additional publications:")
publications = [
    Book("1984", "George Orwell", 328, 24.99),
    Book("To Kill a Mockingbird", "Harper Lee", 324, 29.95),
    Magazine("National Geographic", "National Geographic Society", 8.99, "Monthly"),
    Magazine("Time", "Time USA, LLC", 5.99, "Weekly"),
    Newspaper("The Guardian", "Guardian Media Group", 3.50, "Daily"),
    Newspaper("Wall Street Journal", "News Corp", 4.25, "Daily"),
    EBook("The Da Vinci Code", "Dan Brown", 454, 12.99, "PDF", 3.2),
    EBook("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 320, 9.99, "MOBI", 1.8)
]

print(f"\n   All publications:")
for i, pub in enumerate(publications, 1):
    print(f"   {i}. {pub}")

print("\n" + "=" * 80)
print("\n6. Polymorphism in action:")

print("\n   Processing publications uniformly:")
print("   " + "-" * 50)

def process_publication(pub):
    """Process any type of publication"""
    print(f"   Processing: {pub.get_info()}")
    
    # Type-specific processing
    if isinstance(pub, Book):
        print(f"     • Reading time: {pub.calculate_reading_time():.1f} hours")
    if isinstance(pub, Periodical):
        print(f"     • Published by: {pub.publisher}")
    if isinstance(pub, EBook):
        print(f"     • Digital format: {pub.file_format}")

# Process all publications
for pub in publications[:4]:  # Process first 4 as example
    process_publication(pub)
    print("   " + "-" * 50)

print("\n" + "=" * 80)
print("\n7. Library inventory system:")

class Library:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def add_publication(self, publication):
        """Add any publication to library"""
        self.inventory.append(publication)
        return f'Added "{publication.title}" to {self.name}'
    
    def get_total_value(self):
        """Calculate total value of inventory"""
        return sum(pub.price for pub in self.inventory)
    
    def list_by_type(self, pub_type):
        """List publications of a specific type"""
        matching = [pub for pub in self.inventory if isinstance(pub, pub_type)]
        if not matching:
            return f"No {pub_type.__name__}s in inventory"
        
        result = f"{pub_type.__name__}s in {self.name}:\n"
        for i, pub in enumerate(matching, 1):
            result += f"  {i}. {pub.get_info()}\n"
        return result
    
    def find_by_author(self, author_name):
        """Find books by a specific author"""
        books_by_author = []
        for pub in self.inventory:
            if isinstance(pub, Book) and author_name.lower() in pub.author.lower():
                books_by_author.append(pub)
        return books_by_author

print("\n   Creating a library:")
city_library = Library("City Central Library")

print("\n   Adding publications to library:")
for pub in publications:
    print(f"   {city_library.add_publication(pub)}")

print(f"\n   Total library value: ${city_library.get_total_value():.2f}")

print(f"\n   {city_library.list_by_type(Book)}")
print(f"   {city_library.list_by_type(Magazine)}")
print(f"   {city_library.list_by_type(Newspaper)}")

print("\n   Finding books by author 'Dan Brown':")
brown_books = city_library.find_by_author("Dan Brown")
for book in brown_books:
    print(f"   • {book.title}")

print("\n" + "=" * 80)
print("\n8. Enhanced functionality with inheritance:")

print("\n   Adding audiobook class:")

class AudioBook(Book):
    def __init__(self, title, author, pages, price, duration, narrator):
        super().__init__(title, author, pages, price)
        self.duration = duration  # in hours
        self.narrator = narrator
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Duration: {self.duration}h, Narrator: {self.narrator}"
    
    def calculate_listening_time(self, speed=1.0):
        """Calculate listening time at given speed"""
        return self.duration / speed

print("\n   Creating audiobooks:")
audiobooks = [
    AudioBook("The Hobbit", "J.R.R. Tolkien", 310, 24.99, 11.5, "Rob Inglis"),
    AudioBook("Becoming", "Michelle Obama", 448, 29.99, 19.0, "Michelle Obama"),
    AudioBook("The Martian", "Andy Weir", 369, 19.99, 10.8, "R.C. Bray")
]

print("\n   Audiobook details:")
for audiobook in audiobooks:
    print(f"   {audiobook}")
    print(f"     • Listening time (normal): {audiobook.calculate_listening_time():.1f}h")
    print(f"     • Listening time (1.5x): {audiobook.calculate_listening_time(1.5):.1f}h")

print("\n" + "=" * 80)
print("\n9. Publication statistics:")

print("\n   Analyzing all publications:")
all_pubs = publications + audiobooks

# Count by type
type_counts = {}
total_pages = 0
total_price = 0

for pub in all_pubs:
    pub_type = type(pub).__name__
    type_counts[pub_type] = type_counts.get(pub_type, 0) + 1
    
    total_price += pub.price
    if hasattr(pub, 'pages'):
        total_pages += pub.pages

print(f"   Total publications: {len(all_pubs)}")
print(f"   By type:")
for pub_type, count in type_counts.items():
    print(f"     • {pub_type}: {count}")
print(f"   Total value: ${total_price:.2f}")
print(f"   Total pages (books only): {total_pages}")

print("\n" + "=" * 80)
print("\n10. Testing the original example code:")

print("\n   Original example recreation:")
orig_b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
orig_n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
orig_m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(f"\n   print(b1.author): {orig_b1.author}")
print(f"   print(n1.publisher): {orig_n1.publisher}")
print(f"   print(b1.price, m1.price, n1.price): {orig_b1.price}, {orig_m1.price}, {orig_n1.price}")

print("\n   Additional info from enhanced classes:")
print(f"   b1.get_info(): {orig_b1.get_info()}")
print(f"   n1.get_info(): {orig_n1.get_info()}")
print(f"   m1.get_info(): {orig_m1.get_info()}")

print("\n" + "=" * 80)
print("\nSummary of Inheritance:")
print("✓ Publication is the base class with title and price")
print("✓ Periodical inherits from Publication, adds publisher and period")
print("✓ Book inherits from Publication, adds author and pages")
print("✓ Magazine and Newspaper inherit from Periodical")
print("✓ EBook inherits from Book, adds file format and size")
print("✓ super().__init__() calls parent class constructor")
print("✓ Methods can be overridden in subclasses")
print("✓ isinstance() checks object type in inheritance hierarchy")
print("✓ Polymorphism allows treating different types uniformly")
print("✓ Inheritance enables code reuse and specialization")