# Python Object Oriented Programming
# Using composition to build complex objects

class Book:
    def __init__(self, title, price, authorfname, authorlname):
        self.title = title
        self.price = price

        self.authorfname = authorfname
        self.authorlname = authorlname

        self.chapters = []

    def addchapter(self, name, pages):
        self.chapters.append((name, pages))
    
    def get_total_pages(self):
        """Calculate total pages from all chapters"""
        total = 0
        for chapter_name, pages in self.chapters:
            total += pages
        return total
    
    def get_average_chapter_length(self):
        """Calculate average pages per chapter"""
        if not self.chapters:
            return 0
        return self.get_total_pages() / len(self.chapters)
    
    def get_book_info(self):
        """Return formatted book information"""
        author_name = f"{self.authorfname} {self.authorlname}"
        chapters_info = f", {len(self.chapters)} chapters, {self.get_total_pages()} pages"
        return f'"{self.title}" by {author_name} - ${self.price}{chapters_info}'
    
    def __str__(self):
        return self.get_book_info()


print("Testing Book Class with Simple Composition:")
print("=" * 80)

# Create a book instance
b1 = Book("War and Peace", 39.0, "Leo", "Tolstoy")

print("1. Created book instance:")
print(f"   b1 = Book('War and Peace', 39.0, 'Leo', 'Tolstoy')")
print(f"   Book info: {b1}")

print("\n" + "=" * 80)
print("\n2. Adding chapters to the book:")

print("\n   Adding chapters:")
print(f"   b1.addchapter('Chapter 1', 125)")
b1.addchapter("Chapter 1", 125)

print(f"   b1.addchapter('Chapter 2', 97)")
b1.addchapter("Chapter 2", 97)

print(f"   b1.addchapter('Chapter 3', 143)")
b1.addchapter("Chapter 3", 143)

print(f"   b1.addchapter('Chapter 4', 88)")
b1.addchapter("Chapter 4", 88)

print(f"   b1.addchapter('Chapter 5', 112)")
b1.addchapter("Chapter 5", 112)

print("\n   Current book info:")
print(f"   {b1}")

print("\n" + "=" * 80)
print("\n3. Accessing book attributes and methods:")

print(f"\n   Book attributes:")
print(f"   b1.title: {b1.title}")
print(f"   b1.price: ${b1.price}")
print(f"   b1.authorfname: {b1.authorfname}")
print(f"   b1.authorlname: {b1.authorlname}")
print(f"   b1.chapters: {b1.chapters}")

print(f"\n   Book methods:")
print(f"   b1.get_total_pages(): {b1.get_total_pages()} pages")
print(f"   b1.get_average_chapter_length(): {b1.get_average_chapter_length():.1f} pages per chapter")
print(f"   b1.get_book_info(): {b1.get_book_info()}")

print("\n" + "=" * 80)
print("\n4. Working with chapters:")

print(f"\n   All chapters:")
for i, (chapter_name, pages) in enumerate(b1.chapters, 1):
    print(f"   Chapter {i}: '{chapter_name}' - {pages} pages")

print(f"\n   Finding longest chapter:")
if b1.chapters:
    longest_chapter = max(b1.chapters, key=lambda x: x[1])
    print(f"   Longest: '{longest_chapter[0]}' - {longest_chapter[1]} pages")

print(f"\n   Finding shortest chapter:")
if b1.chapters:
    shortest_chapter = min(b1.chapters, key=lambda x: x[1])
    print(f"   Shortest: '{shortest_chapter[0]}' - {shortest_chapter[1]} pages")

print("\n" + "=" * 80)
print("\n5. Creating more books:")

# Create more books
books = [
    Book("1984", 24.99, "George", "Orwell"),
    Book("To Kill a Mockingbird", 29.95, "Harper", "Lee"),
    Book("The Great Gatsby", 19.99, "F. Scott", "Fitzgerald"),
    Book("Moby Dick", 34.50, "Herman", "Melville")
]

print("\n   Adding chapters to each book:")
# Add chapters to 1984
books[0].addchapter("Part 1: War is Peace", 45)
books[0].addchapter("Part 2: Ignorance is Strength", 52)
books[0].addchapter("Part 3: Freedom is Slavery", 38)

# Add chapters to To Kill a Mockingbird
books[1].addchapter("Part One", 68)
books[1].addchapter("Part Two", 92)

# Add chapters to The Great Gatsby
books[2].addchapter("Chapter 1", 32)
books[2].addchapter("Chapter 2", 28)
books[2].addchapter("Chapter 3", 35)
books[2].addchapter("Chapter 4", 31)
books[2].addchapter("Chapter 5", 29)
books[2].addchapter("Chapter 6", 27)
books[2].addchapter("Chapter 7", 42)
books[2].addchapter("Chapter 8", 26)
books[2].addchapter("Chapter 9", 30)

# Add chapters to Moby Dick
books[3].addchapter("Loomings", 15)
books[3].addchapter("The Carpet-Bag", 12)
books[3].addchapter("The Spouter-Inn", 28)

print("\n   All books in collection:")
for i, book in enumerate(books, 1):
    print(f"   {i}. {book}")

print("\n" + "=" * 80)
print("\n6. Book analysis:")

print("\n   Statistics for all books:")
total_pages_all = 0
total_price_all = 0
book_with_most_chapters = None
book_with_fewest_chapters = None

for book in books:
    total_pages_all += book.get_total_pages()
    total_price_all += book.price
    
    if book_with_most_chapters is None or len(book.chapters) > len(book_with_most_chapters.chapters):
        book_with_most_chapters = book
    
    if book_with_fewest_chapters is None or len(book.chapters) < len(book_with_fewest_chapters.chapters):
        book_with_fewest_chapters = book

print(f"   Total pages across all books: {total_pages_all}")
print(f"   Total value of books: ${total_price_all:.2f}")
print(f"   Book with most chapters: '{book_with_most_chapters.title}' ({len(book_with_most_chapters.chapters)} chapters)")
print(f"   Book with fewest chapters: '{book_with_fewest_chapters.title}' ({len(book_with_fewest_chapters.chapters)} chapters)")

print("\n   Detailed chapter analysis:")
for book in books:
    if book.chapters:
        avg_length = book.get_average_chapter_length()
        print(f"\n   '{book.title}':")
        print(f"     • {len(book.chapters)} chapters")
        print(f"     • {book.get_total_pages()} total pages")
        print(f"     • {avg_length:.1f} pages per chapter (average)")

print("\n" + "=" * 80)
print("\n7. Improving the design with separate classes:")

print("\n   Current design issues:")
print("   • Author name split into first/last (hard to process)")
print("   • Chapters stored as tuples (limited functionality)")
print("   • No way to add additional chapter metadata")

print("\n   Improved design with separate classes:")

class Author:
    def __init__(self, first_name, last_name, nationality=""):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        result = self.full_name()
        if self.nationality:
            result += f" ({self.nationality})"
        return result

class Chapter:
    def __init__(self, title, page_count, summary=""):
        self.title = title
        self.page_count = page_count
        self.summary = summary
    
    def __str__(self):
        result = f"'{self.title}' - {self.page_count} pages"
        if self.summary:
            result += f": {self.summary}"
        return result

class ImprovedBook:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author  # Now an Author object
        self.chapters = []  # Now a list of Chapter objects
    
    def add_chapter(self, chapter):
        self.chapters.append(chapter)
        return f"Added chapter: {chapter.title}"
    
    def get_total_pages(self):
        return sum(chapter.page_count for chapter in self.chapters)
    
    def __str__(self):
        author_name = str(self.author)
        chapters_info = f", {len(self.chapters)} chapters, {self.get_total_pages()} pages"
        return f'"{self.title}" by {author_name} - ${self.price}{chapters_info}'

print("\n   Creating improved book:")
tolstoy = Author("Leo", "Tolstoy", "Russian")
improved_b1 = ImprovedBook("War and Peace", 39.0, tolstoy)

print(f"\n   Adding improved chapters:")
improved_b1.add_chapter(Chapter("Chapter 1", 125, "Introduction to the characters"))
improved_b1.add_chapter(Chapter("Chapter 2", 97, "The ball scene"))
improved_b1.add_chapter(Chapter("Chapter 3", 143, "Battle of Austerlitz"))

print(f"   {improved_b1}")

print(f"\n   Chapter details:")
for i, chapter in enumerate(improved_b1.chapters, 1):
    print(f"   {i}. {chapter}")

print("\n" + "=" * 80)
print("\n8. Testing the original example code:")

print("\n   Original example recreation:")
orig_b1 = Book("War and Peace", 39.0, "Leo", "Tolstoy")

orig_b1.addchapter("Chapter 1", 125)
orig_b1.addchapter("Chapter 2", 97)
orig_b1.addchapter("Chapter 3", 143)

print(f"\n   print(b1.title): {orig_b1.title}")

print("\n   What the original example doesn't show:")
print(f"   b1.price: ${orig_b1.price}")
print(f"   b1.authorfname: {orig_b1.authorfname}")
print(f"   b1.authorlname: {orig_b1.authorlname}")
print(f"   b1.chapters: {orig_b1.chapters}")
print(f"   Total pages: {orig_b1.get_total_pages()}")

print("\n" + "=" * 80)
print("\n9. Practical example - Book collection:")

class BookCollection:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        return f'Added "{book.title}" to {self.name}'
    
    def get_total_value(self):
        return sum(book.price for book in self.books)
    
    def get_total_pages(self):
        return sum(book.get_total_pages() for book in self.books)
    
    def find_books_by_author(self, author_last_name):
        matching_books = []
        for book in self.books:
            if book.authorlname.lower() == author_last_name.lower():
                matching_books.append(book)
        return matching_books
    
    def display_collection(self):
        print(f"\n   {self.name} Collection:")
        print("   " + "-" * 50)
        for i, book in enumerate(self.books, 1):
            print(f"   {i}. {book.get_book_info()}")
        print(f"\n   Total value: ${self.get_total_value():.2f}")
        print(f"   Total pages: {self.get_total_pages()}")

print("\n   Creating a book collection:")
my_collection = BookCollection("My Personal Library")

print("\n   Adding books to collection:")
all_books = [b1] + books  # Include original b1 and the other books
for book in all_books:
    print(f"   {my_collection.add_book(book)}")

my_collection.display_collection()

print("\n   Finding books by author 'Orwell':")
orwell_books = my_collection.find_books_by_author("Orwell")
for book in orwell_books:
    print(f"   • {book.title}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Composition combines objects to build complex systems")
print("✓ Book contains author name as separate attributes")
print("✓ Book contains chapters as list of tuples")
print("✓ Methods operate on composed data")
print("✓ Simple but effective for basic needs")
print("✓ Could be improved with dedicated Author and Chapter classes")
print("✓ Composition is often more flexible than inheritance")
print("✓ Objects can be composed in different ways at runtime")