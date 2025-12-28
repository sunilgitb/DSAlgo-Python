# 08. Trapping Rain Water
# Problem: Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water it can trap after raining.

# Optimal solution using Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def trap(height):
    """
    Returns the total amount of water that can be trapped.
    
    Approach: Use a stack to keep track of indices of bars in decreasing order.
    When we find a bar taller than the top of the stack, we calculate trapped water.
    """
    if not height:
        return 0
    
    n = len(height)
    stack = []  # stores indices
    total_water = 0
    
    for i in range(n):
        # While stack is not empty and current bar is taller than the bar at stack top
        while stack and height[stack[-1]] < height[i]:
            top = stack.pop()  # the bar that will trap water
            
            # If stack is empty after pop, no left boundary → no water trapped
            if not stack:
                break
            
            # Left boundary
            left = stack[-1]
            
            # Width of the water trapped
            width = i - left - 1
            
            # Height of water = min(left boundary height, right boundary height) - height of current bar
            bounded_height = min(height[left], height[i]) - height[top]
            
            # Add trapped water
            total_water += width * bounded_height
        
        # Push current index to stack
        stack.append(i)
    
    return total_water


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Standard examples
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
        
        # No water trapped
        ([1,2,3,4,5], 0),
        ([5,4,3,2,1], 0),
        
        # All same height
        ([3,3,3,3,3], 0),
        
        # Single bar or empty
        ([], 0),
        ([10], 0),
        
        # Large trap
        ([0,1,0,2,1,0,3,1,0,1,2], 8),
        
        # Another classic
        ([5,3,7,7], 1),
    ]
    
    print("Testing Trapping Rain Water (Monotonic Stack)\n" + "="*50)
    
    for idx, (height, expected) in enumerate(test_cases, 1):
        result = trap(height)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Height: {height}")
        print(f"   Output: {result}")
        print(f" Expected: {expected}")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()