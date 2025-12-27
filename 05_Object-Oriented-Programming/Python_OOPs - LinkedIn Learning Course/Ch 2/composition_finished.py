# Python Object Oriented Programming
# Using composition to build complex objects

class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        # Use references to other objects, like author and chapters
        self.author = author
        self.chapters = []
        self.reviews = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)
        return f"Added chapter: {chapter.name}"

    def addreview(self, rating, comment):
        self.reviews.append({"rating": rating, "comment": comment})
        return f"Added {rating}-star review"

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

    def getaveragechapterlength(self):
        if not self.chapters:
            return 0
        return self.getbookpagecount() / len(self.chapters)

    def getbookinfo(self):
        info = f'"{self.title}"'
        if self.author:
            info += f" by {self.author}"
        info += f" - ${self.price}"
        if self.chapters:
            info += f", {len(self.chapters)} chapters, {self.getbookpagecount()} pages"
        return info

    def __str__(self):
        return self.getbookinfo()


class Author:
    def __init__(self, fname, lname, nationality=""):
        self.fname = fname
        self.lname = lname
        self.nationality = nationality
        self.books = []  # List of books by this author

    def addbook(self, book):
        self.books.append(book)
        return f'Added "{book.title}" to {self.fname} {self.lname}\'s bibliography'

    def getbibliography(self):
        if not self.books:
            return f"{self.fname} {self.lname} has no books listed"
        
        result = f"Bibliography of {self.fname} {self.lname}:\n"
        for i, book in enumerate(self.books, 1):
            result += f"  {i}. {book.title} (${book.price})\n"
        return result

    def __str__(self):
        result = f"{self.fname} {self.lname}"
        if self.nationality:
            result += f" ({self.nationality})"
        return result


class Chapter:
    def __init__(self, name, pagecount, summary=""):
        self.name = name
        self.pagecount = pagecount
        self.summary = summary

    def __str__(self):
        result = f"{self.name} ({self.pagecount} pages)"
        if self.summary:
            result += f" - {self.summary}"
        return result


class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.published_books = []

    def publishbook(self, book):
        self.published_books.append(book)
        return f'{self.name} published "{book.title}"'

    def __str__(self):
        return f"{self.name} - {self.location}"


print("Testing Composition in Python:")
print("=" * 80)

print("\n1. Creating authors:")
auth1 = Author("Leo", "Tolstoy", "Russian")
auth2 = Author("George", "Orwell", "British")
auth3 = Author("Harper", "Lee", "American")

print(f"   Author 1: {auth1}")
print(f"   Author 2: {auth2}")
print(f"   Author 3: {auth3}")

print("\n" + "=" * 80)
print("\n2. Creating books with authors:")

b1 = Book("War and Peace", 39.95, auth1)
b2 = Book("1984", 24.99, auth2)
b3 = Book("To Kill a Mockingbird", 29.95, auth3)
b4 = Book("Animal Farm", 19.99, auth2)  # Same author different book

print(f"   Book 1: {b1}")
print(f"   Book 2: {b2}")
print(f"   Book 3: {b3}")
print(f"   Book 4: {b4}")

# Add books to authors' bibliographies
auth1.addbook(b1)
auth2.addbook(b2)
auth2.addbook(b4)
auth3.addbook(b3)

print("\n" + "=" * 80)
print("\n3. Adding chapters to books:")

print(f"\n   Adding chapters to '{b1.title}':")
print(f"   {b1.addchapter(Chapter('Part 1: 1805', 104))}")
print(f"   {b1.addchapter(Chapter('Part 2: 1806', 89))}")
print(f"   {b1.addchapter(Chapter('Part 3: 1807', 124))}")
print(f"   {b1.addchapter(Chapter('Part 4: 1812', 156))}")

print(f"\n   Adding chapters to '{b2.title}':")
print(f"   {b2.addchapter(Chapter('Chapter 1: Big Brother', 45))}")
print(f"   {b2.addchapter(Chapter('Chapter 2: Thoughtcrime', 52))}")
print(f"   {b2.addchapter(Chapter('Chapter 3: Newspeak', 38))}")

print(f"\n   Adding chapters to '{b3.title}':")
print(f"   {b3.addchapter(Chapter('Part One', 68))}")
print(f"   {b3.addchapter(Chapter('Part Two', 92))}")

print("\n" + "=" * 80)
print("\n4. Book information and calculations:")

books = [b1, b2, b3, b4]
for book in books:
    print(f"\n   {book.getbookinfo()}")
    if book.chapters:
        print(f"   Total pages: {book.getbookpagecount()}")
        print(f"   Average chapter length: {book.getaveragechapterlength():.1f} pages")
        print(f"   Chapters:")
        for i, chapter in enumerate(book.chapters, 1):
            print(f"     {i}. {chapter}")
    else:
        print(f"   No chapters added yet")

print("\n" + "=" * 80)
print("\n5. Author bibliographies:")

authors = [auth1, auth2, auth3]
for author in authors:
    print(f"\n   {author.getbibliography()}")

print("\n" + "=" * 80)
print("\n6. Adding publishers:")

pub1 = Publisher("Penguin Classics", "London")
pub2 = Publisher("HarperCollins", "New York")
pub3 = Publisher("Modern Library", "New York")

print(f"\n   Publishers:")
print(f"   {pub1}")
print(f"   {pub2}")
print(f"   {pub3}")

print(f"\n   Publishing books:")
print(f"   {pub1.publishbook(b1)}")
print(f"   {pub1.publishbook(b2)}")
print(f"   {pub2.publishbook(b3)}")
print(f"   {pub3.publishbook(b4)}")

print("\n   Books by publisher:")
print(f"   {pub1.name} published:")
for book in pub1.published_books:
    print(f"     - {book.title}")

print(f"\n   {pub2.name} published:")
for book in pub2.published_books:
    print(f"     - {book.title}")

print("\n" + "=" * 80)
print("\n7. Adding reviews to books:")

print(f"\n   Adding reviews to '{b1.title}':")
print(f"   {b1.addreview(5, 'Masterpiece of literature')}")
print(f"   {b1.addreview(4, 'Very long but worth it')}")
print(f"   {b1.addreview(5, 'The best novel ever written')}")

print(f"\n   Adding reviews to '{b2.title}':")
print(f"   {b2.addreview(5, 'Prophetic and chilling')}")
print(f"   {b2.addreview(4, 'Still relevant today')}")

print(f"\n   Book reviews:")
for book in [b1, b2]:
    if book.reviews:
        print(f"\n   {book.title}:")
        avg_rating = sum(r['rating'] for r in book.reviews) / len(book.reviews)
        print(f"   Average rating: {avg_rating:.1f} stars from {len(book.reviews)} reviews")
        for review in book.reviews:
            print(f"     {review['rating']} stars: {review['comment']}")

print("\n" + "=" * 80)
print("\n8. Complex composition - Bookstore:")

class Bookstore:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.authors = []
        self.publishers = []
    
    def addbook(self, book):
        self.inventory.append(book)
        
        # Add author if not already in list
        if book.author and book.author not in self.authors:
            self.authors.append(book.author)
        
        return f'Added "{book.title}" to {self.name} inventory'
    
    def addpublisher(self, publisher):
        self.publishers.append(publisher)
        return f'Added {publisher.name} to bookstore'
    
    def getinventoryvalue(self):
        total = sum(book.price for book in self.inventory)
        return total
    
    def getbooksbyauthor(self, author_name):
        result = []
        for book in self.inventory:
            if book.author and author_name.lower() in str(book.author).lower():
                result.append(book)
        return result
    
    def displayinventory(self):
        print(f"\n   {self.name} Inventory (${self.getinventoryvalue():.2f} total value):")
        print("   " + "-" * 60)
        
        # Group by author
        books_by_author = {}
        for book in self.inventory:
            author_name = str(book.author) if book.author else "Unknown Author"
            if author_name not in books_by_author:
                books_by_author[author_name] = []
            books_by_author[author_name].append(book)
        
        for author, books in books_by_author.items():
            print(f"\n   {author}:")
            for book in books:
                chapter_info = f", {len(book.chapters)} chapters" if book.chapters else ""
                print(f"     • {book.title} - ${book.price}{chapter_info}")

print("\n   Creating a bookstore:")
chapter_and_verse = Bookstore("Chapter & Verse")

print("\n   Adding books to bookstore:")
for book in [b1, b2, b3, b4]:
    print(f"   {chapter_and_verse.addbook(book)}")

print("\n   Adding publishers:")
for pub in [pub1, pub2, pub3]:
    print(f"   {chapter_and_verse.addpublisher(pub)}")

chapter_and_verse.displayinventory()

print("\n   Books by George Orwell:")
orwell_books = chapter_and_verse.getbooksbyauthor("Orwell")
for book in orwell_books:
    print(f"     • {book.title}")

print("\n" + "=" * 80)
print("\n9. Testing original example code:")

print("\n   Original example recreation:")
orig_auth = Author("Leo", "Tolstoy")
orig_b1 = Book("War and Peace", 39.95, orig_auth)

orig_b1.addchapter(Chapter("Chapter 1", 104))
orig_b1.addchapter(Chapter("Chapter 2", 89))
orig_b1.addchapter(Chapter("Chapter 3", 124))

print(f"\n   print(b1.title): {orig_b1.title}")
print(f"   print(b1.author): {orig_b1.author}")
print(f"   print(b1.getbookpagecount()): {orig_b1.getbookpagecount()}")

print("\n" + "=" * 80)
print("\nSummary of Composition:")
print("✓ Composition builds complex objects from simpler ones")
print("✓ Book 'has-a' Author (not 'is-a' Author)")
print("✓ Book 'has-many' Chapters")
print("✓ Objects maintain references to other objects")
print("✓ More flexible than inheritance for many use cases")
print("✓ Allows runtime modification of object relationships")
print("✓ Enables building complex hierarchies without deep inheritance")
print("✓ Objects can be reused in multiple compositions")