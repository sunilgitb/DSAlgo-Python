# https://leetcode.com/problems/majority-element/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = -1   # Majority Element
        count = 0
        
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

# ================= DRIVER CODE =================
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.majorityElement([3,2,3]))        # 3
    print(sol.majorityElement([2,2,1,1,1,2,2]))# 2
    print(sol.majorityElement([1,2,3,4]))      # -1
    print(sol.majorityElement([1,1,1,2,2]))    # 1
