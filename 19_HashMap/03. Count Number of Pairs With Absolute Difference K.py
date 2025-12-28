# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

from collections import Counter

class Solution:
    def countKDifference(self, nums, k):
        cnt = Counter(nums)
        res = 0
        taken = set()
        for n in cnt:
            l, r = n - k, n + k
            if l not in taken:
                res += cnt[n] * cnt.get(l, 0)
            if r not in taken:
                res += cnt[n] * cnt.get(r, 0)
            taken.add(n)
        return res


# ================= DRIVER CODE =================
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.countKDifference([1,2,2,1], 1))          # 4
    print(sol.countKDifference([1,3], 3))              # 0
    print(sol.countKDifference([3,2,1,5,4], 2))        # 3
    print(sol.countKDifference([1,5,1,5], 4))          # 4

        
    
'''    
class Solution:
    def countKDifference(self, nums, k):
        seen = {num:0 for num in nums}
        count = 0
        
        for num in nums:
            tmp1 = num - k;  tmp2 = num + k
            if tmp1 in seen:
                count += seen[tmp1]
            elif tmp2 in seen:
                count += seen[tmp2]
            seen[num] += 1
        
        return count
'''


# Time: O(N)
# Space: O(N)
