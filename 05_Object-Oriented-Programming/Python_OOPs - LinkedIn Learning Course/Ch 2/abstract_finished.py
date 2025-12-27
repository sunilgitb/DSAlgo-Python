# Python Object Oriented Programming
# Using Abstract Base Classes to enforce class constraints

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    # Inheriting from ABC indicates that this is an abstract base class
    def __init__(self):
        super().__init__()

    # declaring a method as abstract requires a subclass to implement it
    @abstractmethod
    def calcArea(self):
        pass
    
    @abstractmethod
    def calcPerimeter(self):
        pass
    
    def get_shape_type(self):
        """Non-abstract method - can be used by all subclasses"""
        return self.__class__.__name__


class Circle(GraphicShape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calcArea(self):
        return 3.14159 * (self.radius ** 2)
    
    def calcPerimeter(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"


class Square(GraphicShape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def calcArea(self):
        return self.side * self.side
    
    def calcPerimeter(self):
        return 4 * self.side
    
    def __str__(self):
        return f"Square(side={self.side})"


class Rectangle(GraphicShape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def calcArea(self):
        return self.length * self.width
    
    def calcPerimeter(self):
        return 2 * (self.length + self.width)
    
    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"


class Triangle(GraphicShape):
    def __init__(self, base, height, side1, side2, side3):
        super().__init__()
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calcArea(self):
        return 0.5 * self.base * self.height
    
    def calcPerimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height})"


print("Testing Abstract Base Classes:")
print("=" * 80)

# Abstract classes can't be instantiated themselves
print("1. Trying to instantiate abstract base class:")
try:
    g = GraphicShape()
    print(f"   ✗ Unexpectedly created: {g}")
except TypeError as e:
    print(f"   ✓ Correctly prevented: {e}")

print("\n" + "=" * 80)
print("\n2. Creating concrete shape instances:")

c = Circle(10)
s = Square(12)
r = Rectangle(8, 6)
t = Triangle(10, 5, 8, 9, 7)

print(f"   Created shapes:")
print(f"   {c}")
print(f"   {s}")
print(f"   {r}")
print(f"   {t}")

print("\n3. Calculating areas (original example):")
print(f"   Circle(10).calcArea(): {c.calcArea():.2f}")
print(f"   Square(12).calcArea(): {s.calcArea():.2f}")

print("\n4. Calculating perimeters (added abstract method):")
print(f"   Circle perimeter: {c.calcPerimeter():.2f}")
print(f"   Square perimeter: {s.calcPerimeter():.2f}")
print(f"   Rectangle perimeter: {r.calcPerimeter():.2f}")
print(f"   Triangle perimeter: {t.calcPerimeter():.2f}")

print("\n5. Using non-abstract method from base class:")
print(f"   Circle shape type: {c.get_shape_type()}")
print(f"   Square shape type: {s.get_shape_type()}")
print(f"   Rectangle shape type: {r.get_shape_type()}")
print(f"   Triangle shape type: {t.get_shape_type()}")

print("\n" + "=" * 80)
print("\n6. Testing incomplete subclass (should fail):")

class IncompleteShape(GraphicShape):
    """This class doesn't implement all abstract methods"""
    def __init__(self):
        super().__init__()
    
    # Missing calcArea() and calcPerimeter()

print("   Trying to instantiate incomplete subclass:")
try:
    incomplete = IncompleteShape()
    print(f"   ✗ Unexpectedly created: {incomplete}")
except TypeError as e:
    print(f"   ✓ Correctly prevented: {e}")

print("\n" + "=" * 80)
print("\n7. Shape collection with polymorphism:")

shapes = [
    Circle(7),
    Square(5),
    Rectangle(9, 4),
    Triangle(12, 8, 10, 10, 12),
    Circle(3.5),
    Square(8.2)
]

print("\n   Processing shapes uniformly:")
print("   " + "-" * 50)
total_area = 0
total_perimeter = 0

for shape in shapes:
    area = shape.calcArea()
    perimeter = shape.calcPerimeter()
    total_area += area
    total_perimeter += perimeter
    
    print(f"   {shape.get_shape_type()}:")
    print(f"     Area: {area:.2f}")
    print(f"     Perimeter: {perimeter:.2f}")
    print("   " + "-" * 50)

print(f"\n   Total area of all shapes: {total_area:.2f}")
print(f"   Total perimeter of all shapes: {total_perimeter:.2f}")

print("\n" + "=" * 80)
print("\n8. Factory pattern using abstract base class:")

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        """Factory method to create shapes"""
        shape_type = shape_type.lower()
        
        if shape_type == "circle":
            return Circle(*args)
        elif shape_type == "square":
            return Square(*args)
        elif shape_type == "rectangle":
            return Rectangle(*args)
        elif shape_type == "triangle":
            return Triangle(*args)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

print("\n   Creating shapes using factory:")
shapes_from_factory = [
    ShapeFactory.create_shape("circle", 5),
    ShapeFactory.create_shape("square", 4),
    ShapeFactory.create_shape("rectangle", 6, 3),
    ShapeFactory.create_shape("triangle", 8, 6, 5, 7, 9)
]

for shape in shapes_from_factory:
    print(f"   Created {shape.get_shape_type()}: Area = {shape.calcArea():.2f}")

print("\n" + "=" * 80)
print("\n9. Adding more abstract methods:")

class ThreeDShape(ABC):
    @abstractmethod
    def calcVolume(self):
        pass
    
    @abstractmethod
    def calcSurfaceArea(self):
        pass
    
    def get_dimensions(self):
        return "3D Shape"

class Sphere(ThreeDShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calcVolume(self):
        return (4/3) * 3.14159 * (self.radius ** 3)
    
    def calcSurfaceArea(self):
        return 4 * 3.14159 * (self.radius ** 2)
    
    def get_dimensions(self):
        return f"Sphere with radius {self.radius}"

class Cube(ThreeDShape):
    def __init__(self, side):
        self.side = side
    
    def calcVolume(self):
        return self.side ** 3
    
    def calcSurfaceArea(self):
        return 6 * (self.side ** 2)
    
    def get_dimensions(self):
        return f"Cube with side {self.side}"

print("\n   3D Shapes (another abstract base class):")
sphere = Sphere(5)
cube = Cube(4)

print(f"   {sphere.get_dimensions()}")
print(f"     Volume: {sphere.calcVolume():.2f}")
print(f"     Surface Area: {sphere.calcSurfaceArea():.2f}")

print(f"\n   {cube.get_dimensions()}")
print(f"     Volume: {cube.calcVolume():.2f}")
print(f"     Surface Area: {cube.calcSurfaceArea():.2f}")

print("\n" + "=" * 80)
print("\n10. Mixing 2D and 3D shapes with common interface:")

class ShapeCollection:
    def __init__(self):
        self.shapes = []
    
    def add_shape(self, shape):
        """Add any shape that implements area calculation"""
        if hasattr(shape, 'calcArea') and callable(shape.calcArea):
            self.shapes.append(shape)
            return f"Added {shape.__class__.__name__}"
        else:
            return f"Cannot add {type(shape).__name__} - missing calcArea method"
    
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calcArea()
        return total

print("\n   Creating shape collection:")
collection = ShapeCollection()

# Add both 2D and 3D shapes (3D shapes don't have calcArea)
print(f"   {collection.add_shape(Circle(5))}")
print(f"   {collection.add_shape(Square(4))}")
print(f"   {collection.add_shape(sphere)}")  # This should fail

print(f"\n   Total area in collection: {collection.total_area():.2f}")

print("\n" + "=" * 80)
print("\n11. Testing the original example requirements:")

print("\n   Original example output:")
print("   " + "=" * 40)

# Recreate original example
orig_circle = Circle(10)
orig_square = Square(12)

print(f"\n   c = Circle(10)")
print(f"   s = Square(12)")
print(f"\n   c.calcArea(): {orig_circle.calcArea():.2f}")
print(f"   s.calcArea(): {orig_square.calcArea():.2f}")

print("\n   Trying to create GraphicShape directly:")
try:
    orig_g = GraphicShape()
    print(f"   ✗ Unexpectedly created: {orig_g}")
except TypeError as e:
    print(f"   ✓ TypeError: {e}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Abstract Base Classes (ABC) enforce method implementation")
print("✓ @abstractmethod decorator marks methods that must be implemented")
print("✓ Abstract classes cannot be instantiated directly")
print("✓ Subclasses must implement all abstract methods")
print("✓ Abstract classes can have both abstract and concrete methods")
print("✓ Enables polymorphism - treating different shapes uniformly")
print("✓ Ensures consistent interfaces across related classes")
print("✓ Useful for creating frameworks and enforcing contracts")