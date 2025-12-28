# https://leetcode.com/problems/continuous-subarray-sum/

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # remainder -> earliest index
        sumIndexDic = {0: -1}
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i]

            if k != 0:
                curSum %= k

            if curSum in sumIndexDic:
                if i - sumIndexDic[curSum] >= 2:
                    return True
            else:
                sumIndexDic[curSum] = i

        return False


# ================= DRIVER CODE =================
if __name__ == "__main__":
    sol = Solution()

    print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))   # True
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 6))   # True
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 13))  # False
    print(sol.checkSubarraySum([0, 0], 0))            # True
