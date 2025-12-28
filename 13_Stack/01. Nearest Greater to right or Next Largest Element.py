# Nearest Greater to Right / Next Greater Element to the Right
# Problem: For each element in the array, find the first greater element to its right.
# If no greater element exists, return -1.
# Optimal approach: Monotonic Stack (from right to left)

def nearest_greater_to_right(arr):
    """
    Returns a list where result[i] = next greater element to the right of arr[i],
    or -1 if none exists.
    
    Time Complexity: O(n) - each element is pushed and popped at most once
    Space Complexity: O(n)
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # stores elements in decreasing order (from right to left)
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Remove elements smaller than or equal to current
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        # If stack is not empty, top is the next greater
        if stack:
            result[i] = stack[-1]
        
        # Push current element
        stack.append(arr[i])
    
    return result


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Basic cases
        ([1, 3, 2, 4], [3, 4, 4, -1]),
        ([4, 5, 2, 25], [5, 25, 25, -1]),
        ([13, 7, 6, 12], [-1, 12, 12, -1]),
        
        # All increasing
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, -1]),
        
        # All decreasing
        ([5, 4, 3, 2, 1], [-1, -1, -1, -1, -1]),
        
        # Duplicates
        ([1, 3, 3, 2, 5, 3], [3, 5, 5, 5, -1, -1]),
        
        # Single element
        ([10], [-1]),
        
        # Empty array
        ([], []),
        
        # All same elements
        ([7, 7, 7, 7], [-1, -1, -1, -1]),
        
        # Mixed with large numbers
        ([11, 13, 21, 3], [13, 21, -1, -1]),
    ]
    
    print("Testing Nearest Greater to Right\n" + "="*40)
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        result = nearest_greater_to_right(arr)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Input: {arr}")
        print(f"   Output: {result}")
        print(f" Expected: {expected}")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()