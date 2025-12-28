# 02. Nearest Greater to Left (or Previous Greater Element)
# Given an array, find for each element the nearest greater element to its left.
# If no greater element exists on the left, return -1.
# Optimal solution using Stack (Monotonic Stack)

def nearest_greater_to_left(arr):
    """
    Returns a list where ans[i] = nearest greater element to the left of arr[i],
    or -1 if none exists.
    
    Time Complexity: O(n) - each element pushed/popped at most once
    Space Complexity: O(n)
    """
    n = len(arr)
    ans = [-1] * n
    stack = []  # will store elements in decreasing order (from left to right)
    
    # Traverse from left to right
    for i in range(n):
        # Pop elements that are smaller than or equal to current element
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        # If stack is not empty, top is the nearest greater to the left
        if stack:
            ans[i] = stack[-1]
        
        # Push current element onto the stack
        stack.append(arr[i])
    
    return ans


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Basic cases
        ([1, 3, 2, 4], [-1, -1, 3, 3]),
        ([4, 5, 2, 25], [-1, -1, 5, -1]),
        ([13, 7, 6, 12], [-1, 13, 13, 13]),
        
        # All increasing
        ([1, 2, 3, 4, 5], [-1, -1, -1, -1, -1]),
        
        # All decreasing
        ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5]),
        
        # Duplicates
        ([1, 3, 3, 2, 5, 3], [-1, -1, -1, 3, -1, 5]),
        
        # Single element
        ([10], [-1]),
        
        # Empty array
        ([], []),
        
        # All same elements
        ([7, 7, 7, 7], [-1, -1, -1, -1]),
        
        # Mixed with large numbers
        ([11, 13, 21, 3], [-1, -1, -1, 21]),
    ]
    
    print("Testing Nearest Greater to Left\n" + "="*40)
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        result = nearest_greater_to_left(arr)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Input: {arr}")
        print(f"   Output: {result}")
        print(f" Expected: {expected}")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()