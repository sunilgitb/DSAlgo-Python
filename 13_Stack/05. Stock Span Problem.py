# 05. Stock Span Problem
# The stock span problem is a financial problem where we have a series of daily stock prices.
# The span of the stock's price on a given day is defined as the maximum number of consecutive days
# (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

# Example:
# Input:  [100, 80, 60, 70, 60, 75, 85]
# Output: [1,  1,  1,  2,  1,  4,  6]

# Optimal solution using Stack (Monotonic Stack)
# Time Complexity: O(n) - each element pushed/popped at most once
# Space Complexity: O(n)

def stock_span(prices):
    """
    Returns a list where span[i] = number of consecutive days (including today)
    where prices[i] was greater than or equal to previous days' prices.
    """
    n = len(prices)
    span = [1] * n  # Every day has at least span 1 (itself)
    stack = []      # stores indices of prices in decreasing order
    
    for i in range(n):
        # Pop elements that are smaller than or equal to current price
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        # If stack is empty, span = i+1 (all previous days)
        # Else, span = i - top of stack
        span[i] = i - stack[-1] if stack else i + 1
        
        # Push current index
        stack.append(i)
    
    return span


# Driver Code with multiple test cases
def run_tests():
    test_cases = [
        # Classic example
        ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
        
        # All increasing
        ([10, 20, 30, 40, 50], [1, 2, 3, 4, 5]),
        
        # All decreasing
        ([50, 40, 30, 20, 10], [1, 1, 1, 1, 1]),
        
        # Duplicates
        ([100, 100, 100, 100], [1, 2, 3, 4]),
        
        # Single element
        ([500], [1]),
        
        # Empty array
        ([], []),
        
        # Another standard example
        ([10, 4, 5, 90, 120, 80], [1, 1, 2, 4, 5, 1]),
        
        # Large numbers with mix
        ([11, 13, 21, 3], [1, 2, 3, 1]),
    ]
    
    print("Testing Stock Span Problem\n" + "="*40)
    
    for idx, (prices, expected) in enumerate(test_cases, 1):
        result = stock_span(prices)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {idx:2d}: {status}")
        print(f"   Prices: {prices}")
        print(f"   Output: {result}")
        print(f" Expected: {expected}")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()