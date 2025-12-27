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

    # __repr__ for better debugging
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"

    # TODO: the __call__ method can be used to call the object like a function
    def __call__(self, title=None, author=None, price=None):
        """Allows the book object to be called like a function to update its attributes."""
        print(f"Calling book object: {self.title}")
        
        # Only update attributes that are provided
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if price is not None:
            self.price = price
        
        # Return self to allow method chaining
        return self
    
    # Additional method to demonstrate functionality
    def apply_discount(self, discount_percent):
        """Apply a discount to the book price."""
        self.price = self.price * (1 - discount_percent/100)
        return self
    
    def get_book_info(self):
        """Return a dictionary with book information."""
        return {
            'title': self.title,
            'author': self.author,
            'price': self.price
        }

# Driver code
if __name__ == "__main__":
    print("=== Creating Book Objects ===")
    b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
    
    print("Initial state:")
    print(f"b1: {b1}")
    print(f"b2: {b2}")
    
    print("\n=== Testing __call__ Method ===")
    print("Calling b1 as a function to update all attributes:")
    b1("Anna Karenina", "Leo Tolstoy", 49.95)
    print(f"After update: {b1}")
    
    print("\nCalling b2 with partial updates:")
    print(f"Before: {b2}")
    b2(price=34.95)  # Only update price
    print(f"After updating price: {b2}")
    
    b2(author="J.D. Salinger")  # Only update author
    print(f"After updating author: {b2}")
    
    print("\n=== Method Chaining with __call__ ===")
    print("Using __call__ with method chaining:")
    b3 = Book("1984", "George Orwell", 19.95)
    print(f"Original: {b3}")
    
    # Chain __call__ with other methods
    b3("Animal Farm", price=14.95).apply_discount(10)
    print(f"After chained calls: {b3}")
    
    print("\n=== Checking if Objects are Callable ===")
    print(f"Is b1 callable? {callable(b1)}")
    print(f"Is b2 callable? {callable(b2)}")
    print(f"Is 'hello' callable? {callable('hello')}")
    print(f"Is print callable? {callable(print)}")
    
    print("\n=== Using __call__ for Different Purposes ===")
    
    # Example 1: Reusable configuration
    print("\nExample 1: Configuration updates")
    class ConfigurableBook(Book):
        def __call__(self, **kwargs):
            """Update any attribute using keyword arguments."""
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    print(f"Warning: '{key}' is not a valid attribute")
            return self
    
    cb = ConfigurableBook("Brave New World", "Aldous Huxley", 24.95)
    print(f"Original: {cb}")
    cb(title="Island", price=29.95, publisher="Harper")  # publisher doesn't exist
    print(f"After config update: {cb}")
    
    # Example 2: Function-like behavior
    print("\nExample 2: Function-like calculations")
    class Calculator:
        def __init__(self):
            self.memory = 0
        
        def __call__(self, operation, *args):
            """Make calculator callable for operations."""
            if operation == 'add':
                result = sum(args)
            elif operation == 'multiply':
                result = 1
                for num in args:
                    result *= num
            elif operation == 'memory':
                return self.memory
            elif operation == 'store':
                self.memory = args[0] if args else 0
                return self.memory
            else:
                raise ValueError(f"Unknown operation: {operation}")
            
            self.memory = result
            return result
    
    calc = Calculator()
    print(f"Add 1, 2, 3: {calc('add', 1, 2, 3)}")
    print(f"Multiply 4, 5: {calc('multiply', 4, 5)}")
    print(f"Memory value: {calc('memory')}")
    
    # Example 3: Stateful function
    print("\nExample 3: Stateful counter")
    class Counter:
        def __init__(self, start=0):
            self.count = start
        
        def __call__(self, increment=1):
            """Increment and return the count."""
            self.count += increment
            return self.count
        
        def reset(self, value=0):
            self.count = value
            return self
    
    counter = Counter()
    print(f"Initial count: {counter.count}")
    print(f"Call counter(): {counter()}")
    print(f"Call counter(5): {counter(5)}")
    print(f"Call counter(2): {counter(2)}")
    print(f"Final count: {counter.count}")
    
    print("\n=== Real-world Use Cases ===")
    print("1. Objects that need to be reconfigured dynamically")
    print("2. Stateful functions (like decorators with state)")
    print("3. Functors in functional programming patterns")
    print("4. Objects that behave like functions for APIs")
    
    print("\n=== Important Notes ===")
    print("• __call__ makes objects callable like functions")
    print("• Useful for creating functors (objects that act like functions)")
    print("• Common in decorator classes that need to maintain state")
    print("• Can return values just like regular functions")
    print("• Use callable() to check if an object is callable")