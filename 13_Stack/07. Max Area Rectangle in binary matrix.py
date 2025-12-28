# 07. Maximal Rectangle in Binary Matrix
# Problem: Given a binary matrix filled with 0s and 1s,
# find the largest rectangle containing only 1s and return its area.
# This is an extension of "Largest Rectangle in Histogram" problem.
# Optimal solution using Stack (Monotonic Stack)

def maximal_rectangle(matrix):
    """
    Returns the maximum area of a rectangle containing only 1s.
    
    Time Complexity: O(rows * cols)
    Space Complexity: O(cols)
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # heights[i] = number of consecutive 1s ending at row r in column i
    heights = [0] * cols
    max_area = 0
    
    for r in range(rows):
        # Update heights array
        for c in range(cols):
            if matrix[r][c] == '1':
                heights[c] += 1
            else:
                heights[c] = 0
        
        # Compute largest rectangle area in current histogram
        area = largest_rectangle_area(heights)
        max_area = max(max_area, area)
    
    return max_area


def largest_rectangle_area(heights):
    """
    Given an array of heights representing a histogram,
    find the largest rectangle area in it.
    Uses Monotonic Stack.
    """
    n = len(heights)
    stack = []  # stores indices
    max_area = 0
    
    # Add sentinel -1 at the end to handle remaining bars
    heights.append(0)
    
    for i in range(n + 1):
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, height * width)
        stack.append(i)
    
    heights.pop()  # remove sentinel
    return max_area


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Example 1
        ([
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ], 6),  # Output: 6
        
        # Example 2
        ([["0"]], 0),
        
        # All 1s
        ([
            ["1", "1"],
            ["1", "1"]
        ], 4),
        
        # Single row
        ([["1", "1", "0", "1"]], 2),
        
        # All zeros
        ([["0", "0"], ["0", "0"]], 0),
        
        # Larger example
        ([
            ["1", "1", "1", "0", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "0", "0", "0"]
        ], 10),
        
        # Edge case: empty matrix
        ([], 0),
    ]
    
    print("Testing Maximal Rectangle in Binary Matrix\n" + "="*50)
    
    for idx, (matrix, expected) in enumerate(test_cases, 1):
        result = maximal_rectangle(matrix)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Matrix:")
        for row in matrix:
            print(f"      {row}")
        print(f"   Output: {result}")
        print(f" Expected: {expected}")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()