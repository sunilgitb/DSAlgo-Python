class Solution:
    # Method 1: Memoization
    def integerBreak_memo(self, n: int) -> int:
        dp = {1: 1}
        
        def dfs(num):
            if num in dp:
                return dp[num]
            
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]
        
        return dfs(n)
    
    # Method 2: Dynamic Programming
    def integerBreak_dp(self, n: int) -> int:
        dp = [0, 1]
        for m in range(2, n + 1):
            j = m - 1
            i = 1
            max_product = 0
            while i <= j:
                max_product = max(max_product, max(i, dp[i]) * max(j, dp[j]))
                j -= 1
                i += 1
            dp.append(max_product)
        return dp[n]
    
    # Method 3: Mathematical
    def integerBreak_math(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
        if n % 3 == 0:
            return 3 ** (n // 3)
        if n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        if n % 3 == 2:
            return 3 ** (n // 3) * 2


# Test cases
solution = Solution()
test_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("Testing all three methods:")
print("-" * 60)
print("n\tMemo\tDP\tMath")
print("-" * 60)

for n in test_nums:
    memo = solution.integerBreak_memo(n)
    dp = solution.integerBreak_dp(n)
    math = solution.integerBreak_math(n)
    print(f"{n}\t{memo}\t{dp}\t{math}")
    if not (memo == dp == math):
        print(f"Warning: Results don't match for n={n}!")