from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): 
        pass

    @abstractmethod
    def perimeter(self): 
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side
    
    def area(self):
        return self.__side * self.__side
    
    def perimeter(self):
        return 4 * self.__side


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    def area(self):
        return 3.14159 * self.__radius * self.__radius
    
    def perimeter(self):
        return 2 * 3.14159 * self.__radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return 2 * (self.__length + self.__width)


# Test the classes
print("Testing Abstract Classes and Inheritance:")
print("=" * 60)

# Test Square
print("\n1. Square with side 5:")
square = Square(5)
print(f"   Area: {square.area()}")
print(f"   Perimeter: {square.perimeter()}")

# Test Circle
print("\n2. Circle with radius 7:")
circle = Circle(7)
print(f"   Area: {circle.area():.2f}")
print(f"   Perimeter (Circumference): {circle.perimeter():.2f}")

# Test Rectangle
print("\n3. Rectangle with length 6 and width 4:")
rectangle = Rectangle(6, 4)
print(f"   Area: {rectangle.area()}")
print(f"   Perimeter: {rectangle.perimeter()}")

print("\n" + "=" * 60)
print("\nDemonstrating Polymorphism:")

shapes = [Square(3), Circle(5), Rectangle(4, 7)]

print("\nList of shapes:")
for i, shape in enumerate(shapes, 1):
    print(f"\nShape {i}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")

print("\n" + "=" * 60)
print("\nTesting Abstract Class Enforcement:")

try:
    print("\nTrying to instantiate Shape directly (should fail):")
    shape = Shape()
except TypeError as e:
    print(f"  ✓ Correctly raised error: {e}")

class IncompleteTriangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    # Missing area() and perimeter() methods

try:
    print("\nTrying to instantiate IncompleteTriangle (missing methods):")
    triangle = IncompleteTriangle(3, 4, 5)
except TypeError as e:
    print(f"  ✓ Correctly raised error: {e}")

class CompleteTriangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c

print("\nCompleteTriangle with sides 3, 4, 5:")
triangle = CompleteTriangle(3, 4, 5)
print(f"  Area: {triangle.area():.2f}")
print(f"  Perimeter: {triangle.perimeter():.2f}")

print("\n" + "=" * 60)
print("\nSummary:")
print("✓ Abstract classes force implementation of methods")
print("✓ Polymorphism allows different shapes to be treated uniformly")
print("✓ Encapsulation protects internal state (private variables)")