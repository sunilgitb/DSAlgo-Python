import csv

class Item:
    pay_rate = 0.8  # 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} must be >= 0!"
        assert quantity >= 0, f"Quantity {quantity} must be >= 0!"
        
        self.__name = name  # Private attribute
        self.__price = price  # Private attribute
        self.quantity = quantity
        
        Item.all.append(self)
    
    @property
    def price(self):
        """Getter for price - read-only access to private __price"""
        return self.__price
    
    def apply_discount(self):
        """Apply 20% discount to the price"""
        self.__price = self.__price * Item.pay_rate
    
    def apply_increment(self, increment_value):
        """Apply percentage increment to the price"""
        self.__price = self.__price + self.__price * increment_value
    
    @property
    def name(self):
        """Getter for name - read-only access to private __name"""
        return self.__name
    
    @name.setter
    def name(self, value):
        """Setter for name - validates name length"""
        if len(value) > 10:
            raise Exception(f"The name '{value}' is too long! Must be 10 characters or less.")
        else:
            self.__name = value
    
    def calculate_total_price(self):
        """Calculate total price for all items"""
        return self.__price * self.quantity
    
    @classmethod
    def instantiate_from_csv(cls, filename='items.csv'):
        """Create items from CSV file"""
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
        """Check if a number is integer (including floats like 5.0)"""
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"


# Test the enhanced Item class
print("Testing Enhanced Item Class with Private Price:")
print("=" * 80)

# Create items
item1 = Item("Laptop", 1500, 2)
item2 = Item("Phone", 1000, 3)

print("1. Created items:")
print(f"   {item1}")
print(f"   {item2}")

print("\n" + "=" * 80)
print("\n2. Testing price property (getter):")
print(f"   item1.price = {item1.price}")
print(f"   item2.price = {item2.price}")

print("\n3. Testing price encapsulation:")
try:
    print(f"   item1.__price = {item1.__price}")
except AttributeError as e:
    print(f"   ✓ Correctly prevented direct access: {e}")

print("\n" + "=" * 80)
print("\n4. Testing apply_discount method:")
print(f"   item1.price before discount: {item1.price}")
item1.apply_discount()
print(f"   item1.price after 20% discount: {item1.price}")

print(f"\n   item2.price before discount: {item2.price}")
item2.apply_discount()
print(f"   item2.price after 20% discount: {item2.price}")

print("\n" + "=" * 80)
print("\n5. Testing apply_increment method:")
print(f"   item1.price before increment: {item1.price}")
item1.apply_increment(0.10)  # 10% increase
print(f"   item1.price after 10% increment: {item1.price}")

print(f"\n   item2.price before increment: {item2.price}")
item2.apply_increment(0.15)  # 15% increase
print(f"   item2.price after 15% increment: {item2.price}")

print("\n" + "=" * 80)
print("\n6. Testing name property (getter and setter):")
print(f"   item1.name = {item1.name}")
print(f"   item2.name = {item2.name}")

print("\n   Changing item names:")
try:
    item1.name = "Desktop"
    print(f"   ✓ Successfully changed item1.name to '{item1.name}'")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n   Testing name length validation:")
try:
    item2.name = "SuperLongProductName"
    print(f"   ✗ Unexpectedly succeeded: {item2.name}")
except Exception as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 80)
print("\n7. Testing calculate_total_price:")
print(f"   item1.calculate_total_price() = {item1.calculate_total_price()}")
print(f"   item2.calculate_total_price() = {item2.calculate_total_price()}")

print("\n" + "=" * 80)
print("\n8. Testing class and static methods:")
print("\n   Testing is_integer static method:")
test_numbers = [5, 5.0, 5.5, "5", -3, -3.0, 0, 0.0]
for num in test_numbers:
    result = Item.is_integer(num)
    print(f"   Item.is_integer({repr(num):6}) = {result}")

print("\n   Instantiating from CSV:")
Item.all = []  # Clear existing items
Item.instantiate_from_csv()

print(f"\n   Items loaded from CSV ({len(Item.all)} items):")
for item in Item.all:
    print(f"   - {item}")

print("\n" + "=" * 80)
print("\n9. Testing with price modifications sequence:")
test_item = Item("TestItem", 100, 5)
print(f"\n   Starting with: {test_item}")
print(f"   Initial total price: {test_item.calculate_total_price()}")

print("\n   Sequence of operations:")
print("   1. Apply 20% discount")
test_item.apply_discount()
print(f"      Price: {test_item.price}, Total: {test_item.calculate_total_price()}")

print("   2. Apply 10% increment")
test_item.apply_increment(0.10)
print(f"      Price: {test_item.price}, Total: {test_item.calculate_total_price()}")

print("   3. Apply another 20% discount")
test_item.apply_discount()
print(f"      Price: {test_item.price}, Total: {test_item.calculate_total_price()}")

print("   4. Change quantity to 10")
test_item.quantity = 10
print(f"      Price: {test_item.price}, Total: {test_item.calculate_total_price()}")

print("\n" + "=" * 80)
print("\n10. Testing encapsulation comprehensively:")
print("\n   Creating an item with negative price (should fail):")
try:
    invalid_item = Item("Invalid", -100, 5)
    print(f"   ✗ Unexpectedly created: {invalid_item}")
except AssertionError as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n   Creating an item with negative quantity (should fail):")
try:
    invalid_item = Item("Invalid", 100, -5)
    print(f"   ✗ Unexpectedly created: {invalid_item}")
except AssertionError as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n   All items in system:")
print(f"   Total items: {len(Item.all)}")
for idx, item in enumerate(Item.all, 1):
    print(f"   {idx}. {item}")

print("\n" + "=" * 80)
print("\n11. Calculating total inventory value:")
total_value = 0
for item in Item.all:
    item_value = item.calculate_total_price()
    print(f"   {item.name}: {item.quantity} @ ${item.price} = ${item_value:.2f}")
    total_value += item_value

print(f"\n   Total inventory value: ${total_value:.2f}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Price is now a private attribute (__price)")
print("✓ Price can only be modified through controlled methods")
print("✓ apply_discount() applies 20% discount")
print("✓ apply_increment() applies percentage increment")
print("✓ Name validation ensures max 10 characters")
print("✓ Encapsulation protects data integrity")
print("✓ Class methods for CSV instantiation")
print("✓ Static methods for utility functions")