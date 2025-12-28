# https://leetcode.com/problems/hand-of-straights/

import collections

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        cnt = collections.Counter(nums)
        numset = sorted(cnt.keys())
        i = 0
        while i < len(numset):
            c = numset[i]
            if cnt[c] > 0:
                for j in range(k):
                    if cnt[c+j] == 0:
                        return False
                    cnt[c+j] -= 1
            else:
                i += 1
        return True


if __name__ == "__main__":
    solution = Solution()
    
    nums = [1,2,3,3,4,4,5,6]
    k = 4
    print(solution.isPossibleDivide(nums, k))  # True
    
    nums = [3,3,2,2,1,1]
    k = 3
    print(solution.isPossibleDivide(nums, k))  # True
    
    nums = [1,2,3,4]
    k = 3
    print(solution.isPossibleDivide(nums, k))  # False

      
# Time: O(N log(N))
