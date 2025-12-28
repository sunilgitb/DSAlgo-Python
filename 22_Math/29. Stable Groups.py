# https://codeforces.com/problemset/problem/1539/C

# https://codeforces.com/problemset/problem/1539/C
# Stable Groups

def solve(n: int, k: int, x: int, arr: list[int]) -> int:
    """
    Calculate the minimum number of stable groups after at most k operations.
    
    Approach:
    - Sort the array
    - Compute differences between consecutive elements
    - Large gaps (diff > x) require operations to connect
    - Each operation can reduce a gap by x
    - Greedily use operations on smallest gaps first
    """
    if n <= 1:
        return n
    
    # Sort array
    arr.sort()
    
    # Compute differences > x
    gaps = []
    for i in range(1, n):
        diff = arr[i] - arr[i - 1]
        if diff > x:
            gaps.append(diff)
    
    # If no large gaps → already 1 group
    if not gaps:
        return 1
    
    # Sort gaps ascending (greedy: fix smallest gaps first)
    gaps.sort()
    
    groups = len(gaps) + 1  # initial number of groups
    
    for gap in gaps:
        # Number of operations needed to connect this gap
        ops_needed = (gap - 1) // x
        
        if ops_needed <= k:
            k -= ops_needed
            groups -= 1
        else:
            # Cannot connect this gap
            break
    
    return groups


# Driver code with multiple test cases (no input required)
if __name__ == "__main__":
    test_cases = [
        # Sample Input 1
        (5, 2, 3, [1, 2, 4, 8, 9]),  # Expected: 2
        
        # Sample Input 2
        (5, 3, 10, [1, 11, 21, 31, 41]),  # Expected: 2
        
        # All close
        (4, 1, 5, [1, 2, 3, 4]),  # Expected: 1
        
        # All far apart
        (5, 1, 1, [1, 3, 5, 7, 9]),  # Expected: 4
        
        # Single element
        (1, 10, 5, [100]),  # Expected: 1
        
        # Large k
        (6, 100, 2, [1, 5, 9, 13, 17, 21]),  # Expected: 1
        
        # Mixed
        (7, 3, 4, [1, 2, 6, 10, 15, 19, 23]),  # Expected: 3
    ]
    
    print("Testing Stable Groups\n" + "="*50)
    
    for idx, (n, k, x, arr) in enumerate(test_cases, 1):
        result = solve(n, k, x, arr[:])
        print(f"Test {idx:2d}:")
        print(f"   n = {n}, k = {k}, x = {x}")
        print(f"   arr = {arr}")
        print(f"   Output: {result}")
        print("-" * 50)
