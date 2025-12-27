# Recreating the Item class from earlier to demonstrate inheritance
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
        """Apply discount using class pay_rate"""
        self.__price = self.__price * self.pay_rate
    
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
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"


class Keyboard(Item):
    pay_rate = 0.7  # Class-specific discount rate (30% off)
    
    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)
    
    def get_keyboard_type(self):
        """Keyboard-specific method"""
        if "mechanical" in self.name.lower():
            return "Mechanical"
        elif "membrane" in self.name.lower():
            return "Membrane"
        elif "wireless" in self.name.lower():
            return "Wireless"
        else:
            return "Standard"
    
    def __repr__(self):
        keyboard_type = self.get_keyboard_type()
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, type={keyboard_type})"


class Phone(Item):
    pay_rate = 0.75  # 25% discount for phones
    
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken Phones {broken_phones} must be >= 0!"
        self.broken_phones = broken_phones
    
    def calculate_working_items(self):
        """Override to account for broken phones"""
        return self.quantity - self.broken_phones
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, broken={self.broken_phones})"


# Test the Keyboard class
print("Testing Keyboard Class with Class-Specific Discount Rate:")
print("=" * 80)

# Create items
keyboard1 = Keyboard("MechanicalKB", 150, 10)
keyboard2 = Keyboard("WirelessKeyboard", 100, 5)
phone1 = Phone("iPhone13", 999, 5, 1)
item1 = Item("GenericItem", 50, 20)

print("1. Created items with different discount rates:")
print(f"   {keyboard1}")
print(f"   {keyboard2}")
print(f"   {phone1}")
print(f"   {item1}")

print("\n" + "=" * 80)
print("\n2. Testing class-specific discount rates:")
print(f"\n   Class pay rates:")
print(f"   Item.pay_rate = {Item.pay_rate} (20% discount)")
print(f"   Keyboard.pay_rate = {Keyboard.pay_rate} (30% discount)")
print(f"   Phone.pay_rate = {Phone.pay_rate} (25% discount)")

print(f"\n   Applying discounts:")
print(f"   Keyboard 'MechanicalKB' before discount: ${keyboard1.price}")
keyboard1.apply_discount()
print(f"   After Keyboard discount (30%): ${keyboard1.price}")

print(f"\n   Phone 'iPhone13' before discount: ${phone1.price}")
phone1.apply_discount()
print(f"   After Phone discount (25%): ${phone1.price}")

print(f"\n   Generic Item before discount: ${item1.price}")
item1.apply_discount()
print(f"   After Item discount (20%): ${item1.price}")

print("\n" + "=" * 80)
print("\n3. Testing Keyboard-specific methods:")
print(f"\n   Keyboard type detection:")
print(f"   {keyboard1.name} -> {keyboard1.get_keyboard_type()}")
print(f"   {keyboard2.name} -> {keyboard2.get_keyboard_type()}")

print("\n   Creating more keyboards:")
keyboard3 = Keyboard("Membrane Keyboard", 60, 15)
keyboard4 = Keyboard("Standard KB", 40, 25)
print(f"   {keyboard3}")
print(f"   {keyboard4}")

print("\n" + "=" * 80)
print("\n4. Testing inheritance chain:")

print(f"\n   Keyboard is a subclass of Item:")
print(f"   isinstance(keyboard1, Keyboard): {isinstance(keyboard1, Keyboard)}")
print(f"   isinstance(keyboard1, Item): {isinstance(keyboard1, Item)}")
print(f"   Keyboard.__bases__: {Keyboard.__bases__}")

print(f"\n   All items can use Item methods:")
print(f"   keyboard1.calculate_total_price(): ${keyboard1.calculate_total_price()}")
print(f"   phone1.calculate_total_price(): ${phone1.calculate_total_price()}")
print(f"   item1.calculate_total_price(): ${item1.calculate_total_price()}")

print("\n" + "=" * 80)
print("\n5. Testing polymorphism with apply_discount:")

items = [keyboard1, keyboard2, phone1, item1]
print("\n   Applying discounts to all items:")
for item in items:
    original_price = item.price
    item.apply_discount()  # Each uses its own class's pay_rate
    print(f"   {item.name}: ${original_price} -> ${item.price}")

print("\n" + "=" * 80)
print("\n6. All items in system:")
Item.all = []  # Clear the list

# Create new items
kb1 = Keyboard("Gaming Keyboard", 120, 8)
kb2 = Keyboard("Office Keyboard", 80, 12)
ph1 = Phone("AndroidPhone", 600, 10, 2)
it1 = Item("Mouse", 30, 15)
ph2 = Phone("FlagshipPhone", 1200, 3, 0)

print(f"\n   Total items: {len(Item.all)}")
for idx, item in enumerate(Item.all, 1):
    item_type = item.__class__.__name__
    discount_rate = (1 - item.pay_rate) * 100
    print(f"   {idx}. [{item_type}] {item} ({discount_rate:.0f}% discount rate)")

print("\n" + "=" * 80)
print("\n7. Inventory calculation with different discount rates:")

print("\n   Inventory value calculation:")
total_value_before = 0
total_value_after = 0

print("\n   Item breakdown:")
for item in Item.all:
    # Store original price
    temp_price = item.price
    
    # Calculate value before discount
    value_before = temp_price * item.quantity
    
    # Apply discount and calculate value after
    item.apply_discount()
    value_after = item.price * item.quantity
    
    print(f"\n   {item.__class__.__name__}: {item.name}")
    print(f"     Quantity: {item.quantity}")
    print(f"     Original price: ${temp_price}")
    print(f"     Discounted price: ${item.price:.2f}")
    print(f"     Value before discount: ${value_before:.2f}")
    print(f"     Value after discount: ${value_after:.2f}")
    
    total_value_before += value_before
    total_value_after += value_after

print(f"\n   Total inventory value:")
print(f"   Before discounts: ${total_value_before:.2f}")
print(f"   After discounts: ${total_value_after:.2f}")
print(f"   Total savings: ${total_value_before - total_value_after:.2f}")

print("\n" + "=" * 80)
print("\n8. Testing class hierarchy and method resolution:")

print("\n   Method Resolution Order (MRO) for Keyboard:")
for cls in Keyboard.__mro__:
    print(f"   → {cls.__name__}")

print(f"\n   Keyboard has its own pay_rate: {Keyboard.pay_rate}")
print(f"   Item (parent) pay_rate: {Item.pay_rate}")
print(f"   Keyboard instance uses Keyboard.pay_rate: {keyboard1.pay_rate}")

print("\n   Demonstrating attribute lookup:")
print(f"   hasattr(keyboard1, 'pay_rate'): {hasattr(keyboard1, 'pay_rate')}")
print(f"   keyboard1.pay_rate: {keyboard1.pay_rate}")
print(f"   Item.pay_rate: {Item.pay_rate}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Keyboard class inherits from Item")
print("✓ Keyboard has its own class attribute: pay_rate = 0.7 (30% discount)")
print("✓ Class-specific discount rates allow different pricing strategies")
print("✓ Method resolution follows inheritance hierarchy")
print("✓ Polymorphism: apply_discount() uses the appropriate pay_rate for each class")
print("✓ Each subclass can override parent class attributes and methods")