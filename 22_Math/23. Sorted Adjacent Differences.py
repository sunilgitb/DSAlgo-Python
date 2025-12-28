# https://codeforces.com/problemset/problem/1339/B

'''Solution: 
Sort the array. Keep 2 pointers left and right. Take the pair of elements of these pointed elements
in the result array. Move the left leftwards and right rightwards. This ensures the net distance on the 
number line is smallest, thereby agreeing to the constraint of absolute differences of pair elements.

For odd length arrays, we keep the middle element as the first element in the result array since it cannot
be paired. And then we start from the pointers movement as mentioned above.  
'''


# https://codeforces.com/problemset/problem/1339/B
# Sorted Adjacent Differences

def solve(arr):
    """
    Rearrange array such that absolute difference between adjacent elements is minimized.
    Returns the rearranged array.
    """
    n = len(arr)
    arr.sort()  # Sort the array first
    
    res = [0] * n
    
    if n % 2 == 0:
        left = n // 2 - 1
        right = n // 2
        i = 0
    else:
        left = n // 2 - 1
        right = n // 2 + 1
        res[0] = arr[n // 2]
        i = 1
    
    while left >= 0 and right < n:
        res[i] = arr[left]
        left -= 1
        i += 1
        
        res[i] = arr[right]
        right += 1
        i += 1
    
    return res


# Driver code with test cases (no input required)
if __name__ == "__main__":
    test_cases = [
        # Sample Input 1
        [4, 2, 4, 1, 3],
        
        # Sample Input 2
        [5, 1, 3, 5, 2, 4],
        
        # Odd length
        [1, 5, 3, 7, 2],
        
        # All same
        [10, 10, 10, 10],
        
        # Single element
        [7],
        
        # Increasing sequence
        [1, 2, 3, 4, 5, 6],
    ]
    
    print("Testing Sorted Adjacent Differences\n" + "="*50)
    
    for idx, arr in enumerate(test_cases, 1):
        original = arr[:]
        result = solve(arr)
        print(f"Test {idx}:")
        print(f"   Original: {original}")
        print(f"   Result:   {result}")
        print("-" * 50)