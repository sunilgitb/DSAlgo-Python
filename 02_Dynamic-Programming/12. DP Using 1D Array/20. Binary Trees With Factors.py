from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        MOD = 10**9 + 7
        dp = {}
        
        for i, x in enumerate(arr):
            dp[x] = 1  # single node tree
            for j in range(i):
                if x % arr[j] == 0:  # arr[j] can be left child
                    right = x // arr[j]
                    if right in dp:  # valid right child
                        dp[x] += dp[arr[j]] * dp[right]
                        dp[x] %= MOD
        
        return sum(dp.values()) % MOD

# ------------------- Driver Code -------------------
if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 5, 10]
    print(sol.numFactoredBinaryTrees(arr))  # Output: 7
