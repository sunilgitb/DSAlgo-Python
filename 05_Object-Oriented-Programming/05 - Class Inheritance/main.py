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
    
    def calculate_working_phones(self):
        return self.quantity - self.broken_phones
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, broken={self.broken_phones})"


class Laptop(Item):
    def __init__(self, name: str, price: float, quantity=0, ram=8, storage=256):
        super().__init__(name, price, quantity)
        
        self.ram = ram
        self.storage = storage
    
    def get_specs(self):
        return f"{self.ram}GB RAM, {self.storage}GB SSD"
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.ram}GB/{self.storage}GB)"


# Test the classes
print("Testing Inheritance and Polymorphism:")
print("=" * 80)

# Create some items
phone1 = Phone("iPhone13", 999, 10, 2)
phone2 = Phone("SamsungS22", 899, 8, 1)
laptop1 = Laptop("MacBook Pro", 1999, 5, 16, 512)
laptop2 = Laptop("Dell XPS", 1499, 7, 8, 256)
item1 = Item("Generic Tablet", 299, 15)

print("Created items:")
print(f"  {phone1}")
print(f"  {phone2}")
print(f"  {laptop1}")
print(f"  {laptop2}")
print(f"  {item1}")

print("\n" + "=" * 80)
print("\nTesting Phone-specific methods:")
print(f"Phone: {phone1.name}")
print(f"  Total phones: {phone1.quantity}")
print(f"  Broken phones: {phone1.broken_phones}")
print(f"  Working phones: {phone1.calculate_working_phones()}")
print(f"  Total value of working phones: ${phone1.calculate_working_phones() * phone1.price:.2f}")

print(f"\nPhone: {phone2.name}")
print(f"  Total phones: {phone2.quantity}")
print(f"  Broken phones: {phone2.broken_phones}")
print(f"  Working phones: {phone2.calculate_working_phones()}")

print("\n" + "=" * 80)
print("\nTesting Laptop-specific methods:")
print(f"Laptop: {laptop1.name}")
print(f"  Specifications: {laptop1.get_specs()}")
print(f"  Total value: ${laptop1.calculate_total_price():.2f}")

print(f"\nLaptop: {laptop2.name}")
print(f"  Specifications: {laptop2.get_specs()}")
print(f"  Total value: ${laptop2.calculate_total_price():.2f}")

print("\n" + "=" * 80)
print("\nAll items in Item.all:")
print(f"Total items: {len(Item.all)}")
print("\nList of all items:")
for idx, item in enumerate(Item.all, 1):
    print(f"  {idx}. {item}")

print("\n" + "=" * 80)
print("\nTesting Polymorphism - All items can use Item methods:")

print("\nCalculating total prices for all items:")
for item in Item.all:
    print(f"  {item.name}: ${item.calculate_total_price():.2f}")

print("\nApplying 20% discount to all items:")
for item in Item.all:
    original_price = item.price
    item.apply_discount()
    print(f"  {item.name}: ${original_price:.2f} → ${item.price:.2f}")

print("\n" + "=" * 80)
print("\nTesting class and static methods:")

print("\nChecking if numbers are integers:")
test_numbers = [5, 5.0, 5.5, "5"]
for num in test_numbers:
    print(f"  Item.is_integer({repr(num)}): {Item.is_integer(num)}")

# Clear items and load from CSV
print("\n" + "=" * 80)
print("\nInstantiating items from CSV:")
Item.all = []  # Clear existing items
Item.instantiate_from_csv()

print(f"\nItems loaded from CSV: {len(Item.all)}")
for item in Item.all:
    print(f"  {item}")

print("\n" + "=" * 80)
print("\nSummary:")
total_value = sum(item.calculate_total_price() for item in Item.all)
total_items = sum(item.quantity for item in Item.all)
print(f"Total inventory value: ${total_value:.2f}")
print(f"Total number of items in stock: {total_items}")
print(f"Number of different products: {len(Item.all)}")