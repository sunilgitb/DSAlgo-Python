# 03. Nearest Smaller to Left (or Previous Smaller Element)
# Given an array, find for each element the nearest smaller element to its left.
# If no smaller element exists on the left, return -1.
# Optimal solution using Stack (Monotonic Stack)

def nearest_smaller_to_left(arr):
    """
    Returns a list where ans[i] = nearest smaller element to the left of arr[i],
    or -1 if none exists.
    
    Time Complexity: O(n) - each element pushed/popped at most once
    Space Complexity: O(n)
    """
    n = len(arr)
    ans = [-1] * n
    stack = []  # will store elements in increasing order (from left to right)
    
    # Traverse from left to right
    for i in range(n):
        # Pop elements that are greater than or equal to current element
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        
        # If stack is not empty, top is the nearest smaller to the left
        if stack:
            ans[i] = stack[-1]
        
        # Push current element onto the stack
        stack.append(arr[i])
    
    return ans


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Basic cases
        ([1, 3, 2, 4], [-1, 1, 1, 2]),
        ([4, 5, 2, 25], [-1, 4, -1, 2]),
        ([13, 7, 6, 12], [-1, -1, -1, 6]),
        
        # All increasing
        ([1, 2, 3, 4, 5], [-1, 1, 2, 3, 4]),
        
        # All decreasing
        ([5, 4, 3, 2, 1], [-1, -1, -1, -1, -1]),
        
        # Duplicates
        ([1, 3, 3, 2, 5, 3], [-1, 1, 1, 1, 2, 2]),
        
        # Single element
        ([10], [-1]),
        
        # Empty array
        ([], []),
        
        # All same elements
        ([7, 7, 7, 7], [-1, -1, -1, -1]),
        
        # Mixed with large numbers
        ([11, 13, 21, 3], [-1, 11, 13, -1]),
    ]
    
    print("Testing Nearest Smaller to Left\n" + "="*40)
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        result = nearest_smaller_to_left(arr)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Input: {arr}")
        print(f"   Output: {result}")
        print(f" Expected: {expected}")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()