# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# https://www.youtube.com/watch?v=QM0klnvTQzk

# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# https://www.youtube.com/watch?v=QM0klnvTQzk

from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Count of prefix sum remainders
        remainderCountDic = {0: 1}
        curSum = 0
        ans = 0
        
        for num in nums:
            curSum += num
            # Handle negative prefix sum
            curSum = ((curSum % k) + k) % k
            
            if curSum in remainderCountDic:
                ans += remainderCountDic[curSum]
                remainderCountDic[curSum] += 1
            else:
                remainderCountDic[curSum] = 1
        
        return ans


# ================= DRIVER CODE =================
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.subarraysDivByK([4,5,0,-2,-3,1], 5))   # 7
    print(sol.subarraysDivByK([5], 9))               # 0
    print(sol.subarraysDivByK([7, 4, -10], 5))       # 1
    print(sol.subarraysDivByK([1,2,3,4,5], 3))       # 4
