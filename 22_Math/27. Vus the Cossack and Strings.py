'''
https://codeforces.com/problemset/problem/1186/C
 
Solution: This question requires some effort to delve into and find a pattern. Lets take examples
of b and a's sub-array of equal length as a_arr and calculate f():

A)
b = 00110 and a_arr = 00111:

00110
00111

Ans: 1

B)
b = 00110 and a_arr = 01100:

00110
01100

Ans: 2

C)
b = 00010 and a_arr = 01110:

00010
01110

Ans: 2

D)
b = 00110 and a_arr = 00010:

00110
00010

Ans: 1

If you observe these examples, in cases where the count of 1s was same in b and a_arr, we ended up
having the answer even. This comes from the fact that same parity of count of 1s makes the resulting answer
to be always even. Odd +(or -) Odd is even and Even +(or -) Even is even. Therefore irrespective of 
which bits match, in such cases, the value of f() would always be even and that is what we
need to calculate in this question. 

Therefore, we calculate this observation in b and the first sub-array of a of length of b. Then
we slide the window of that length over a and compute it over subsequent sub-arrays of a. A counter
of same parity of these observations on b and a_arr is calculated and is the final answer. 

~ Tidbit ~
Checking parity between collections of bits is optimal via XOR operator rather than counting 
the occurrences and then using MODULO over 2. XOR alternates between 0 and 1 as we keep
operating it against 1, thereby denoting if the value is even or odd respectively. 

'''

# https://codeforces.com/problemset/problem/1186/C
# Flag of Many Colors (or XOR-based parity counting)

def count_matching_parity_windows(a: str, b: str) -> int:
    """
    Given two binary strings a and b,
    count the number of contiguous subarrays in a of length len(b)
    that have the same parity of 1's as b (i.e., same XOR of all bits).

    Time: O(n)
    Space: O(1)
    """
    n = len(a)
    m = len(b)
    
    if m > n:
        return 0
    
    # Compute XOR (parity) of b
    xor_b = 0
    for char in b:
        xor_b ^= int(char)
    
    # Compute initial XOR for a[0..m-1]
    xor_window = 0
    for i in range(m):
        xor_window ^= int(a[i])
    
    count = 0
    if xor_window == xor_b:
        count += 1
    
    # Slide the window
    for i in range(m, n):
        # Remove a[i-m] and add a[i]
        xor_window ^= int(a[i - m])
        xor_window ^= int(a[i])
        
        if xor_window == xor_b:
            count += 1
    
    return count


# Driver code with test cases (no input required)
if __name__ == "__main__":
    test_cases = [
        # Sample Input 1
        ("101010", "110", 3),      # Expected: 3
        
        # Sample Input 2
        ("00110011", "1010", 2),
        
        # Small examples
        ("111", "1", 3),
        ("000", "1", 0),
        ("101", "10", 2),
        ("1", "1", 1),
        ("", "1", 0),
        
        # Long string
        ("101010101010", "1010", 5),
    ]
    
    print("Testing Count Matching Parity Windows\n" + "="*50)
    
    for idx, (a, b, expected) in enumerate(test_cases, 1):
        result = count_matching_parity_windows(a, b)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   a = '{a}'")
        print(f"   b = '{b}'")
        print(f"   Output: {result} (Expected: {expected})")
        print("-" * 50)