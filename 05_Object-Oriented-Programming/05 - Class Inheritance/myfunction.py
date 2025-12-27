def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


# Test the functions
print("Testing add and multiply functions:")
print("=" * 40)

# Test cases for add function
print("\n1. Testing add function:")
test_cases_add = [
    (2, 3, 5),        # Positive numbers
    (-2, 3, 1),       # Negative and positive
    (0, 5, 5),        # Zero and positive
    (-5, -5, -10),    # Negative numbers
    (2.5, 3.5, 6.0),  # Floating point numbers
    (0, 0, 0),        # Both zeros
]

for a, b, expected in test_cases_add:
    result = add(a, b)
    status = "✓" if result == expected else "✗"
    print(f"  add({a}, {b}) = {result} (expected: {expected}) {status}")

# Test cases for multiply function
print("\n2. Testing multiply function:")
test_cases_multiply = [
    (2, 3, 6),         # Positive numbers
    (-2, 3, -6),       # Negative and positive
    (0, 5, 0),         # Zero multiplication
    (-5, -5, 25),      # Negative numbers
    (2.5, 4, 10.0),    # Floating point
    (1, 10, 10),       # Multiplication by 1
]

for a, b, expected in test_cases_multiply:
    result = multiply(a, b)
    status = "✓" if result == expected else "✗"
    print(f"  multiply({a}, {b}) = {result} (expected: {expected}) {status}")

print("\n" + "=" * 40)

# Combining both functions
print("\n3. Combining both functions:")
print("  Example 1: add(2, 3) * multiply(4, 5)")
result1 = add(2, 3) * multiply(4, 5)
print(f"    = {add(2, 3)} * {multiply(4, 5)} = {result1}")

print("\n  Example 2: multiply(add(10, 5), 2)")
result2 = multiply(add(10, 5), 2)
print(f"    = multiply({add(10, 5)}, 2) = {result2}")

print("\n  Example 3: add(multiply(3, 4), multiply(5, 6))")
result3 = add(multiply(3, 4), multiply(5, 6))
print(f"    = add({multiply(3, 4)}, {multiply(5, 6)}) = {result3}")

print("\n" + "=" * 40)

# Testing with different data types
print("\n4. Testing with different scenarios:")
print("  add('Hello', ' World') = ", end="")
try:
    result = add("Hello", " World")
    print(f"'{result}' ✓")
except TypeError as e:
    print(f"Error: {e}")

print("  multiply('Hi', 3) = ", end="")
try:
    result = multiply("Hi", 3)
    print(f"'{result}' ✓")
except TypeError as e:
    print(f"Error: {e}")

print("\n5. Using in mathematical expressions:")
a, b, c, d = 5, 10, 3, 7
expression_result = multiply(add(a, b), add(c, d))
print(f"  multiply(add({a}, {b}), add({c}, {d}))")
print(f"  = multiply({add(a, b)}, {add(c, d)})")
print(f"  = {expression_result}")

print("\n" + "=" * 40)
print("All tests completed!")