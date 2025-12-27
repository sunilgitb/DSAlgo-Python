# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # __repr__ provides an unambiguous string representation, often used for debugging
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"

    # Called when an attribute is retrieved. Be aware that you can't
    # directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    # __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The 'price' attribute must be a float")
        return super().__setattr__(name, value)

    # __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    def __getattr__(self, name):
        return f"{name} is not here!"

# Driver code
if __name__ == "__main__":
    print("=== Creating Books ===")
    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
    
    print("\n=== Testing __str__ and __repr__ ===")
    print("Using str():")
    print(str(b1))
    print(str(b2))
    
    print("\nUsing repr():")
    print(repr(b1))
    print(repr(b2))
    
    print("\nDirect printing (uses __str__):")
    print(b1)
    print(b2)
    
    print("\n=== Testing __getattribute__ (discount calculation) ===")
    print(f"b1.price (with 10% discount): {b1.price}")
    print(f"b2.price (with 10% discount): {b2.price}")
    
    print("\n=== Testing __setattr__ (type validation) ===")
    try:
        b1.price = 38.95  # This should work
        print(f"Successfully set b1.price to 38.95")
        print(f"b1.price after discount: {b1.price}")
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        b1.price = 40  # This should fail (int instead of float)
    except ValueError as e:
        print(f"Error when setting int: {e}")
    
    try:
        b2.price = float(40)  # This works - explicit conversion
        print(f"Successfully set b2.price to float(40)")
        print(f"b2.price after discount: {b2.price}")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== Testing __getattr__ (non-existent attributes) ===")
    print(f"b1.randomprop: {b1.randomprop}")
    print(f"b1.isbn: {b1.isbn}")
    print(f"b2.publisher: {b2.publisher}")
    
    print("\n=== Testing existing vs non-existent attributes ===")
    print(f"b1.title (exists): {b1.title}")
    print(f"b1.author (exists): {b1.author}")
    print(f"b1._discount (exists): {b1._discount}")
    
    print("\n=== Changing discount and observing effect ===")
    print(f"Current b1.price: {b1.price}")
    b1._discount = 0.2  # Change discount to 20%
    print(f"b1.price after 20% discount: {b1.price}")
    
    print("\n=== Object inspection ===")
    print(f"b1.__dict__: {b1.__dict__}")
    print(f"Attributes that exist on b1: {dir(b1)[:10]}...")  # First 10
    
    print("\n=== Creating a book with bad data ===")
    try:
        b3 = Book("Bad Book", "Bad Author", 25)  # int instead of float
    except ValueError as e:
        print(f"Error creating book: {e}")