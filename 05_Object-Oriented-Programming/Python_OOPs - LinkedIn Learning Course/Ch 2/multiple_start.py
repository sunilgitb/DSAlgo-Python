# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        print("Class A initializer")

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        print("Class B initializer")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("Class C initializer")

# Driver code
if __name__ == "__main__":
    # Create an instance of class C
    c = C()
    
    # Check the Method Resolution Order (MRO)
    print("\nMethod Resolution Order (MRO):")
    for i, cls in enumerate(C.__mro__):
        print(f"{i}: {cls.__name__}")
    
    # Access attributes from parent classes
    print("\nAccessing attributes:")
    print(f"c.foo = {c.foo}")
    print(f"c.bar = {c.bar}")
    
    # Check what methods are available
    print("\nInstance attributes:")
    print(f"c.__dict__ = {c.__dict__}")
    
    # Demonstrate inheritance hierarchy
    print("\nInheritance check:")
    print(f"Is c an instance of A? {isinstance(c, A)}")
    print(f"Is c an instance of B? {isinstance(c, B)}")
    print(f"Is c an instance of C? {isinstance(c, C)}")