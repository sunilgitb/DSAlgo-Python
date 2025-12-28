# https://leetcode.com/problems/subsets-ii/

# Use the same concept of 01. Subset Sums

# https://leetcode.com/problems/subsets-ii/
# Subsets II - Return all possible subsets (including duplicates) without duplicate subsets

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to handle duplicates easily
        res = []
        
        def dfs(i: int, subset: List[int]):
            # Base case: we've considered all elements
            if i >= len(nums):
                res.append(subset[:])  # Add a copy of current subset
                return
            
            # 1. Include the current element
            dfs(i + 1, subset + [nums[i]])
            
            # 2. Skip all duplicates of the current element
            # (to avoid duplicate subsets)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            # Now skip the current element (and all its duplicates)
            dfs(i + 1, subset)
        
        dfs(0, [])
        return res


# ──────────────────────────────────────────────────────────────
# Driver Code (for local testing)
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [1, 2, 2]
    result1 = sol.subsetsWithDup(nums1)
    print("Input:", nums1)
    print("Output:")
    for subset in sorted(result1):  # Sorted for readability
        print(subset)
    # Expected (all unique subsets):
    # []
    # [1]
    # [1,2]
    # [1,2,2]
    # [2]
    # [2,2]

    print("-" * 50)

    # Test Case 2
    nums2 = [0]
    result2 = sol.subsetsWithDup(nums2)
    print("Input:", nums2)
    print("Output:")
    for subset in sorted(result2):
        print(subset)
    # Expected: [], [0]

    print("-" * 50)

    # Test Case 3
    nums3 = [1, 2, 3]
    result3 = sol.subsetsWithDup(nums3)
    print("Input:", nums3)
    print("Output:")
    for subset in sorted(result3):
        print(subset)
    # Expected: all 8 unique subsets
            

# Time: O(2^n)
# Space: O(2^n)  # as we are storeing subsets in path array in each calls