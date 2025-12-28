# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefixArr = []
        s = 0
        for i in nums:
            s += i
            prefixArr.append(s)
        
        # max sum of subarray of length k ending at or before i
        def left(k):
            arr = [0] * n
            curmax = 0
            for i in range(k-1, n):
                cur = prefixArr[i] - (prefixArr[i-k] if i-k >= 0 else 0)
                curmax = max(curmax, cur)
                arr[i] = curmax
            return arr
        
        # max sum of subarray of length k starting at or after i
        def right(k):
            arr = [0] * n
            curmax = 0
            for i in range(n-k, -1, -1):
                cur = prefixArr[i+k-1] - (prefixArr[i-1] if i-1 >= 0 else 0)
                curmax = max(curmax, cur)
                arr[i] = curmax
            return arr
        
        first_left = left(firstLen)
        first_right = right(firstLen)
        second_left = left(secondLen)
        second_right = right(secondLen)
        
        res = 0
        for i in range(1, n):
            a = first_left[i-1] + second_right[i]
            b = second_left[i-1] + first_right[i]
            res = max(res, a, b)
        
        return res


if __name__ == "__main__":
    solution = Solution()
    
    nums = [0,6,5,2,2,5,1,9,4]
    firstLen = 1
    secondLen = 2
    print(solution.maxSumTwoNoOverlap(nums, firstLen, secondLen))  # Output: 20

    nums = [3,8,1,3,2,1,8,9,0]
    firstLen = 3
    secondLen = 2
    print(solution.maxSumTwoNoOverlap(nums, firstLen, secondLen))  # Output: 29

    nums = [2,1,5,6,0,9,5,0,3,8]
    firstLen = 4
    secondLen = 3
    print(solution.maxSumTwoNoOverlap(nums, firstLen, secondLen))  # Output: 31
