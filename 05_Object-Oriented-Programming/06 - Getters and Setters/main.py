# Assuming this is a separate file that imports from the Item class defined earlier
# Let's recreate the Item class here for demonstration

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
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


# Main execution
print("Testing Item class attribute access:")
print("=" * 60)

# Create an item
item1 = Item("MyItem", 750, 1)

print("1. Created item:")
print(f"   item1 = Item('MyItem', 750, 1)")
print(f"   Result: {item1}")

print("\n2. Getting the name attribute:")
print(f"   print(item1.name)")
print(f"   Output: {item1.name}")

print("\n3. Setting the name attribute:")
print("   item1.name = 'OtherItem'")
try:
    item1.name = "OtherItem"
    print(f"   ✓ Successfully changed name to: {item1.name}")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n4. Testing with longer name:")
print("   item1.name = 'VeryLongProductName'")
try:
    item1.name = "VeryLongProductName"
    print(f"   ✗ Unexpectedly succeeded: {item1.name}")
except Exception as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n5. Testing other attribute access:")
print(f"   Getting price: item1.price = {item1.price}")
print(f"   Getting quantity: item1.quantity = {item1.quantity}")

print("\n6. Setting other attributes:")
item1.price = 800
item1.quantity = 3
print(f"   Set price to 800: item1.price = {item1.price}")
print(f"   Set quantity to 3: item1.quantity = {item1.quantity}")

print("\n7. Calculating total price:")
print(f"   item1.calculate_total_price() = {item1.calculate_total_price()}")

print("\n8. Applying discount:")
item1.apply_discount()
print(f"   After 20% discount: item1.price = {item1.price}")
print(f"   New total price: {item1.calculate_total_price()}")

print("\n" + "=" * 60)
print("\nAdvanced attribute testing:")

print("\n9. Creating multiple items:")
item2 = Item("Short", 100, 5)
item3 = Item("MediumName", 200, 2)
item4 = Item("ExactlyTen", 300, 3)

print(f"   item2: {item2}")
print(f"   item3: {item3}")
print(f"   item4: {item4}")

print("\n10. All items in system:")
print(f"   Total items: {len(Item.all)}")
for idx, item in enumerate(Item.all, 1):
    print(f"   {idx}. {item}")

print("\n" + "=" * 60)
print("\nEdge cases:")

print("\n11. Testing name with exactly 10 characters:")
test_name = "0123456789"  # 10 characters
try:
    item5 = Item(test_name, 50, 1)
    print(f"   Created item with 10-char name: {item5.name}")
    item5.name = test_name  # Try to set same name
    print(f"   ✓ Can set 10-char name")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n12. Testing name with 11 characters:")
try:
    item6 = Item("01234567890", 60, 1)  # 11 characters
    print(f"   ✗ Unexpectedly created item: {item6.name}")
except Exception as e:
    print(f"   ✓ Correctly rejected: {e}")

print("\n" + "=" * 60)
print("\nSummary:")
print("✓ Properties provide controlled access to attributes")
print("✓ Getter allows reading the name")
print("✓ Setter validates the name length (max 10 chars)")
print("✓ Other attributes (price, quantity) can be accessed directly")
print("✓ The __name attribute is private and can only be accessed via the property")