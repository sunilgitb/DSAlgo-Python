# First, let's recreate the Item class
class Item:
    pay_rate = 0.8  # 20% discount for general items
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} must be >= 0!"
        assert quantity >= 0, f"Quantity {quantity} must be >= 0!"
        
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        Item.all.append(self)
    
    @property
    def price(self):
        return self.__price
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception(f"The name '{value}' is too long! Must be 10 characters or less.")
        else:
            self.__name = value
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


# Now define the Phone class with 50% discount
class Phone(Item):
    pay_rate = 0.5  # 50% discount for phones
    
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} must be >= 0!"

        # Assign to self object
        self.broken_phones = broken_phones
    
    def calculate_working_phones(self):
        """Calculate number of working phones"""
        return self.quantity - self.broken_phones
    
    def calculate_value_of_working_phones(self):
        """Calculate total value of working phones"""
        return self.calculate_working_phones() * self.price
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, broken={self.broken_phones})"


# Test the Phone class with 50% discount
print("Testing Phone Class with 50% Discount:")
print("=" * 80)

# Create phone instances
phone1 = Phone("iPhone14", 1000, 10, 2)
phone2 = Phone("SamsungS23", 900, 8, 1)

print("1. Created Phone instances with 50% discount rate:")
print(f"   {phone1}")
print(f"   {phone2}")

print("\n" + "=" * 80)
print("\n2. Testing class-specific discount rates:")

print(f"\n   Class pay rates:")
print(f"   Item.pay_rate = {Item.pay_rate} (20% discount)")
print(f"   Phone.pay_rate = {Phone.pay_rate} (50% discount)")

print(f"\n   Verifying Phone instances use Phone.pay_rate:")
print(f"   phone1.pay_rate = {phone1.pay_rate}")
print(f"   phone2.pay_rate = {phone2.pay_rate}")

print("\n" + "=" * 80)
print("\n3. Applying 50% discount to phones:")

print(f"\n   Before discount:")
print(f"   phone1.price = ${phone1.price}")
print(f"   phone2.price = ${phone2.price}")

print(f"\n   Applying discount:")
phone1.apply_discount()
phone2.apply_discount()

print(f"\n   After 50% discount:")
print(f"   phone1.price = ${phone1.price}")
print(f"   phone2.price = ${phone2.price}")

print("\n   Verification:")
print(f"   iPhone14: $1000 × 0.5 = ${1000 * 0.5}")
print(f"   SamsungS23: $900 × 0.5 = ${900 * 0.5}")

print("\n" + "=" * 80)
print("\n4. Testing phone-specific functionality:")

print(f"\n   Working phones calculation:")
print(f"   phone1: {phone1.quantity} total, {phone1.broken_phones} broken")
print(f"   Working phones: {phone1.calculate_working_phones()}")

print(f"\n   Value of working phones:")
print(f"   phone1: ${phone1.calculate_value_of_working_phones():.2f}")
print(f"   phone2: ${phone2.calculate_value_of_working_phones():.2f}")

print("\n" + "=" * 80)
print("\n5. Comparing with other item types:")

# Create items of different types
keyboard = Item("Keyboard", 100, 5)  # Uses Item.pay_rate (20% discount)
phone = Phone("Phone50Off", 100, 5, 1)  # Uses Phone.pay_rate (50% discount)

print("\n   Comparing discount rates:")
print(f"   Keyboard (Item): pay_rate = {keyboard.pay_rate}")
print(f"   Phone (Phone): pay_rate = {phone.pay_rate}")

print(f"\n   Original prices: $100 each")
keyboard.apply_discount()
phone.apply_discount()

print(f"\n   After respective discounts:")
print(f"   Keyboard price: ${keyboard.price} (20% discount)")
print(f"   Phone price: ${phone.price} (50% discount)")

print(f"\n   Savings comparison:")
print(f"   Keyboard saved: ${100 - keyboard.price:.2f}")
print(f"   Phone saved: ${100 - phone.price:.2f}")

print("\n" + "=" * 80)
print("\n6. Testing validation for broken phones:")

print("\n   Testing with valid broken phones count:")
try:
    valid_phone = Phone("ValidPhone", 500, 10, 3)
    print(f"   ✓ Created phone with {valid_phone.broken_phones} broken phones")
except AssertionError as e:
    print(f"   ✗ Error: {e}")

print("\n   Testing with zero broken phones:")
try:
    phone_zero = Phone("ZeroBroken", 500, 10, 0)
    print(f"   ✓ Created phone with {phone_zero.broken_phones} broken phones")
except AssertionError as e:
    print(f"   ✗ Error: {e}")

print("\n   Testing with invalid (negative) broken phones:")
try:
    invalid_phone = Phone("InvalidPhone", 500, 10, -2)
    print(f"   ✗ Unexpectedly created: {invalid_phone}")
except AssertionError as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 80)
print("\n7. Real-world scenario with 50% discount:")

print("\n   Inventory with 50% phone discount:")
phones = [
    Phone("BudgetPhone", 200, 20, 3),
    Phone("MidRangePhone", 500, 15, 2),
    Phone("PremiumPhone", 1000, 10, 1)
]

print("\n   Phone inventory before discount:")
for phone in phones:
    print(f"   {phone.name}: ${phone.price} × {phone.quantity} = ${phone.calculate_total_price():.2f}")

print("\n   Applying 50% discount to all phones:")
for phone in phones:
    original_price = phone.price
    phone.apply_discount()
    print(f"   {phone.name}: ${original_price} → ${phone.price}")

print("\n   Phone inventory after discount:")
total_value = 0
for phone in phones:
    value = phone.calculate_value_of_working_phones()
    print(f"   {phone.name}: {phone.calculate_working_phones()} working × ${phone.price} = ${value:.2f}")
    total_value += value

print(f"\n   Total value of working phones after 50% discount: ${total_value:.2f}")

print("\n" + "=" * 80)
print("\n8. Testing inheritance and method overriding:")

print("\n   Phone inherits from Item:")
print(f"   isinstance(phone1, Phone): {isinstance(phone1, Phone)}")
print(f"   isinstance(phone1, Item): {isinstance(phone1, Item)}")

print("\n   Phone can use all Item methods:")
print(f"   phone1.calculate_total_price(): ${phone1.calculate_total_price():.2f}")

print("\n   Method Resolution Order:")
for cls in Phone.__mro__:
    print(f"   → {cls.__name__}")

print("\n   Attribute lookup order:")
print(f"   phone1.pay_rate first looks in Phone class: {Phone.pay_rate}")
print(f"   If not found, looks in Item class: {Item.pay_rate}")

print("\n" + "=" * 80)
print("\nSummary:")
print("✓ Phone class overrides pay_rate = 0.5 (50% discount)")
print("✓ Phone instances get 50% discount instead of 20%")
print("✓ Broken phones validation prevents negative values")
print("✓ Phone-specific methods calculate working phones and their value")
print("✓ Inheritance allows Phone to use all Item functionality")
print("✓ Method resolution ensures Phone.pay_rate is used instead of Item.pay_rate")