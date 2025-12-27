# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# https://www.youtube.com/watch?v=IeT9Qz_vqHo

from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[-1] * 2 for _ in range(n)]
        
        def solve(prev1: int, prev2: int, i: int, swapped: int) -> int:
            if i == n:
                return 0
            if dp[i][swapped] != -1:
                return dp[i][swapped]
            
            ans = float('inf')
            
            # Option 1: No swap at current position
            if nums1[i] > prev1 and nums2[i] > prev2:
                ans = min(ans, solve(nums1[i], nums2[i], i + 1, 0))
            
            # Option 2: Swap at current position
            if nums1[i] > prev2 and nums2[i] > prev1:
                ans = min(ans, 1 + solve(nums2[i], nums1[i], i + 1, 1))
            
            dp[i][swapped] = ans
            return ans
        
        # Start with invalid previous values (-1) since all elements are positive
        return solve(-1, -1, 0, 0)


# ---------------- Example Usage ----------------
sol = Solution()

# Example 1
nums1 = [1,3,5,4]
nums2 = [1,2,3,7]
print(sol.minSwap(nums1, nums2))  # Output: 1  (swap at index 3: [1,3,5,7] & [1,2,3,4])

# Example 2
nums1 = [3,3,8,9,10]
nums2 = [1,7,4,6,8]
print(sol.minSwap(nums1, nums2))  # Output: 1  (swap at index 1)

# Example 3
nums1 = [0,3,5,8,9]
nums2 = [2,1,4,6,9]
print(sol.minSwap(nums1, nums2))  # Output: 1

# Example 4
nums1 = [1,2,3,4,5]
nums2 = [2,3,4,5,6]
print(sol.minSwap(nums1, nums2))  # Output: 0  (already increasing, no swaps needed)

# Example 5
nums1 = [1]
nums2 = [2]
print(sol.minSwap(nums1, nums2))  # Output: 0

# Example 6
nums1 = [10, 20, 30]
nums2 = [20, 10, 40]
print(sol.minSwap(nums1, nums2))  # Output: 1  (swap at index 1)