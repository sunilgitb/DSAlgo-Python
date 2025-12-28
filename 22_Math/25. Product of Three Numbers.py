'''
https://codeforces.com/problemset/problem/1294/C
 
Solution: We first find the factor for n using a standard sqrt time complexity stub. If we could 
find one, that becomes a. And then we find factor for n/a which is not equal to a. If we could
find one, that becomes b. By then, the value of n is made (n/a)/b or n/ab. Hence if that value of
n is not equal to a,b or 1 then it is c. We add it to the distinct factor's set and return the result.
At any step if we fail, the answer returned is NO. 
'''


# https://codeforces.com/problemset/problem/1294/C
# Product of Three Numbers
# Problem: Given n, find three distinct positive integers a, b, c
# such that a * b * c = n, or determine that it's impossible.

def find_factor(n, used):
    """
    Find the smallest factor of n that is not in used.
    Returns (True, factor) if found, (False, None) otherwise.
    """
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and i not in used:
            return True, i
    return False, None


def solve(n):
    """
    Try to factorize n into three distinct integers > 1.
    Returns "YES" followed by the three numbers if possible, else "NO".
    """
    if n < 8:
        return "NO"
    
    used = set()
    
    # Find first factor a
    done, a = find_factor(n, used)
    if not done:
        return "NO"
    used.add(a)
    n //= a
    
    # Find second factor b
    done, b = find_factor(n, used)
    if not done:
        # If b not found, try to use a as one factor and find another
        # But since a was smallest, if no other factor exists, impossible
        return "NO"
    used.add(b)
    n //= b
    
    # Now n should be the third factor c
    c = n
    if c in used or c == 1:
        return "NO"
    
    return f"YES\n{a} {b} {c}"


# Driver Code with multiple test cases (no input needed)
if __name__ == "__main__":
    test_cases = [
        8,      # YES 2 2 2 → but must be distinct → NO
        30,     # YES 2 3 5
        123,    # YES 3 41 1 → NO (1 invalid)
        100,    # YES 2 2 25 → NO (not distinct)
        999,    # YES 3 3 111 → NO
        1234,   # YES 2 617 1 → NO
        123456, # YES 2 3 20576 (example)
        1,      # NO
        2,      # NO
        6,      # YES 1 2 3 → NO (1 invalid)
        12,     # YES 2 2 3 → NO (not distinct)
        60,     # YES 2 3 10
    ]
    
    print("Testing Product of Three Numbers\n" + "="*50)
    
    for idx, n in enumerate(test_cases, 1):
        result = solve(n)
        print(f"Test {idx:2d}: n = {n}")
        print(f"   Output: {result}")
        print("-" * 50)