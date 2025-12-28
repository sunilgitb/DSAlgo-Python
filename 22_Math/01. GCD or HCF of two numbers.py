# https://www.geeksforgeeks.org/c-program-find-gcd-hcf-two-numbers/
'''
GCD (Greatest Common Divisor) or HCF (Highest Common Factor)
of two numbers is the largest number that divides both of them. 
'''
# Euclidean Algorithm: GCD of two numbers doesn’t change if smaller number is subtracted from a bigger number. 
# https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

# --------------------------------------------------------------------------------------------------
"""
GCD (Greatest Common Divisor) / HCF (Highest Common Factor)
The largest number that divides both numbers.
"""

# ---------------------------------------------------------------------
# 1️⃣ Brute Force Approach
# ---------------------------------------------------------------------
def gcd_bruteforce(a, b):
    result = min(a, b)
    while result > 0:
        if a % result == 0 and b % result == 0:
            return result
        result -= 1


# Driver Code
a, b = 98, 56
print("Brute Force GCD:", gcd_bruteforce(a, b))
# Output: 14


# ---------------------------------------------------------------------
# 2️⃣ Euclidean Algorithm (Recursive – Subtraction)
# ---------------------------------------------------------------------
def gcd_subtraction(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd_subtraction(a - b, b)
    return gcd_subtraction(a, b - a)


# Driver Code
print("Euclidean (Subtraction) GCD:", gcd_subtraction(a, b))
# Output: 14

# Time Complexity: O(max(a, b))
# Space Complexity: O(max(a, b))


# ---------------------------------------------------------------------
# 3️⃣ Dynamic Programming (Memoization)
# ---------------------------------------------------------------------
MAX = 1000
dp = [[-1 for _ in range(MAX + 1)] for _ in range(MAX + 1)]

def gcd_dp(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if dp[a][b] != -1:
        return dp[a][b]
    if a > b:
        dp[a][b] = gcd_dp(a - b, b)
    else:
        dp[a][b] = gcd_dp(a, b - a)
    return dp[a][b]


# Driver Code
print("DP (Memoization) GCD:", gcd_dp(a, b))
# Output: 14

# Time Complexity: O(max(a, b))
# Space Complexity: O(max(a, b))


# ---------------------------------------------------------------------
# 4️⃣ Optimized Euclidean Algorithm (Modulo) ⭐ BEST
# ---------------------------------------------------------------------
def gcd_modulo(a, b):
    if b == 0:
        return a
    return gcd_modulo(b, a % b)


# Driver Code
print("Euclidean (Modulo) GCD:", gcd_modulo(a, b))
# Output: 14

# Time Complexity: O(log(max(a, b)))
# Space Complexity: O(log(max(a, b)))
