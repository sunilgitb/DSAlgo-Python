# Python Object Oriented Programming
# Using Abstract Base Classes to enforce class constraints

from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def calcArea(self):
        return 3.14159 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def calcArea(self):
        return self.side * self.side


class IncompleteShape(GraphicShape):
    """This class doesn't implement calcArea - should fail"""
    def __init__(self):
        super().__init__()


print("Testing Abstract Base Classes:")
print("=" * 80)

print("1. Trying to instantiate abstract base class:")
try:
    g = GraphicShape()
    print(f"   ✗ Unexpectedly created: {g}")
except TypeError as e:
    print(f"   ✓ Correctly prevented: {e}")

print("\n2. Creating concrete shape instances:")
c = Circle(10)
s = Square(12)

print(f"   Created Circle with radius 10")
print(f"   Created Square with side 12")

print("\n3. Calculating areas:")
print(f"   Circle(10).calcArea(): {c.calcArea():.2f}")
print(f"   Square(12).calcArea(): {s.calcArea():.2f}")

print("\n4. Testing incomplete subclass:")
try:
    incomplete = IncompleteShape()
    print(f"   ✗ Unexpectedly created: {incomplete}")
except TypeError as e:
    print(f"   ✓ Correctly prevented: {e}")

print("\n" + "=" * 80)
print("\nWithout Abstract Base Classes (problem demonstration):")

class ProblematicGraphicShape:
    def __init__(self):
        super().__init__()
    
    def calcArea(self):
        """Default implementation that might not make sense"""
        return 0

class ProblematicCircle(ProblematicGraphicShape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    # Oops! Forgot to implement calcArea

class ProblematicSquare(ProblematicGraphicShape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def calcArea(self):
        return self.side * self.side

print("\n   Creating problematic shapes:")
problematic_g = ProblematicGraphicShape()
problematic_c = ProblematicCircle(10)  # No error!
problematic_s = ProblematicSquare(12)

print(f"   ProblematicCircle(10).calcArea(): {problematic_c.calcArea()}")
print(f"   ProblematicSquare(12).calcArea(): {problematic_s.calcArea()}")

print("\n   Issue: Circle returns 0 instead of calculating area!")
print("   Without ABC, we don't get errors for missing implementations.")

print("\n" + "=" * 80)
print("\nEnhanced example with more shapes and methods:")

class EnhancedGraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        """Calculate area - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def calcPerimeter(self):
        """Calculate perimeter - must be implemented by subclasses"""
        pass
    
    def get_shape_info(self):
        """Non-abstract method available to all subclasses"""
        return f"{self.__class__.__name__}: Area={self.calcArea():.2f}, Perimeter={self.calcPerimeter():.2f}"

class EnhancedCircle(EnhancedGraphicShape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def calcArea(self):
        return 3.14159 * (self.radius ** 2)
    
    def calcPerimeter(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"

class EnhancedSquare(EnhancedGraphicShape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def calcArea(self):
        return self.side * self.side
    
    def calcPerimeter(self):
        return 4 * self.side
    
    def __str__(self):
        return f"Square(side={self.side})"

class Rectangle(EnhancedGraphicShape):
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

print("\n5. Enhanced shapes with more methods:")
circle = EnhancedCircle(7)
square = EnhancedSquare(5)
rectangle = Rectangle(8, 6)

shapes = [circle, square, rectangle]

print("\n   Shape information:")
for shape in shapes:
    print(f"   {shape}: {shape.get_shape_info()}")

print("\n" + "=" * 80)
print("\n6. Practical use case - Shape processor:")

class ShapeProcessor:
    def __init__(self):
        self.shapes = []
    
    def add_shape(self, shape):
        """Add a shape to the processor"""
        if isinstance(shape, EnhancedGraphicShape):
            self.shapes.append(shape)
            return f"Added {shape.__class__.__name__}"
        else:
            raise TypeError(f"Expected EnhancedGraphicShape, got {type(shape).__name__}")
    
    def total_area(self):
        """Calculate total area of all shapes"""
        return sum(shape.calcArea() for shape in self.shapes)
    
    def total_perimeter(self):
        """Calculate total perimeter of all shapes"""
        return sum(shape.calcPerimeter() for shape in self.shapes)
    
    def process_shapes(self):
        """Process all shapes"""
        print(f"   Processing {len(self.shapes)} shapes:")
        for i, shape in enumerate(self.shapes, 1):
            print(f"   {i}. {shape.get_shape_info()}")

print("\n   Creating shape processor:")
processor = ShapeProcessor()

print("\n   Adding shapes:")
for shape in shapes:
    print(f"   {processor.add_shape(shape)}")

print(f"\n   Total area: {processor.total_area():.2f}")
print(f"   Total perimeter: {processor.total_perimeter():.2f}")

processor.process_shapes()

print("\n" + "=" * 80)
print("\n7. Testing the original code requirements:")

print("\n   Original code output:")
print("   " + "-" * 40)

# Recreate the problematic original code
class OriginalGraphicShape:
    def __init__(self):
        super().__init__()

    def calcArea(self):
        pass

class OriginalCircle(OriginalGraphicShape):
    def __init__(self, radius):
        self.radius = radius

class OriginalSquare(OriginalGraphicShape):
    def __init__(self, side):
        self.side = side

# This should work but give wrong results
orig_g = OriginalGraphicShape()
orig_c = OriginalCircle(10)
orig_s = OriginalSquare(12)

print(f"\n   orig_g = GraphicShape() - Created: {orig_g}")
print(f"   orig_c = Circle(10) - Created: {orig_c}")
print(f"   orig_s = Square(12) - Created: {orig_s}")

print(f"\n   orig_c.calcArea(): {orig_c.calcArea()}")
print(f"   orig_s.calcArea(): {orig_s.calcArea()}")

print("\n   Problem: Circle returns None instead of calculating area!")
print("   Solution: Use ABC to enforce method implementation.")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Without ABC: Subclasses can forget to implement methods")
print("✓ With ABC: Compile-time enforcement of method implementation")
print("✓ @abstractmethod marks methods that must be implemented")
print("✓ Abstract classes cannot be instantiated")
print("✓ Ensures consistent interface across subclasses")
print("✓ Prevents runtime errors from missing implementations")
print("✓ Makes code more robust and maintainable")