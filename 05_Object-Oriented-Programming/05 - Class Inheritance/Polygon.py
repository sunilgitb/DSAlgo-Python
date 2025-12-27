class Polygon:
    __height = None   # Private class attributes
    __width = None    # Private class attributes
    
    def set_values(self, height, width):
        self.__height = height
        self.__width = width
    
    def get_height(self):
        return self.__height
    
    def get_width(self):
        return self.__width


class Rectangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width()
    
    def perimeter(self):
        return 2 * (self.get_height() + self.get_width())


class Triangle(Polygon):
    def area(self):
        return (self.get_width() * self.get_height()) / 2
    
    def perimeter(self):
        # Assuming right triangle for simplicity
        # Using Pythagorean theorem
        import math
        return self.get_width() + self.get_height() + math.sqrt(
            self.get_width()**2 + self.get_height()**2
        )


class Square(Rectangle):
    def set_side(self, side):
        super().set_values(side, side)
    
    def set_values(self, height, width):
        if height != width:
            print("Warning: Square should have equal sides. Setting both to first value.")
        super().set_values(height, height)


# Test the classes
print("Testing Polygon Inheritance and Encapsulation:")
print("=" * 80)

# Create instances
rect = Rectangle()
tri = Triangle()
square = Square()

# Set values
print("\n1. Setting dimensions:")
rect.set_values(50, 40)
tri.set_values(50, 40)
square.set_side(30)

print(f"   Rectangle: height={rect.get_height()}, width={rect.get_width()}")
print(f"   Triangle: height={tri.get_height()}, width={tri.get_width()}")
print(f"   Square: side={square.get_height()}")

print("\n" + "=" * 80)
print("\n2. Calculating areas:")
print(f"   Rectangle area: {rect.area()} square units")
print(f"   Triangle area: {tri.area()} square units")
print(f"   Square area: {square.area()} square units")

print("\n" + "=" * 80)
print("\n3. Calculating perimeters:")
print(f"   Rectangle perimeter: {rect.perimeter()} units")
print(f"   Triangle perimeter: {tri.perimeter():.2f} units")
print(f"   Square perimeter: {square.perimeter()} units")

print("\n" + "=" * 80)
print("\n4. Testing encapsulation (private attributes):")

print("\n   Trying to access private attributes directly (should fail):")
try:
    print(f"   rect.__height = {rect.__height}")
except AttributeError as e:
    print(f"   ✓ AttributeError: {e}")

try:
    print(f"   tri.__width = {tri.__width}")
except AttributeError as e:
    print(f"   ✓ AttributeError: {e}")

print("\n   Accessing through getter methods (should work):")
print(f"   rect.get_height() = {rect.get_height()}")
print(f"   tri.get_width() = {tri.get_width()}")

print("\n" + "=" * 80)
print("\n5. Testing Square class specifically:")
square2 = Square()
square2.set_values(10, 20)  # Should show warning
print(f"   Square dimensions after set_values(10, 20):")
print(f"   Height: {square2.get_height()}, Width: {square2.get_width()}")
print(f"   Area: {square2.area()}")
print(f"   Perimeter: {square2.perimeter()}")

print("\n" + "=" * 80)
print("\n6. Testing with different dimensions:")

# Multiple rectangles
rectangles = [
    ("Small", 5, 3),
    ("Medium", 10, 6),
    ("Large", 15, 9)
]

print("\n   Rectangles with different sizes:")
for name, h, w in rectangles:
    r = Rectangle()
    r.set_values(h, w)
    print(f"   {name}: {h}x{w}, Area: {r.area()}, Perimeter: {r.perimeter()}")

# Multiple triangles
triangles = [
    ("Right Triangle 3-4-5", 3, 4),
    ("Right Triangle 6-8-10", 6, 8),
    ("Right Triangle 5-12-13", 5, 12)
]

print("\n   Right triangles (height and width as legs):")
for name, h, w in triangles:
    t = Triangle()
    t.set_values(h, w)
    print(f"   {name}: legs {h}x{w}, Area: {t.area()}, Perimeter: {t.perimeter():.2f}")

print("\n" + "=" * 80)
print("\n7. Testing inheritance hierarchy:")
print("   Polygon (Base Class)")
print("   ├── Rectangle")
print("   │   └── Square")
print("   └── Triangle")

print("\n   Method availability:")
rect_test = Rectangle()
rect_test.set_values(7, 5)

print(f"   Can Rectangle access Polygon methods?")
print(f"   - set_values(): {hasattr(rect_test, 'set_values')}")
print(f"   - get_height(): {hasattr(rect_test, 'get_height')}")
print(f"   - get_width(): {hasattr(rect_test, 'get_width')}")
print(f"   - area(): {hasattr(rect_test, 'area')}")
print(f"   - perimeter(): {hasattr(rect_test, 'perimeter')}")

print("\n" + "=" * 80)
print("\n8. Demonstration of polymorphism:")

shapes = [rect, tri, square]
print("\n   Processing different shapes uniformly:")
for i, shape in enumerate(shapes, 1):
    print(f"\n   Shape {i} ({shape.__class__.__name__}):")
    print(f"     Height: {shape.get_height()}")
    print(f"     Width: {shape.get_width()}")
    print(f"     Area: {shape.area()}")
    if hasattr(shape, 'perimeter'):
        print(f"     Perimeter: {shape.perimeter():.2f}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Encapsulation achieved through private attributes")
print("✓ Inheritance allows code reuse")
print("✓ Polymorphism enables uniform treatment of different shapes")
print("✓ Getter methods provide controlled access to private data")