import csv

class Item:
    pay_rate = 0.8  # 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} must be >= 0!"
        assert quantity >= 0, f"Quantity {quantity} must be >= 0!"
        
        self.__name = name  # Private attribute
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
    
    @property
    def name(self):
        """Getter for name - provides read-only access to private __name"""
        return self.__name
    
    @name.setter
    def name(self, value):
        """Setter for name - validates before setting"""
        if len(value) > 10:
            raise Exception(f"The name '{value}' is too long! Must be 10 characters or less.")
        else:
            self.__name = value
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls, filename='items.csv'):
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                items = list(reader)
            
            for item in items:
                cls(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )
        except FileNotFoundError:
            print(f"File '{filename}' not found. Creating sample data.")
            sample_data = [
                {"name": "Phone", "price": "1000", "quantity": "3"},
                {"name": "Laptop", "price": "1500", "quantity": "2"},
                {"name": "Tablet", "price": "500", "quantity": "5"}
            ]
            
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
                writer.writeheader()
                writer.writerows(sample_data)
            
            cls.instantiate_from_csv(filename)
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken Phones {broken_phones} must be >= 0!"
        self.broken_phones = broken_phones
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, broken={self.broken_phones})"


# Test the Item class with property decorators
print("Testing Item Class with Property Decorators:")
print("=" * 80)

# Create items
item1 = Item("Laptop", 1500, 2)
item2 = Item("Phone", 1000, 3)
phone1 = Phone("iPhone13", 999, 10, 2)

print("1. Created items:")
print(f"   {item1}")
print(f"   {item2}")
print(f"   {phone1}")

print("\n" + "=" * 80)
print("\n2. Testing property getter:")
print(f"   item1.name = {item1.name}")
print(f"   item2.name = {item2.name}")
print(f"   phone1.name = {phone1.name}")

print("\n" + "=" * 80)
print("\n3. Testing property setter:")
print("\n   Testing valid name change (10 chars or less):")
try:
    item1.name = "Desktop"
    print(f"   ✓ Successfully changed item1.name to '{item1.name}'")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n   Testing invalid name change (more than 10 chars):")
try:
    item2.name = "SuperLongProductName"
    print(f"   ✗ Unexpectedly succeeded: {item2.name}")
except Exception as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 80)
print("\n4. Testing encapsulation - direct access to private attribute:")
try:
    print(f"   item1.__name = {item1.__name}")
except AttributeError as e:
    print(f"   ✓ Correctly prevented direct access: {e}")

print("\n   Accessing through property (works):")
print(f"   item1.name = {item1.name}")

print("\n" + "=" * 80)
print("\n5. Testing inheritance with properties:")
print("\n   Phone inherits from Item, so it also has the name property:")
try:
    phone1.name = "GalaxyS22"
    print(f"   ✓ Successfully changed phone1.name to '{phone1.name}'")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n   Testing phone with too long name:")
try:
    phone1.name = "VeryLongPhoneName"
    print(f"   ✗ Unexpectedly succeeded: {phone1.name}")
except Exception as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 80)
print("\n6. Testing other Item functionality:")
print(f"\n   item1.calculate_total_price(): ${item1.calculate_total_price()}")
print(f"   item2.calculate_total_price(): ${item2.calculate_total_price()}")

print("\n   Applying 20% discount:")
item1.apply_discount()
item2.apply_discount()
print(f"   item1.price after discount: ${item1.price}")
print(f"   item2.price after discount: ${item2.price}")

print("\n" + "=" * 80)
print("\n7. Testing class and static methods:")
print("\n   Testing is_integer static method:")
test_numbers = [5, 5.0, 5.5, "5"]
for num in test_numbers:
    print(f"   Item.is_integer({repr(num)}): {Item.is_integer(num)}")

print("\n   Instantiating from CSV:")
Item.all = []  # Clear existing items
Item.instantiate_from_csv()

print(f"\n   Items loaded from CSV ({len(Item.all)} items):")
for item in Item.all:
    print(f"   - {item}")

print("\n" + "=" * 80)
print("\n8. Advanced property testing:")
class ProductWithValidation(Item):
    def __init__(self, name: str, price: float, quantity=0, category=""):
        super().__init__(name, price, quantity)
        self.category = category
    
    @property
    def price(self):
        """Getter for price with logging"""
        print(f"   Getting price for {self.name}: ${self._price}")
        return self._price
    
    @price.setter
    def price(self, value):
        """Setter for price with validation"""
        if value < 0:
            raise ValueError(f"Price cannot be negative: {value}")
        self._price = value
        print(f"   Setting price for {self.name} to: ${value}")

print("\n   Creating ProductWithValidation with validation:")
try:
    prod = ProductWithValidation("ValidProduct", 100, 5, "Electronics")
    print(f"   Created: {prod}")
    
    print(f"\n   Testing price validation:")
    prod.price = 150
    print(f"   Price after update: ${prod.price}")
    
    print(f"\n   Testing invalid price:")
    prod.price = -50
except ValueError as e:
    print(f"   ✓ Correctly rejected invalid price: {e}")

print("\n" + "=" * 80)
print("\n9. All items in system:")
print(f"Total items: {len(Item.all)}")
for idx, item in enumerate(Item.all, 1):
    print(f"   {idx}. {item}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Encapsulation achieved through private attributes (__name)")
print("✓ Property decorators provide controlled access to private data")
print("✓ Getter (@property) allows read access")
print("✓ Setter (@name.setter) allows write access with validation")
print("✓ Inheritance preserves property functionality")
print("✓ Validation ensures data integrity")