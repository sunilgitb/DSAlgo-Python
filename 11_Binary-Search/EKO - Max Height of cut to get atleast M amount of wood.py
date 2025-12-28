# https://www.spoj.com/problems/EKO/

def eko(n, m, heights):
    """
    Finds the maximum height at which to cut trees to get at least m meters of wood.
    
    Args:
        n: Number of trees
        m: Required meters of wood
        heights: List of tree heights
        
    Returns:
        Maximum possible cutting height
    """
    
    def can_chop(cut_height):
        """Check if cutting at cut_height gives at least m meters of wood."""
        total_wood = 0
        for h in heights:
            if h > cut_height:
                total_wood += h - cut_height
        return total_wood >= m
    
    low = 0
    high = max(heights)
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if can_chop(mid):
            # We can get enough wood → try to increase cut height
            low = mid + 1
        else:
            # Not enough wood → decrease cut height
            high = mid - 1
    
    # After loop, high is the highest possible cut height that still gives >= m wood
    return high


# Driver code to test the solution
if __name__ == "__main__":
    print("Test Case 1: Example from SPOJ")
    n1, m1 = 5, 20
    heights1 = [4, 42, 40, 26, 46]
    print(f"n={n1}, m={m1}, heights={heights1}")
    print(f"Result: {eko(n1, m1, heights1)}")  # Expected: 36
    
    print("\n" + "="*50 + "\n")
    
    print("Test Case 2: Small case")
    n2, m2 = 4, 7
    heights2 = [20, 15, 10, 17]
    print(f"n={n2}, m={m2}, heights={heights2}")
    print(f"Result: {eko(n2, m2, heights2)}")  # Expected: 15
    
    print("\n" + "="*50 + "\n")
    
    print("Test Case 3: All trees same height")
    n3, m3 = 3, 6
    heights3 = [10, 10, 10]
    print(f"n={n3}, m={m3}, heights={heights3}")
    print(f"Result: {eko(n3, m3, heights3)}")  # Expected: 8
    
    print("\n" + "="*50 + "\n")
    
    print("Test Case 4: Need exactly all wood")
    n4, m4 = 3, 25
    heights4 = [10, 10, 10]
    print(f"n={n4}, m={m4}, heights={heights4}")
    print(f"Result: {eko(n4, m4, heights4)}")  # Expected: 0
    
    print("\n" + "="*50 + "\n")
    
    print("Test Case 5: Need more wood than available")
    n5, m5 = 3, 35
    heights5 = [10, 10, 10]
    print(f"n={n5}, m={m5}, heights={heights5}")
    print(f"Result: {eko(n5, m5, heights5)}")  # Expected: -1 (impossible case)
    
    print("\n" + "="*50 + "\n")
    
    print("Test Case 6: Single tree")
    n6, m6 = 1, 5
    heights6 = [10]
    print(f"n={n6}, m={m6}, heights={heights6}")
    print(f"Result: {eko(n6, m6, heights6)}")  # Expected: 5
    
    print("\n" + "="*50 + "\n")
    
    # For SPOJ submission format
    print("SPOJ Submission Format Test:")
    print("Simulating SPOJ input format:")
    
    test_cases = [
        "5 20\n4 42 40 26 46\n",
        "4 7\n20 15 10 17\n",
        "3 6\n10 10 10\n"
    ]
    
    for i, test_input in enumerate(test_cases, 1):
        print(f"\nTest {i}:")
        print(f"Input:\n{test_input}")
        
        # Simulate reading from input
        lines = test_input.strip().split('\n')
        n, m = map(int, lines[0].split())
        heights = list(map(int, lines[1].split()))
        
        result = eko(n, m, heights)
        print(f"Output: {result}")
    
    print("\n" + "="*50 + "\n")
    
    # Large test case simulation
    print("Large Test Case (performance test simulation):")
    n_large = 1000000
    m_large = 2000000000
    # Simulating heights around 1e9
    print(f"n={n_large}, m={m_large}")
    print("(Simulation: algorithm should handle this efficiently with O(n log max_height))")
    
    print("\n" + "="*50 + "\n")
    
    # Interactive testing
    print("To use this for SPOJ submission:")
    print("1. Remove all driver code")
    print("2. Keep only the eko() function and the main reading logic")
    print("3. Submit the code as shown below:")
    
    print("\n" + "="*50 + "\n")
    print("SPOJ Submission Code:")
    print("""def main():
    import sys
    
    def can_chop(cut_height, heights, m):
        total_wood = 0
        for h in heights:
            if h > cut_height:
                total_wood += h - cut_height
        return total_wood >= m
    
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n, m = int(data[0]), int(data[1])
    heights = list(map(int, data[2:2+n]))
    
    low = 0
    high = max(heights)
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if can_chop(mid, heights, m):
            low = mid + 1
        else:
            high = mid - 1
    
    print(high)

if __name__ == "__main__":
    main()""")