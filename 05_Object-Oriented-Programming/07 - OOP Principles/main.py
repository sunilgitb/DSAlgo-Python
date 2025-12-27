# First, let's recreate the necessary classes
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


class Phone(Item):
    pay_rate = 0.75  # 25% discount for phones
    
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken Phones {broken_phones} must be >= 0!"
        self.broken_phones = broken_phones
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, broken={self.broken_phones})"


class Keyboard(Item):
    pay_rate = 0.7  # 30% discount for keyboards
    
    def __init__(self, name: str, price: float, quantity=0):
        super().__init__(name, price, quantity)
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


# Now test the code
print("Testing Keyboard Discount Application:")
print("=" * 60)

# Create a keyboard instance
item1 = Keyboard("jscKeyboard", 1000, 3)

print("1. Created Keyboard instance:")
print(f"   item1 = Keyboard('jscKeyboard', 1000, 3)")
print(f"   Result: {item1}")

print("\n2. Before applying discount:")
print(f"   item1.price = ${item1.price}")

print("\n3. Applying discount:")
print("   item1.apply_discount()")
item1.apply_discount()

print("\n4. After applying discount:")
print(f"   item1.price = ${item1.price}")

print("\n" + "=" * 60)
print("\nDetailed Explanation:")

print("\n   Keyboard class pay_rate:")
print(f"   Keyboard.pay_rate = {Keyboard.pay_rate}")

print("\n   Item (parent) class pay_rate:")
print(f"   Item.pay_rate = {Item.pay_rate}")

print("\n   Which pay_rate is used?")
print(f"   Keyboard instance uses Keyboard.pay_rate: {item1.pay_rate}")

print("\n   Calculation:")
print(f"   Original price: $1000")
print(f"   Discount rate: 30% (pay_rate = 0.7)")
print(f"   Discounted price: $1000 × 0.7 = ${1000 * 0.7}")

print("\n" + "=" * 60)
print("\nComparison with other item types:")

# Create different item types for comparison
keyboard = Keyboard("MyKeyboard", 1000, 1)
phone = Phone("MyPhone", 1000, 1, 0)
item = Item("MyItem", 1000, 1)

print("\n   Different items with same original price ($1000):")
print(f"   Keyboard: {keyboard}")
print(f"   Phone: {phone}")
print(f"   Item: {item}")

print("\n   Applying discounts:")
keyboard.apply_discount()
phone.apply_discount()
item.apply_discount()

print(f"\n   After discounts:")
print(f"   Keyboard price: ${keyboard.price} (30% discount)")
print(f"   Phone price: ${phone.price} (25% discount)")
print(f"   Item price: ${item.price} (20% discount)")

print("\n   Discount amounts:")
print(f"   Keyboard saved: ${1000 - keyboard.price:.2f}")
print(f"   Phone saved: ${1000 - phone.price:.2f}")
print(f"   Item saved: ${1000 - item.price:.2f}")

print("\n" + "=" * 60)
print("\nTesting the actual output from the provided code:")
print("-" * 60)

# Simulate exactly what the provided code does
item1 = Keyboard("jscKeyboard", 1000, 3)
item1.apply_discount()
print(item1.price)  # This should print 700.0

print("\n" + "=" * 60)
print("\nExplanation of the result:")
print("1. Keyboard class has pay_rate = 0.7 (30% discount)")
print("2. When apply_discount() is called on a Keyboard instance,")
print("   it uses Keyboard.pay_rate = 0.7")
print("3. Calculation: $1000 × 0.7 = $700")
print(f"4. Output: {item1.price}")

print("\n" + "=" * 60)
print("\nVerification:")
print(f"Keyboard instance pay_rate: {Keyboard.pay_rate}")
print(f"item1.pay_rate: {item1.pay_rate}")
print(f"1000 * {item1.pay_rate} = {1000 * item1.pay_rate}")
print(f"Actual item1.price: {item1.price}")

print("\n✓ The output is correct! Keyboard gets a 30% discount.")