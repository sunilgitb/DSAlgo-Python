# https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.res = 0
        nums.sort()
        seen = set()
        
        def dfs(subset, i):
            if i >= len(nums):
                if len(subset) > 0: self.res += 1
                return 
            if nums[i] - k not in seen:
                seen.add(nums[i])
                dfs(subset + [nums[i]], i+1)
                seen.discard(nums[i])
            dfs(subset, i+1)
        
        dfs([], 0)
        return self.res
    
    
# Time: O(2^n)    

from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        seen = set()
        
        def dfs(i):
            if i == len(nums):
                return 1  # count this subset
            count = 0
            # Include nums[i] if it does not conflict
            if nums[i] - k not in seen:
                seen.add(nums[i])
                count += dfs(i + 1)
                seen.discard(nums[i])
            # Exclude nums[i]
            count += dfs(i + 1)
            return count
        
        return dfs(0) - 1  # subtract 1 to exclude empty subset


# ------------------- Driver Code -------------------

if __name__ == "__main__":
    solution = Solution()
    
    nums = [2, 4, 6]
    k = 2
    print(solution.beautifulSubsets(nums, k))  
    # Output: 4
    # Explanation: Beautiful subsets are [2], [4], [6], [2,6]

    nums = [1, 2, 3, 4]
    k = 1
    print(solution.beautifulSubsets(nums, k))  
    # Output: 8
    # Explanation: Beautiful subsets are [1], [2], [3], [4], [1,3], [1,4], [2,4], [1,3,4]

''' NOTE:
The discard() method removes the specified item from the set. This method is different from the remove() method, 
because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
'''
