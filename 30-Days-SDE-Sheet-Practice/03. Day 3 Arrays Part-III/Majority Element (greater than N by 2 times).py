# https://leetcode.com/problems/majority-element/
''' 
take an assumed majority element and count of that element. if current element equal then increase the count
else decrease by 1. the element present at the end will be the majority element.
'''

cfrom typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = -1   # me = Majority Element
        count = 0 # count = Count of Majority Element
        
        for i in range(len(nums)):
            if nums[i] == me:
                count += 1
            elif count > 0 and nums[i] != me:
                count -= 1
            
            if count == 0:
                me = nums[i]
                count = 1
        
        if nums.count(me) > len(nums) // 2:
            return me
        return -1


# ----------------- Driver Code -----------------
if __name__ == "__main__":
    test_cases = [
        [3, 3, 4],
        [2, 2, 1, 1, 1, 2, 2],
        [1, 2, 3],
        [1, 1, 1, 2, 3, 4, 1]
    ]
    
    sol = Solution()
    for nums in test_cases:
        print(f"Array: {nums} -> Majority Element: {sol.majorityElement(nums)}")
