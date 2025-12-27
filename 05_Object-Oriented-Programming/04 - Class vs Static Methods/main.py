import csv

class Item:
    pay_rate = 0.8  # 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} must be >= 0!"
        assert quantity >= 0, f"Quantity {quantity} must be >= 0!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
    
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
            # Create sample CSV data
            sample_data = [
                {"name": "Phone", "price": "1000", "quantity": "3"},
                {"name": "Laptop", "price": "1500", "quantity": "2"},
                {"name": "Tablet", "price": "500", "quantity": "5"},
                {"name": "Monitor", "price": "300", "quantity": "8"},
                {"name": "Keyboard", "price": "50", "quantity": "10"}
            ]
            
            # Write sample data to CSV
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
                writer.writeheader()
                writer.writerows(sample_data)
            
            # Now instantiate from the created file
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
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# Test the Item class
print("Testing Item Class:")
print("=" * 60)

# Create some items
item1 = Item("Phone", 1000, 3)
item2 = Item("Laptop", 1500, 2)
item3 = Item("Tablet", 500, 5)

print("1. Individual Items:")
print(f"   {item1}")
print(f"   {item2}")
print(f"   {item3}")

print("\n2. Calculate Total Prices:")
print(f"   {item1.name} total: ${item1.calculate_total_price()}")
print(f"   {item2.name} total: ${item2.calculate_total_price()}")
print(f"   {item3.name} total: ${item3.calculate_total_price()}")

print("\n3. Apply Discount (20% off):")
print(f"   {item1.name} before discount: ${item1.price}")
item1.apply_discount()
print(f"   {item1.name} after discount: ${item1.price}")

print("\n4. Test is_integer static method:")
print(f"   Item.is_integer(5): {Item.is_integer(5)}")
print(f"   Item.is_integer(5.0): {Item.is_integer(5.0)}")
print(f"   Item.is_integer(5.5): {Item.is_integer(5.5)}")
print(f"   Item.is_integer('5'): {Item.is_integer('5')}")

print("\n5. Instantiate from CSV:")
# Clear existing items
Item.all = []
Item.instantiate_from_csv()

print(f"   Total items created from CSV: {len(Item.all)}")
print("\n   Items from CSV:")
for item in Item.all:
    print(f"   - {item.name}: ${item.price} x {item.quantity} = ${item.calculate_total_price()}")

print("\n6. All items in the system:")
for idx, item in enumerate(Item.all, 1):
    print(f"   {idx}. {item}")

print("\n7. Test validation (should raise AssertionError):")
try:
    invalid_item = Item("Invalid", -100, 5)
except AssertionError as e:
    print(f"   ✓ Correctly raised error: {e}")

try:
    invalid_item = Item("Invalid", 100, -5)
except AssertionError as e:
    print(f"   ✓ Correctly raised error: {e}")

print("\n" + "=" * 60)
print("Summary:")
print(f"Pay rate (discount): {Item.pay_rate}")
print(f"Total items in system: {len(Item.all)}")
total_value = sum(item.calculate_total_price() for item in Item.all)
print(f"Total inventory value: ${total_value}")