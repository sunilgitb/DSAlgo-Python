class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        
        def solve(i, j):
            if i == j == 0:
                return 1
            if i < 0 or j < 0 or abs(i - j) > 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            ans = 0
            if i == j:
                ans += solve(i-1, j-1)     # vertical domino
                ans += solve(i-2, j-2)     # two horizontal dominos
                ans += solve(i-1, j-2)     # L tromino
                ans += solve(i-2, j-1)     # reverse L tromino
            elif i > j:
                ans += solve(i-2, j)       # vertical domino on left
                ans += solve(i-2, j-1)     # tromino
            else:  # j > i
                ans += solve(i, j-2)
                ans += solve(i-1, j-2)

            memo[(i, j)] = ans % MOD
            return memo[(i, j)]

        return solve(n, n)


class Solution2:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0, 1, 2, 5] + [1] * n
        if n <= 3: 
            return dp[n]
        
        for i in range(4, n+1):
            dp[i] = ((2 * dp[i-1]) % MOD + dp[i-3]) % MOD
        
        return dp[n]


# Driver code
if __name__ == "__main__":
    # Test cases
    test_cases = [1, 2, 3, 4, 5, 10, 30]
    
    print("Testing both solutions:")
    print("-" * 50)
    
    for n in test_cases:
        sol1 = Solution()
        sol2 = Solution2()
        
        result1 = sol1.numTilings(n)
        result2 = sol2.numTilings(n)
        
        print(f"n = {n:2d}:")
        print(f"  Solution 1 (memoization): {result1}")
        print(f"  Solution 2 (DP formula):  {result2}")
        print(f"  Match: {'✓' if result1 == result2 else '✗'}")
    
    print("\n" + "=" * 50)
    print("Explanation of the DP formula approach:")
    print("f(n) = 2*f(n-1) + f(n-3)")
    print("where f(0)=1, f(1)=1, f(2)=2, f(3)=5")
    print("\nBase cases:")
    print("f(1) = 1   (|)")
    print("f(2) = 2   (||, =)")
    print("f(3) = 5   (|||, |=, =|, ⌈⌉, ⌊⌋)")
    
    # Show first 10 values
    print("\nFirst 10 values:")
    sol = Solution2()
    for i in range(1, 11):
        print(f"f({i}) = {sol.numTilings(i)}")