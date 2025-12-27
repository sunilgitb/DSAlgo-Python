# Python Object Oriented Programming
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod
import json

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass
    
    @abstractmethod
    def calcPerimeter(self):
        pass


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class XMLify(ABC):
    @abstractmethod
    def toXML(self):
        pass


class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(GraphicShape, JSONify, XMLify, Drawable):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.name = "Circle"

    def calcArea(self):
        return 3.14159 * (self.radius ** 2)
    
    def calcPerimeter(self):
        return 2 * 3.14159 * self.radius

    def toJSON(self):
        return {
            "shape": self.name,
            "radius": self.radius,
            "area": self.calcArea(),
            "perimeter": self.calcPerimeter()
        }
    
    def toPrettyJSON(self):
        return json.dumps(self.toJSON(), indent=2)
    
    def toXML(self):
        return f'''<shape>
    <type>{self.name}</type>
    <radius>{self.radius}</radius>
    <area>{self.calcArea():.2f}</area>
    <perimeter>{self.calcPerimeter():.2f}</perimeter>
</shape>'''
    
    def draw(self):
        return f"Drawing a {self.name} with radius {self.radius}"
    
    def __str__(self):
        return f"{self.name}(radius={self.radius})"


class Square(GraphicShape, JSONify):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.name = "Square"

    def calcArea(self):
        return self.side * self.side
    
    def calcPerimeter(self):
        return 4 * self.side

    def toJSON(self):
        return {
            "shape": self.name,
            "side": self.side,
            "area": self.calcArea(),
            "perimeter": self.calcPerimeter()
        }
    
    def __str__(self):
        return f"{self.name}(side={self.side})"


class Rectangle(GraphicShape, JSONify, XMLify):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.name = "Rectangle"

    def calcArea(self):
        return self.length * self.width
    
    def calcPerimeter(self):
        return 2 * (self.length + self.width)

    def toJSON(self):
        return {
            "shape": self.name,
            "length": self.length,
            "width": self.width,
            "area": self.calcArea(),
            "perimeter": self.calcPerimeter()
        }
    
    def toXML(self):
        return f'''<shape>
    <type>{self.name}</type>
    <length>{self.length}</length>
    <width>{self.width}</width>
    <area>{self.calcArea():.2f}</area>
    <perimeter>{self.calcPerimeter():.2f}</perimeter>
</shape>'''
    
    def __str__(self):
        return f"{self.name}(length={self.length}, width={self.width})"


class Triangle(GraphicShape):
    """Triangle implements only GraphicShape, not JSONify"""
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
        self.name = "Triangle"

    def calcArea(self):
        return 0.5 * self.base * self.height
    
    def calcPerimeter(self):
        # For simplicity, assume right triangle
        hypotenuse = (self.base**2 + self.height**2) ** 0.5
        return self.base + self.height + hypotenuse
    
    def __str__(self):
        return f"{self.name}(base={self.base}, height={self.height})"


print("Testing Abstract Base Classes as Interfaces:")
print("=" * 80)

print("\n1. Creating shapes with multiple interfaces:")

c = Circle(10)
s = Square(5)
r = Rectangle(8, 6)
t = Triangle(10, 5)

print(f"   Created shapes:")
print(f"   {c}")
print(f"   {s}")
print(f"   {r}")
print(f"   {t}")

print("\n" + "=" * 80)
print("\n2. Testing GraphicShape interface (all shapes):")

print("\n   Calculating area and perimeter:")
for shape in [c, s, r, t]:
    print(f"   {shape}:")
    print(f"     Area: {shape.calcArea():.2f}")
    print(f"     Perimeter: {shape.calcPerimeter():.2f}")

print("\n" + "=" * 80)
print("\n3. Testing JSONify interface (only some shapes):")

print("\n   Shapes that implement JSONify:")
json_shapes = [c, s, r]
for shape in json_shapes:
    print(f"\n   {shape}:")
    print(f"     JSON data: {shape.toJSON()}")
    if hasattr(shape, 'toPrettyJSON'):
        print(f"     Pretty JSON:")
        print(shape.toPrettyJSON())

print("\n   Checking which shapes implement JSONify:")
for shape in [c, s, r, t]:
    implements_json = isinstance(shape, JSONify)
    print(f"   {shape} implements JSONify: {implements_json}")

print("\n" + "=" * 80)
print("\n4. Testing XMLify interface:")

print("\n   Shapes that implement XMLify:")
xml_shapes = [c, r]
for shape in xml_shapes:
    print(f"\n   {shape}:")
    print(f"     XML:")
    print(shape.toXML())

print("\n" + "=" * 80)
print("\n5. Testing Drawable interface:")

print("\n   Shapes that implement Drawable:")
drawable_shapes = [c]  # Only Circle implements Drawable
for shape in drawable_shapes:
    print(f"   {shape.draw()}")

print("\n" + "=" * 80)
print("\n6. Original example demonstration:")

print("\n   Original Circle example:")
orig_circle = Circle(10)
print(f"   c = Circle(10)")
print(f"   c.calcArea(): {orig_circle.calcArea():.2f}")
print(f"   c.toJSON(): {orig_circle.toJSON()}")

print("\n" + "=" * 80)
print("\n7. Interface enforcement:")

print("\n   Trying to create class without implementing all abstract methods:")

class IncompleteShape(GraphicShape, JSONify):
    """This class doesn't implement all abstract methods"""
    def __init__(self):
        super().__init__()
    
    # Missing calcArea(), calcPerimeter(), and toJSON()

print("   Testing incomplete class:")
try:
    incomplete = IncompleteShape()
    print(f"   ✗ Unexpectedly created: {incomplete}")
except TypeError as e:
    print(f"   ✓ Correctly prevented: {e}")

print("\n   Creating complete implementation:")

class CompleteCircle(GraphicShape, JSONify):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def calcArea(self):
        return 3.14159 * (self.radius ** 2)
    
    def calcPerimeter(self):
        return 2 * 3.14159 * self.radius
    
    def toJSON(self):
        return {"radius": self.radius, "area": self.calcArea()}

print("   Testing complete class:")
try:
    complete = CompleteCircle(5)
    print(f"   ✓ Successfully created: {complete}")
    print(f"   Area: {complete.calcArea():.2f}")
    print(f"   JSON: {complete.toJSON()}")
except TypeError as e:
    print(f"   ✗ Error: {e}")

print("\n" + "=" * 80)
print("\n8. Practical example - Shape processor:")

class ShapeProcessor:
    def __init__(self):
        self.shapes = []
    
    def add_shape(self, shape):
        """Add any GraphicShape to processor"""
        if isinstance(shape, GraphicShape):
            self.shapes.append(shape)
            return f"Added {shape}"
        else:
            raise TypeError("Only GraphicShape objects can be added")
    
    def process_all(self):
        """Process all shapes according to their interfaces"""
        print("\n   Processing shapes:")
        print("   " + "-" * 50)
        
        total_area = 0
        total_perimeter = 0
        
        for i, shape in enumerate(self.shapes, 1):
            print(f"\n   {i}. {shape}")
            
            # All shapes have these methods (GraphicShape interface)
            area = shape.calcArea()
            perimeter = shape.calcPerimeter()
            total_area += area
            total_perimeter += perimeter
            
            print(f"     Area: {area:.2f}")
            print(f"     Perimeter: {perimeter:.2f}")
            
            # Check for JSONify interface
            if isinstance(shape, JSONify):
                print(f"     JSON data available")
            
            # Check for XMLify interface
            if isinstance(shape, XMLify):
                print(f"     XML data available")
            
            # Check for Drawable interface
            if isinstance(shape, Drawable):
                print(f"     {shape.draw()}")
        
        print("\n   " + "-" * 50)
        print(f"   Total area: {total_area:.2f}")
        print(f"   Total perimeter: {total_perimeter:.2f}")
    
    def export_to_json(self):
        """Export all JSONify shapes to JSON"""
        json_shapes = [shape for shape in self.shapes if isinstance(shape, JSONify)]
        if not json_shapes:
            return "No shapes support JSON export"
        
        result = {"shapes": []}
        for shape in json_shapes:
            result["shapes"].append(shape.toJSON())
        
        return json.dumps(result, indent=2)

print("\n   Creating shape processor:")
processor = ShapeProcessor()

print("\n   Adding shapes to processor:")
for shape in [c, s, r, t]:
    print(f"   {processor.add_shape(shape)}")

processor.process_all()

print("\n   Exporting to JSON:")
print(processor.export_to_json())

print("\n" + "=" * 80)
print("\n9. Multiple inheritance with interfaces:")

print("\n   Checking what interfaces each shape implements:")
interfaces_to_check = [GraphicShape, JSONify, XMLify, Drawable]

for shape in [c, s, r, t]:
    print(f"\n   {shape}:")
    for interface in interfaces_to_check:
        implements = isinstance(shape, interface)
        print(f"     {interface.__name__}: {implements}")

print("\n" + "=" * 80)
print("\n10. Adding new interfaces:")

class Scalable(ABC):
    @abstractmethod
    def scale(self, factor):
        pass
    
    @abstractmethod
    def get_scale_info(self):
        pass

class ScalableCircle(Circle, Scalable):
    def __init__(self, radius):
        super().__init__(radius)
        self.scale_factor = 1.0
    
    def scale(self, factor):
        self.scale_factor *= factor
        self.radius *= factor
        return f"Scaled by {factor}. New radius: {self.radius}"
    
    def get_scale_info(self):
        return f"Current scale: {self.scale_factor}x, Radius: {self.radius}"
    
    def toJSON(self):
        data = super().toJSON()
        data["scale_factor"] = self.scale_factor
        return data

print("\n   Creating scalable circle:")
scalable_circle = ScalableCircle(5)
print(f"   {scalable_circle}")
print(f"   {scalable_circle.scale(2)}")
print(f"   {scalable_circle.scale(1.5)}")
print(f"   {scalable_circle.get_scale_info()}")
print(f"   JSON with scale info: {scalable_circle.toJSON()}")

print("\n   Checking interfaces:")
print(f"   Implements Scalable: {isinstance(scalable_circle, Scalable)}")
print(f"   Implements GraphicShape: {isinstance(scalable_circle, GraphicShape)}")
print(f"   Implements JSONify: {isinstance(scalable_circle, JSONify)}")

print("\n" + "=" * 80)
print("\nSummary of Abstract Base Classes as Interfaces:")
print("✓ ABCs define contracts that classes must fulfill")
print("✓ @abstractmethod marks methods that must be implemented")
print("✓ Classes can implement multiple interfaces (multiple inheritance)")
print("✓ isinstance() checks if object implements an interface")
print("✓ Interfaces enable polymorphism across unrelated classes")
print("✓ Ensures consistent API across different implementations")
print("✓ Provides compile-time checks for interface compliance")
print("✓ Enables building flexible, extensible systems")