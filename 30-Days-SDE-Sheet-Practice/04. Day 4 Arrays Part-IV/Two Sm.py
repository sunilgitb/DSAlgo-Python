# https://leetcode.com/problems/two-sum/
''' 
Keep a track of traversed element in a dictionary. If we get the target - nums[i] then we got the 2 indeces
'''

# https://leetcode.com/problems/two-sum/

'''
Approach:
- Traverse the array
- Store visited numbers with their indices in a dictionary
- For each element, check if (target - current) already exists
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            required = target - nums[i]

            if required in dic:
                return [dic[required], i]

            dic[nums[i]] = i


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    nums = [2, 7, 11, 15]
    target = 9

    print("Array:", nums)
    print("Target:", target)
    print("Indices of Two Sum:", sol.twoSum(nums, target))
