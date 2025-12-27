# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs ${self.price:.2f}"

    # TODO: the __call__ method can be used to call the object like a function
    def __call__(self, new_title=None, new_author=None, new_price=None):
        """
        Allows the book object to be called like a function.
        Updates the book's attributes with new values.
        
        Args:
            new_title (str, optional): New title for the book
            new_author (str, optional): New author for the book
            new_price (float, optional): New price for the book
        """
        print(f"📚 Updating book: {self.title}")
        
        if new_title is not None:
            print(f"   Changing title from '{self.title}' to '{new_title}'")
            self.title = new_title
            
        if new_author is not None:
            print(f"   Changing author from '{self.author}' to '{new_author}'")
            self.author = new_author
            
        if new_price is not None:
            print(f"   Changing price from ${self.price:.2f} to ${new_price:.2f}")
            self.price = new_price
            
        print(f"✅ Book updated successfully!\n")

# Driver code
if __name__ == "__main__":
    print("=== Creating Book Objects ===")
    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
    
    print("Initial state:")
    print(f"b1: {b1}")
    print(f"b2: {b2}")
    
    print("\n" + "="*50 + "\n")
    
    # TODO: call the object as if it were a function
    print("=== Testing __call__ Method ===")
    print("Calling b1() to update all attributes:")
    b1("Anna Karenina", "Leo Tolstoy", 49.95)
    print(f"After update: {b1}")
    
    print("\n" + "="*50 + "\n")
    
    print("Calling b2() with partial updates:")
    print(f"Before update: {b2}")
    
    # Update only the price
    print("\nUpdating only the price:")
    b2(new_price=34.95)
    print(f"After price update: {b2}")
    
    # Update only the author
    print("\nUpdating only the author:")
    b2(new_author="J.D. Salinger")
    print(f"After author update: {b2}")
    
    print("\n" + "="*50 + "\n")
    
    print("=== Additional Examples ===")
    
    # Create a new book
    b3 = Book("1984", "George Orwell", 19.95)
    print(f"New book created: {b3}")
    
    # Update with no arguments (nothing changes)
    print("\nCalling with no arguments:")
    b3()
    print(f"Book unchanged: {b3}")
    
    print("\n" + "="*50 + "\n")
    
    print("=== Checking Callability ===")
    # Check if objects are callable
    print(f"Is b1 callable? {callable(b1)}")
    print(f"Is b2 callable? {callable(b2)}")
    print(f"Is 'hello' callable? {callable('hello')}")
    print(f"Is print function callable? {callable(print)}")
    
    print("\n" + "="*50 + "\n")
    
    print("=== Practical Use Case ===")
    print("Imagine a book management system where books need to be updated frequently.")
    
    class LibraryBook(Book):
        def __init__(self, title, author, price, isbn, location):
            super().__init__(title, author, price)
            self.isbn = isbn
            self.location = location
            self.last_updated = "Never"
        
        def __call__(self, **kwargs):
            """Update any attribute using keyword arguments."""
            import datetime
            updates = []
            
            for key, value in kwargs.items():
                if hasattr(self, key):
                    old_value = getattr(self, key)
                    setattr(self, key, value)
                    updates.append(f"{key}: {old_value} → {value}")
                else:
                    print(f"⚠️  Warning: '{key}' is not a valid attribute")
            
            if updates:
                self.last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"\n📝 Updating Library Book: {self.title}")
                for update in updates:
                    print(f"   {update}")
                print(f"   Last updated: {self.last_updated}")
            else:
                print("No updates made.")
            
            return self
        
        def __str__(self):
            return (f"{self.title} by {self.author}, "
                    f"${self.price:.2f}, ISBN: {self.isbn}, "
                    f"Location: {self.location}, Last Updated: {self.last_updated}")
    
    print("\nCreating a library book:")
    lb = LibraryBook("To Kill a Mockingbird", "Harper Lee", 14.99, 
                     "978-0446310789", "Fiction Section, Shelf A3")
    print(lb)
    
    print("\nUpdating library book using __call__:")
    lb(price=12.99, location="Fiction Section, Shelf B2", author="Harper E. Lee")
    print(f"\nAfter update:\n{lb}")
    
    print("\n" + "="*50 + "\n")
    
    print("=== Summary ===")
    print("The __call__ method:")
    print("1. Makes objects callable using parentheses: obj()")
    print("2. Can accept any arguments you define")
    print("3. Useful for objects that need to be 'executed' or 'updated'")
    print("4. Allows objects to maintain state between calls")
    print("5. Common in decorator classes and stateful functions")