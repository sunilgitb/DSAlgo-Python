# https://leetcode.com/problems/search-in-rotated-sorted-array/
''' 
Even the array is rotated sorted if we can use binary search in it, as one sided of the mid will be 
sorted and other sider unsorted. if target not present in sorted side then it must be in the unsorted 
part. change l and r pointer likewise.
'''
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0; r = len(nums)-1
        
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] == target: return mid
            
            elif nums[l] <= nums[mid]:  # Left subarray of mid is sorted
                if nums[l] <= target < nums[mid]: # target present at Left subarray of mid 
                    r = mid-1
                else: # target at right subarray of mid
                    l = mid+1
            else:  # right subarray of mid is sorted
                if nums[mid] < target <= nums[r]:  # target is present at right subarray of mid
                    l = mid+1
                else:  # target at left subarray of mid
                    r = mid - 1
        
        return -1

# Time: O(log(n))
# Space: O(1)


if __name__ == "__main__":
    # ✅ Driver code with example tests
    s = Solution()

    tests = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
        ([1,3], 3, 1),
        ([], 5, -1),
    ]

    for i, (nums, target, expected) in enumerate(tests, 1):
        res = s.search(nums, target)
        print(f"Test {i}: nums={nums}, target={target} -> res={res} (expected={expected})")