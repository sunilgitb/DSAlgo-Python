"""
File: 03. Greatest Common Divisor.py
Topic: GCD / HCF
"""

# ------------------------------------------------------------
# GCD (Greatest Common Divisor) / HCF (Highest Common Factor)
# ------------------------------------------------------------
# Euclidean Algorithm (Optimal & Interview Preferred)
# Time Complexity: O(log(max(a, b)))
# Space Complexity: O(log(max(a, b))) due to recursion
# ------------------------------------------------------------

def gcd(a: int, b: int) -> int:
    """Return GCD of two numbers using Euclidean Algorithm"""
    if b == 0:
        return a
    return gcd(b, a % b)


# ------------------------------------------------------------
# Iterative Version (No Recursion)
# Time Complexity: O(log(max(a, b)))
# Space Complexity: O(1)
# ------------------------------------------------------------

def gcd_iterative(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        (98, 56),
        (18, 24),
        (7, 3),
        (100, 10),
        (0, 5),
        (5, 0)
    ]

    print("Using Recursive GCD:")
    for a, b in test_cases:
        print(f"GCD({a}, {b}) = {gcd(a, b)}")

    print("\nUsing Iterative GCD:")
    for a, b in test_cases:
        print(f"GCD({a}, {b}) = {gcd_iterative(a, b)}")


"""
Output:
Using Recursive GCD:
GCD(98, 56) = 14
GCD(18, 24) = 6
GCD(7, 3) = 1
GCD(100, 10) = 10
GCD(0, 5) = 5
GCD(5, 0) = 5

Using Iterative GCD:
GCD(98, 56) = 14
GCD(18, 24) = 6
GCD(7, 3) = 1
GCD(100, 10) = 10
GCD(0, 5) = 5
GCD(5, 0) = 5
"""
