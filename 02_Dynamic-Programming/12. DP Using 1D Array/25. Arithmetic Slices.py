class Solution:
    # Solution 1: Bottom up DP (Space O(n))
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3:
            return 0
            
        dp = [0] * n
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        
        return sum(dp)
    
    # Solution 2: Bottom up DP (Space Optimized O(1))
    def numberOfArithmeticSlices_optimized(self, nums):
        n = len(nums)
        if n < 3:
            return 0
            
        dp = 0
        res = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
                res += dp
            else:
                dp = 0
                
        return res


# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        [1, 2, 3, 4],  # Expected: 3
        [1, 3, 5, 7, 9],  # Expected: 6
        [1, 2, 3, 8, 9, 10],  # Expected: 2
        [1],  # Expected: 0
        [1, 2],  # Expected: 0
        [1, 1, 1, 1, 1],  # Expected: 6
        [7, 7, 7, 7],  # Expected: 3
        [3, -1, -5, -9],  # Expected: 3
        [1, 3, 5, 7, 9, 15, 20, 25, 28, 29],  # Expected: 7
    ]
    
    print("Testing Solution 1 (Space O(n)):")
    print("=" * 40)
    for i, test in enumerate(test_cases, 1):
        result = solution.numberOfArithmeticSlices(test)
        print(f"Test {i}: {test}")
        print(f"Result: {result}")
        print("-" * 40)
    
    print("\nTesting Solution 2 (Space O(1)):")
    print("=" * 40)
    for i, test in enumerate(test_cases, 1):
        result = solution.numberOfArithmeticSlices_optimized(test)
        print(f"Test {i}: {test}")
        print(f"Result: {result}")
        print("-" * 40)
    
    # Additional verification
    print("\nVerification (both methods should give same results):")
    print("=" * 40)
    for i, test in enumerate(test_cases, 1):
        result1 = solution.numberOfArithmeticSlices(test)
        result2 = solution.numberOfArithmeticSlices_optimized(test)
        match = "✓" if result1 == result2 else "✗"
        print(f"Test {i}: Method1={result1}, Method2={result2} {match}")