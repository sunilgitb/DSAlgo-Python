# https://leetcode.com/problems/maximum-length-of-pair-chain/

from typing import List

# DP Approach (O(n²) time, O(n) space)
class SolutionDP:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0
            
        n = len(pairs)
        # Sort by first element
        pairs.sort(key=lambda x: x[0])
        
        # dp[i] = longest chain ending at pairs[i]
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


# Greedy Approach (O(n log n) time, O(1) space)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0
            
        # Sort by first element
        pairs.sort(key=lambda x: x[0])
        
        res = 1
        prev_end = pairs[0][1]
        
        for i in range(1, len(pairs)):
            if prev_end < pairs[i][0]:
                res += 1
                prev_end = pairs[i][1]
            elif pairs[i][1] < prev_end:
                # Better choice: smaller end time for future chaining
                prev_end = pairs[i][1]
        
        return res


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
pairs = [[1,2],[2,3],[3,4]]
print(sol.findLongestChain(pairs))  # Output: 2  ([1,2] → [3,4])

# Example 2
pairs = [[1,2],[7,8],[4,5]]
print(sol.findLongestChain(pairs))  # Output: 3  ([1,2] → [4,5] → [7,8])

# Example 3
pairs = [[1,100],[2,3],[3,4],[4,5]]
print(sol.findLongestChain(pairs))  # Output: 3  ([2,3] → [3,4] → [4,5])

# Example 4
pairs = [[1,2]]
print(sol.findLongestChain(pairs))  # Output: 1

# Example 5
pairs = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(sol.findLongestChain(pairs))  # Output: 6

# Example 6 (overlapping intervals)
pairs = [[5,6],[1,2],[3,4],[2,3]]
print(sol.findLongestChain(pairs))  # Output: 3  ([1,2] → [3,4] → [5,6])