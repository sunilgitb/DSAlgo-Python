# https://leetcode.com/problems/reverse-pairs/
# https://youtu.be/S6rsAlj_iB4
'''
use the merge sort concept of Inversion of Array 
https://github.com/SamirPaulb/DSAlgo/blob/main/30-Days-SDE-Sheet-Practice/02.%20Day%202%20Arrays%20Part-II/Inversion%20of%20Array%20-using%20Merge%20Sort.py
'''
# https://leetcode.com/problems/reverse-pairs/
# https://youtu.be/S6rsAlj_iB4
'''
use the merge sort concept of Inversion of Array 
https://github.com/SamirPaulb/DSAlgo/blob/main/30-Days-SDE-Sheet-Practice/02.%20Day%202%20Arrays%20Part-II/Inversion%20of%20Array%20-using%20Merge%20Sort.py
'''
from typing import List

class Solution:
    def __init__(self):
        self.count = 0
    
    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        return self.count
    
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            
            # Recursive call on left and right halves
            self.mergeSort(left)
            self.mergeSort(right)
            
            # Count reverse pairs
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                self.count += j
            
            # Merge step
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1


# ----------------- Driver Code -----------------
if __name__ == "__main__":
    nums_list = [
        [1, 3, 2, 3, 1],
        [2, 4, 3, 5, 1],
        [5, 4, 3, 2, 1]
    ]
    
    sol = Solution()
    for nums in nums_list:
        # Reset count for each test case
        sol.count = 0
        print(f"Array: {nums} -> Reverse Pairs: {sol.reversePairs(nums.copy())}")


# Time: O(n log(n))
# Space: O(n)
# Time: O(n log(n))
# Space: O(n)