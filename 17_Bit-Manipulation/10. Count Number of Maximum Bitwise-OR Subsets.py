# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/



from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Calculate the maximum OR possible
        maxOR = 0
        for num in nums:
            maxOR |= num
        
        # DFS helper function
        def dfs(i, val):
            if val == maxOR: 
                # All remaining subsets will also have maxOR
                return 1 << (len(nums) - i)
            if i == len(nums): 
                return 0
            # Include nums[i] OR exclude nums[i]
            return dfs(i+1, val | nums[i]) + dfs(i+1, val)
        
        return dfs(0, 0)


# -------- Driver Code --------
solution = Solution()

print(solution.countMaxOrSubsets([3, 1]))          # 2
print(solution.countMaxOrSubsets([2, 2, 2]))       # 7
print(solution.countMaxOrSubsets([3, 2, 1, 5]))    # 6
print(solution.countMaxOrSubsets([1, 2, 3, 4]))    # 4
