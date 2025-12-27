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
        return f"{self.title} by {self.author}, costs ${self.price:.2f}"

    # __repr__ for developer-friendly representation
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name):
        # Apply discount when accessing the price attribute
        if name == "price":
            # Get the actual price using super() to avoid recursion
            actual_price = super().__getattribute__("price")
            # Get the discount using super() to avoid recursion
            discount = super().__getattribute__("_discount")
            # Return discounted price
            return actual_price * (1 - discount)
        # For all other attributes, use normal lookup
        return super().__getattribute__(name)

    # TODO: __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name, value):
        # Validate price to ensure it's a positive number
        if name == "price":
            if not isinstance(value, (int, float)):
                raise ValueError(f"Price must be a number, got {type(value).__name__}")
            if value < 0:
                raise ValueError(f"Price cannot be negative, got {value}")
            # Convert to float for consistency
            value = float(value)
        # Use super() to actually set the attribute
        super().__setattr__(name, value)

    # TODO: __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    def __getattr__(self, name):
        # This is called when attribute is not found
        # Provide helpful messages for common attributes that might be expected
        if name in ["isbn", "ISBN"]:
            return "ISBN not available for this book"
        elif name in ["genre", "category"]:
            return "Genre information not available"
        elif name == "year":
            return "Publication year not specified"
        else:
            # Generic message for other attributes
            return f"'{name}' attribute not found"

# Driver code to test all the implemented methods
if __name__ == "__main__":
    print("=== Creating Book Instances ===")
    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
    
    print("\n=== Testing __str__ ===")
    print("Book 1:", b1)
    print("Book 2:", b2)
    
    print("\n=== Testing __repr__ ===")
    print("Book 1 repr:", repr(b1))
    print("Book 2 repr:", repr(b2))
    
    print("\n=== Testing __getattribute__ (Automatic Discount) ===")
    print(f"Original price of '{b1.title}': $39.95")
    print(f"Price with 10% discount: ${b1.price:.2f}")
    print(f"Original price of '{b2.title}': $29.95")
    print(f"Price with 10% discount: ${b2.price:.2f}")
    
    print("\n=== Testing Discount Modification ===")
    b1._discount = 0.25  # 25% discount
    print(f"'{b1.title}' with 25% discount: ${b1.price:.2f}")
    
    print("\n=== Testing __setattr__ (Validation) ===")
    print("Testing valid price setting...")
    try:
        b1.price = 49.99
        print(f"Successfully set price to: ${b1.price:.2f} (after discount)")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nTesting invalid price setting...")
    try:
        b2.price = -10  # Should fail - negative price
    except ValueError as e:
        print(f"Expected error: {e}")
    
    try:
        b2.price = "free"  # Should fail - string price
    except ValueError as e:
        print(f"Expected error: {e}")
    
    print("\n=== Testing __getattr__ (Non-existent Attributes) ===")
    print("Accessing non-existent attributes:")
    print(f"b1.isbn: {b1.isbn}")
    print(f"b1.genre: {b1.genre}")
    print(f"b1.publication_year: {b1.publication_year}")
    print(f"b2.ISBN: {b2.ISBN}")
    print(f"b2.category: {b2.category}")
    print(f"b2.random_attribute: {b2.random_attribute}")
    
    print("\n=== Testing Existing vs Non-existent Attributes ===")
    print("Accessing existing attributes:")
    print(f"b1.title: {b1.title}")
    print(f"b1.author: {b1.author}")
    print(f"b1._discount: {b1._discount}")
    
    print("\n=== Demonstration of Recursion Prevention ===")
    print("Note: Using super().__getattribute__ and super().__setattr__")
    print("prevents infinite recursion when accessing/setting attributes")
    
    print("\n=== All Book Details ===")
    print(f"b1 details: Title='{b1.title}', Author='{b1.author}', ")
    print(f"  Base Price=${super(Book, b1).__getattribute__('price'):.2f}, ")
    print(f"  Discount={b1._discount*100}%, Final Price=${b1.price:.2f}")
    
    print(f"\nb2 details: Title='{b2.title}', Author='{b2.author}', ")
    print(f"  Base Price=${super(Book, b2).__getattribute__('price'):.2f}, ")
    print(f"  Discount={b2._discount*100}%, Final Price=${b2.price:.2f}")
    
    print("\n=== Testing with eval() ===")
    # repr() should create a string that can recreate the object
    b1_repr = repr(b1)
    print(f"b1 repr string: {b1_repr}")
    # Note: In practice, be careful with eval() for security reasons