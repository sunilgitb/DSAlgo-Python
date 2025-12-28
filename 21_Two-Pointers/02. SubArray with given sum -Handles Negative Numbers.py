# https://practice.geeksforgeeks.org/problems/subarray-range-with-given-sum0128/1

import collections

class Solution:
    def subArraySum(self,arr, n, sum):
        s = res = 0
        cnt = collections.Counter()
        cnt[0] = 1
        for i in arr:
            s += i
            k = s-sum
            res += cnt[k]
            cnt[s] += 1
        return res
        
if __name__ == "__main__":
    solution = Solution()
    
    arr = [1, 1, 1]
    n = len(arr)
    s = 2
    print(solution.subArraySum(arr, n, s))  # Output: 2 ([1,1] twice)
    
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    s = 5
    print(solution.subArraySum(arr, n, s))  # Output: 2 ([2,3] and [5])
    
    arr = [3, 4, 7, 2, -3, 1, 4, 2]
    n = len(arr)
    s = 7
    print(solution.subArraySum(arr, n, s))  # Output: 4 ([3,4],[7],[2,-3,1,4,2],[1,4,2])
