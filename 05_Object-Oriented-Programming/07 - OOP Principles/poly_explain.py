name = "Jim"  # str
print(f"len('{name}') = {len(name)}")

some_list = ["some", "name"]  # list
print(f"len({some_list}) = {len(some_list)}")

print("\n" + "=" * 60)
print("Demonstrating Polymorphism in Python:")
print("=" * 60)

# More examples of polymorphism with len()
print("\n1. The len() function works with different data types:")

# String
string_example = "Hello World"
print(f"   String: '{string_example}'")
print(f"   len(string): {len(string_example)} characters")

# List
list_example = [1, 2, 3, 4, 5]
print(f"\n   List: {list_example}")
print(f"   len(list): {len(list_example)} elements")

# Tuple
tuple_example = (10, 20, 30, 40)
print(f"\n   Tuple: {tuple_example}")
print(f"   len(tuple): {len(tuple_example)} elements")

# Dictionary
dict_example = {"a": 1, "b": 2, "c": 3}
print(f"\n   Dictionary: {dict_example}")
print(f"   len(dict): {len(dict_example)} key-value pairs")

# Set
set_example = {1, 2, 3, 4, 5, 5}  # Note: duplicates are removed
print(f"\n   Set: {set_example}")
print(f"   len(set): {len(set_example)} unique elements")

print("\n" + "=" * 60)
print("\n2. More polymorphism examples with print():")

print("\n   print() works with different data types:")
print(f"   String: {'Python'}")
print(f"   Integer: {42}")
print(f"   Float: {3.14159}")
print(f"   Boolean: {True}")
print(f"   List: {[1, 2, 3]}")
print(f"   None: {None}")

print("\n" + "=" * 60)
print("\n3. Custom classes with polymorphism:")

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"Book: {self.title}"

class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
    
    def __len__(self):
        return len(self.courses)
    
    def __str__(self):
        return f"Student: {self.name}"

print("\n   Custom objects with __len__ method:")
book1 = Book("Python Programming", 350)
student1 = Student("Alice", ["Math", "Science", "History"])

print(f"   {book1}")
print(f"   len(book1): {len(book1)} pages")

print(f"\n   {student1}")
print(f"   len(student1): {len(student1)} courses")

print("\n" + "=" * 60)
print("\n4. Polymorphism with arithmetic operators:")

print("\n   The + operator works differently with different types:")
print(f"   Numbers: 5 + 3 = {5 + 3}")
print(f"   Strings: 'Hello' + ' ' + 'World' = {'Hello' + ' ' + 'World'}")
print(f"   Lists: [1, 2] + [3, 4] = {[1, 2] + [3, 4]}")

print("\n" + "=" * 60)
print("\n5. Polymorphism with iteration:")

print("\n   for loop works with different iterables:")

print("\n   Iterating over a string:")
for char in "Python":
    print(f"     {char}", end=" ")

print("\n\n   Iterating over a list:")
for item in ["apple", "banana", "cherry"]:
    print(f"     {item}", end=" ")

print("\n\n   Iterating over a dictionary:")
for key in {"x": 1, "y": 2, "z": 3}:
    print(f"     {key}", end=" ")

print("\n" + "=" * 60)
print("\n6. Polymorphism with custom iterable classes:")

class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

print("\n   Custom CountDown class is iterable:")
print("   for num in CountDown(5):")
for num in CountDown(5):
    print(f"     {num}")

print("\n" + "=" * 60)
print("\n7. Polymorphism in real-world scenarios:")

print("\n   File I/O - same open() function works with different modes:")
try:
    # Write to a file
    with open("test.txt", "w") as f:
        f.write("Hello World")
    print("   ✓ Wrote to file with 'w' mode")
    
    # Read from a file
    with open("test.txt", "r") as f:
        content = f.read()
    print(f"   ✓ Read from file with 'r' mode: '{content}'")
    
    # Append to a file
    with open("test.txt", "a") as f:
        f.write("\nAppended text")
    print("   ✓ Appended to file with 'a' mode")
    
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "=" * 60)
print("\n8. Polymorphism with type checking:")

print("\n   isinstance() allows checking multiple types:")

data = [42, "hello", 3.14, [1, 2, 3], {"key": "value"}]

for item in data:
    if isinstance(item, (int, float)):
        print(f"   {item} is a number")
    elif isinstance(item, str):
        print(f"   '{item}' is a string")
    elif isinstance(item, list):
        print(f"   {item} is a list")
    elif isinstance(item, dict):
        print(f"   {item} is a dictionary")

print("\n" + "=" * 60)
print("\nSummary of Polymorphism:")
print("• len() works with strings, lists, tuples, dictionaries, sets")
print("• print() works with all data types")
print("• + operator works with numbers, strings, lists")
print("• for loop works with all iterables")
print("• Custom classes can implement __len__, __iter__, etc.")
print("• Functions adapt behavior based on object type")
print("• Makes code more flexible and reusable")
print("• Core principle of object-oriented programming")