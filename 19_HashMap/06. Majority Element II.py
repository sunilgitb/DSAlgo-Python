# https://leetcode.com/problems/majority-element-ii/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        me1, me2 = -1, -2
        count1, count2 = 0, 0
        
        for num in nums:
            if num == me1:
                count1 += 1
            elif num == me2:
                count2 += 1
            elif count1 == 0:
                me1, count1 = num, 1
            elif count2 == 0:
                me2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = set()
        if nums.count(me1) > n // 3: res.add(me1)
        if nums.count(me2) > n // 3: res.add(me2)
        
        return list(res)

# ================= DRIVER CODE =================
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.majorityElement([3,2,3]))           # [3]
    print(sol.majorityElement([1,1,1,3,3,2,2,2])) # [1,2]
    print(sol.majorityElement([1,2]))             # [1,2]
    print(sol.majorityElement([1,2,3,4]))         # []
