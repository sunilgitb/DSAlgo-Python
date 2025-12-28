# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        curSum = 0
        res = 0
        
        for num in nums:
            curSum += num
            if (curSum - k) in hashmap:
                res += hashmap[curSum - k]
            hashmap[curSum] = hashmap.get(curSum, 0) + 1
        
        return res

# ================= DRIVER CODE =================
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.subarraySum([1,1,1], 2))            # 2
    print(sol.subarraySum([1,2,3], 3))            # 2
    print(sol.subarraySum([1,2,1,2,1], 3))        # 4
    print(sol.subarraySum([3,4,7,2,-3,1,4,2], 7)) # 4
