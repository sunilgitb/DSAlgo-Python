from typing import List

# Method 1: Memoization (Top-Down)
class SolutionMemo:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ZOCount = [(s.count('0'), s.count('1')) for s in strs]
        memo = {}
        
        def dfs(m_left, n_left, i):
            if m_left < 0 or n_left < 0: 
                return -2**31  # very small number to invalidate invalid paths
            if i == len(ZOCount):
                return 0
            if (m_left, n_left, i) in memo: 
                return memo[(m_left, n_left, i)]
            
            zeros, ones = ZOCount[i]
            # Option 1: skip this string
            skip = dfs(m_left, n_left, i + 1)
            # Option 2: take this string (if possible)
            take = -2**31
            if m_left >= zeros and n_left >= ones:
                take = 1 + dfs(m_left - zeros, n_left - ones, i + 1)
            
            ans = max(take, skip)
            memo[(m_left, n_left, i)] = ans
            return ans
        
        return dfs(m, n, 0)

# Method 2: DP Tabulation (Bottom-Up)
class SolutionDP:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            
            # Iterate backward to avoid using the same string multiple times
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
        
        return dp[m][n]


# ───────────────────────────────────────────────────────────────
# Example Usage
# ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Test cases from LeetCode problem
    test_cases = [
        {
            "strs": ["10", "0001", "111001", "1", "0"],
            "m": 5,
            "n": 3,
            "expected": 4
        },
        {
            "strs": ["10", "0", "1"],
            "m": 1,
            "n": 1,
            "expected": 2
        },
        {
            "strs": ["111", "1000", "1000", "1000"],
            "m": 2,
            "n": 2,
            "expected": 1
        },
        {
            "strs": ["000", "00"],
            "m": 3,
            "n": 0,
            "expected": 2
        }
    ]

    # Create instances
    sol_memo = SolutionMemo()
    sol_dp = SolutionDP()

    print("=== Testing Both Solutions ===\n")
    
    for idx, case in enumerate(test_cases, 1):
        strs = case["strs"]
        m = case["m"]
        n = case["n"]
        expected = case["expected"]

        result_memo = sol_memo.findMaxForm(strs, m, n)
        result_dp = sol_dp.findMaxForm(strs, m, n)

        print(f"Test Case {idx}:")
        print(f"  strs = {strs}")
        print(f"  m = {m}, n = {n}")
        print(f"  Expected: {expected}")
        print(f"  Memoization: {result_memo} {'✓' if result_memo == expected else '✗'}")
        print(f"  Bottom-Up DP: {result_dp} {'✓' if result_dp == expected else '✗'}")
        print("-" * 60)