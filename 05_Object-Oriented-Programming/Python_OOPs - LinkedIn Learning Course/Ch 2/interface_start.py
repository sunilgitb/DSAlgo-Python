# Python Object Oriented Programming
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


c = Circle(10)
print(c.calcArea())

print("\n" + "=" * 80)
print("Understanding Abstract Base Classes:")
print("=" * 80)

print("\n1. Basic ABC example demonstration:")

# Create more shapes that implement the GraphicShape interface
class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    
    def calcArea(self):
        return self.side * self.side
    
    def __str__(self):
        return f"Square(side={self.side})"


class Rectangle(GraphicShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calcArea(self):
        return self.length * self.width
    
    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"


class Triangle(GraphicShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calcArea(self):
        return 0.5 * self.base * self.height
    
    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height})"


print("\n2. Creating shape instances:")
shapes = [
    Circle(5),
    Square(4),
    Rectangle(6, 3),
    Triangle(8, 5),
    Circle(7.5),
    Square(3.2)
]

for i, shape in enumerate(shapes, 1):
    print(f"   {i}. {shape}: Area = {shape.calcArea():.2f}")

print("\n" + "=" * 80)
print("\n3. Testing ABC enforcement:")

class IncompleteShape(GraphicShape):
    """This class doesn't implement calcArea - should fail"""
    def __init__(self):
        super().__init__()
    
    # Missing calcArea() method

print("\n   Trying to create incomplete shape class:")
try:
    bad_shape = IncompleteShape()
    print(f"   ✗ Unexpectedly created: {bad_shape}")
except TypeError as e:
    print(f"   ✓ Correctly prevented: {e}")

print("\n   Trying to instantiate GraphicShape directly:")
try:
    abstract_shape = GraphicShape()
    print(f"   ✗ Unexpectedly created: {abstract_shape}")
except TypeError as e:
    print(f"   ✓ Correctly prevented: {e}")

print("\n" + "=" * 80)
print("\n4. Adding more methods to the ABC:")

class EnhancedGraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        pass
    
    @abstractmethod
    def calcPerimeter(self):
        pass
    
    def get_shape_type(self):
        return self.__class__.__name__

class EnhancedCircle(EnhancedGraphicShape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def calcArea(self):
        return 3.14159 * (self.radius ** 2)
    
    def calcPerimeter(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"EnhancedCircle(radius={self.radius})"

class EnhancedSquare(EnhancedGraphicShape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def calcArea(self):
        return self.side * self.side
    
    def calcPerimeter(self):
        return 4 * self.side
    
    def __str__(self):
        return f"EnhancedSquare(side={self.side})"

print("\n   Enhanced shapes with perimeter calculation:")
enhanced_shapes = [
    EnhancedCircle(10),
    EnhancedSquare(5),
    EnhancedCircle(3.5),
    EnhancedSquare(7.2)
]

for shape in enhanced_shapes:
    print(f"   {shape}:")
    print(f"     Area: {shape.calcArea():.2f}")
    print(f"     Perimeter: {shape.calcPerimeter():.2f}")
    print(f"     Type: {shape.get_shape_type()}")

print("\n" + "=" * 80)
print("\n5. Polymorphism with ABCs:")

print("\n   Processing shapes uniformly:")
def process_shapes(shape_list):
    total_area = 0
    print("   " + "-" * 40)
    for shape in shape_list:
        area = shape.calcArea()
        total_area += area
        print(f"   {shape.__class__.__name__}: Area = {area:.2f}")
    print("   " + "-" * 40)
    print(f"   Total area: {total_area:.2f}")
    return total_area

print("\n   Processing original shapes:")
process_shapes(shapes)

print("\n   Processing enhanced shapes:")
process_shapes(enhanced_shapes)

print("\n" + "=" * 80)
print("\n6. Real-world example - Shape collection:")

class ShapeCollection:
    def __init__(self, name):
        self.name = name
        self.shapes = []
    
    def add_shape(self, shape):
        if isinstance(shape, GraphicShape):
            self.shapes.append(shape)
            return f'Added {shape.__class__.__name__} to {self.name}'
        else:
            raise TypeError(f"Cannot add {type(shape).__name__} - must be a GraphicShape")
    
    def total_area(self):
        return sum(shape.calcArea() for shape in self.shapes)
    
    def average_area(self):
        if not self.shapes:
            return 0
        return self.total_area() / len(self.shapes)
    
    def list_shapes(self):
        if not self.shapes:
            return f"{self.name} has no shapes"
        
        result = f"Shapes in {self.name}:\n"
        for i, shape in enumerate(self.shapes, 1):
            result += f"  {i}. {shape.__class__.__name__}: Area = {shape.calcArea():.2f}\n"
        result += f"\n  Total area: {self.total_area():.2f}"
        result += f"\n  Average area: {self.average_area():.2f}"
        return result

print("\n   Creating a shape collection:")
my_collection = ShapeCollection("My Geometry Collection")

print("\n   Adding shapes to collection:")
for shape in shapes + enhanced_shapes:
    try:
        print(f"   {my_collection.add_shape(shape)}")
    except TypeError as e:
        print(f"   Error: {e}")

print(f"\n   {my_collection.list_shapes()}")

print("\n" + "=" * 80)
print("\n7. Extending the ABC hierarchy:")

class ThreeDShape(ABC):
    @abstractmethod
    def calcVolume(self):
        pass
    
    @abstractmethod
    def calcSurfaceArea(self):
        pass

class Sphere(ThreeDShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calcVolume(self):
        return (4/3) * 3.14159 * (self.radius ** 3)
    
    def calcSurfaceArea(self):
        return 4 * 3.14159 * (self.radius ** 2)
    
    def __str__(self):
        return f"Sphere(radius={self.radius})"

class Cube(ThreeDShape):
    def __init__(self, side):
        self.side = side
    
    def calcVolume(self):
        return self.side ** 3
    
    def calcSurfaceArea(self):
        return 6 * (self.side ** 2)
    
    def __str__(self):
        return f"Cube(side={self.side})"

print("\n   3D Shapes (separate ABC hierarchy):")
three_d_shapes = [
    Sphere(5),
    Cube(4),
    Sphere(2.5),
    Cube(3.3)
]

for shape in three_d_shapes:
    print(f"   {shape}:")
    print(f"     Volume: {shape.calcVolume():.2f}")
    print(f"     Surface Area: {shape.calcSurfaceArea():.2f}")

print("\n" + "=" * 80)
print("\n8. Multiple ABC implementation:")

class ShapeWithBoth(GraphicShape, ThreeDShape):
    """A shape that implements both 2D and 3D interfaces"""
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        pass
    
    @abstractmethod
    def calcVolume(self):
        pass
    
    @abstractmethod
    def calcSurfaceArea(self):
        pass

class Cylinder(ShapeWithBoth):
    def __init__(self, radius, height):
        super().__init__()
        self.radius = radius
        self.height = height
    
    def calcArea(self):
        # Base area (circle)
        return 3.14159 * (self.radius ** 2)
    
    def calcVolume(self):
        return self.calcArea() * self.height
    
    def calcSurfaceArea(self):
        # 2πr² + 2πrh
        base_area = 2 * self.calcArea()
        side_area = 2 * 3.14159 * self.radius * self.height
        return base_area + side_area
    
    def __str__(self):
        return f"Cylinder(radius={self.radius}, height={self.height})"

print("\n   Cylinder implements both GraphicShape and ThreeDShape:")
cylinder = Cylinder(3, 5)
print(f"   {cylinder}")
print(f"   Base Area: {cylinder.calcArea():.2f}")
print(f"   Volume: {cylinder.calcVolume():.2f}")
print(f"   Surface Area: {cylinder.calcSurfaceArea():.2f}")

print(f"\n   Type checking:")
print(f"   isinstance(cylinder, GraphicShape): {isinstance(cylinder, GraphicShape)}")
print(f"   isinstance(cylinder, ThreeDShape): {isinstance(cylinder, ThreeDShape)}")
print(f"   isinstance(cylinder, ShapeWithBoth): {isinstance(cylinder, ShapeWithBoth)}")

print("\n" + "=" * 80)
print("\n9. Testing the original example in detail:")

print("\n   Original example step by step:")
print("   1. from abc import ABC, abstractmethod")
print("   2. class GraphicShape(ABC):")
print("   3.     @abstractmethod")
print("   4.     def calcArea(self): pass")
print("   5. ")
print("   6. class Circle(GraphicShape):")
print("   7.     def __init__(self, radius):")
print("   8.         self.radius = radius")
print("   9. ")
print("   10.    def calcArea(self):")
print("   11.        return 3.14 * (self.radius ** 2)")
print("   12. ")
print("   13. c = Circle(10)")
print("   14. print(c.calcArea())")

print(f"\n   Result: {c.calcArea()}")

print("\n   What makes this work:")
print("   • GraphicShape is an Abstract Base Class (ABC)")
print("   • calcArea() is marked with @abstractmethod")
print("   • Circle inherits from GraphicShape")
print("   • Circle implements calcArea() method")
print("   • Python enforces that abstract methods are implemented")

print("\n" + "=" * 80)
print("\n10. Benefits of using ABCs:")

print("\n   Without ABCs:")
print("   • No enforcement of method implementation")
print("   • Runtime errors when methods are missing")
print("   • No clear interface definition")
print("   • Hard to maintain consistent APIs")

print("\n   With ABCs:")
print("   • Clear interface definition")
print("   • Compile-time enforcement")
print("   • Better documentation of expected behavior")
print("   • Enables polymorphism")
print("   • Prevents instantiation of incomplete classes")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ ABCs define abstract interfaces that classes must implement")
print("✓ @abstractmethod decorator marks methods that must be overridden")
print("✓ Abstract classes cannot be instantiated directly")
print("✓ Subclasses must implement all abstract methods")
print("✓ Enables polymorphism - treating different shapes uniformly")
print("✓ Provides compile-time checks for interface compliance")
print("✓ Useful for creating frameworks and enforcing contracts")
print("✓ Multiple inheritance allows implementing multiple interfaces")