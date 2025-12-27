# Recreating the Item class from earlier to demonstrate inheritance
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
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception(f"The name '{value}' is too long! Must be 10 characters or less.")
        else:
            self.__name = value
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate
    
    def calculate_working_items(self):
        return self.quantity
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)
        
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} must be >= 0!"
        
        # Assign to self object
        self.broken_phones = broken_phones
    
    def calculate_working_items(self):
        """Override parent method to account for broken phones"""
        return self.quantity - self.broken_phones
    
    def calculate_value_of_working_phones(self):
        """Phone-specific method"""
        return self.calculate_working_items() * self.price
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, broken={self.broken_phones})"


# Test the Phone class
print("Testing Phone Class Inheritance:")
print("=" * 80)

# Create some phones
phone1 = Phone("iPhone13", 999, 10, 2)
phone2 = Phone("SamsungS22", 899, 8, 1)
phone3 = Phone("GoogleP6", 699, 5, 0)

print("1. Created Phone instances:")
print(f"   {phone1}")
print(f"   {phone2}")
print(f"   {phone3}")

print("\n" + "=" * 80)
print("\n2. Testing inherited attributes and methods:")

print(f"\n   Phone inherits from Item, so it has all Item attributes:")
print(f"   phone1.name = {phone1.name}")
print(f"   phone1.price = ${phone1.price}")
print(f"   phone1.quantity = {phone1.quantity}")

print(f"\n   Phone-specific attribute:")
print(f"   phone1.broken_phones = {phone1.broken_phones}")

print(f"\n   Using inherited methods:")
print(f"   phone1.calculate_total_price() = ${phone1.calculate_total_price():.2f}")

print("\n   Applying discount (inherited method):")
phone1.apply_discount()
print(f"   After 20% discount: phone1.price = ${phone1.price:.2f}")

print("\n" + "=" * 80)
print("\n3. Testing Phone-specific methods:")

print(f"\n   Calculating working phones:")
print(f"   phone1: {phone1.quantity} total, {phone1.broken_phones} broken")
print(f"   Working phones: {phone1.calculate_working_items()}")

print(f"\n   Calculating value of working phones:")
print(f"   phone1: ${phone1.calculate_value_of_working_phones():.2f}")

print("\n   All phones:")
for phone in [phone1, phone2, phone3]:
    working = phone.calculate_working_items()
    value = phone.calculate_value_of_working_phones()
    print(f"   {phone.name}: {working} working phones worth ${value:.2f}")

print("\n" + "=" * 80)
print("\n4. Testing polymorphism - overriding parent method:")

# Create a regular Item for comparison
item1 = Item("Generic Item", 100, 5)
print(f"\n   Regular Item: {item1}")
print(f"   item1.calculate_working_items() = {item1.calculate_working_items()}")

print(f"\n   Phone: {phone1}")
print(f"   phone1.calculate_working_items() = {phone1.calculate_working_items()} (accounts for broken phones)")

print("\n" + "=" * 80)
print("\n5. Testing validation in Phone class:")

print("\n   Testing with valid broken phones:")
try:
    valid_phone = Phone("ValidPhone", 500, 10, 3)
    print(f"   ✓ Created phone with {valid_phone.broken_phones} broken phones")
except AssertionError as e:
    print(f"   ✗ Error: {e}")

print("\n   Testing with invalid broken phones (negative):")
try:
    invalid_phone = Phone("InvalidPhone", 500, 10, -1)
    print(f"   ✗ Unexpectedly created phone: {invalid_phone}")
except AssertionError as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 80)
print("\n6. Testing property inheritance:")

print("\n   Phone inherits the name property from Item:")
print(f"   Current phone2.name: {phone2.name}")

print("\n   Testing name setter (max 10 chars):")
try:
    phone2.name = "Pixel6a"
    print(f"   ✓ Successfully changed to '{phone2.name}'")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n   Testing with too long name:")
try:
    phone2.name = "VeryLongPhoneName"
    print(f"   ✗ Unexpectedly succeeded: {phone2.name}")
except Exception as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" = "*" = 80)
print("\n7. All items in the system (including phones):")
Item.all = []  # Clear the list

# Create new instances
phone4 = Phone("iPhone14", 1099, 15, 3)
phone5 = Phone("GalaxyZ", 1299, 8, 1)
regular_item = Item("Tablet", 499, 10)

print(f"\n   Total items in system: {len(Item.all)}")
for idx, item in enumerate(Item.all, 1):
    item_type = item.__class__.__name__
    print(f"   {idx}. [{item_type}] {item}")

print("\n" + "=" * 80)
print("\n8. Calculating total inventory value:")

total_value = 0
total_working_items = 0

print("\n   Inventory breakdown:")
for item in Item.all:
    if isinstance(item, Phone):
        working = item.calculate_working_items()
        value = item.calculate_value_of_working_phones()
        print(f"   {item.name}: {working} working phones @ ${item.price} each = ${value:.2f}")
        total_working_items += working
        total_value += value
    else:
        working = item.calculate_working_items()
        value = item.calculate_total_price()
        print(f"   {item.name}: {working} items @ ${item.price} each = ${value:.2f}")
        total_working_items += working
        total_value += value

print(f"\n   Total working items: {total_working_items}")
print(f"   Total inventory value: ${total_value:.2f}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Phone class successfully inherits from Item")
print("✓ super().__init__() calls parent constructor")
print("✓ Phone adds its own attributes (broken_phones)")
print("✓ Phone can override parent methods (calculate_working_items)")
print("✓ Phone can add new methods (calculate_value_of_working_phones)")
print("✓ Inheritance enables code reuse and polymorphism")