# https://leetcode.com/problems/top-k-frequent-elements/
# https://youtu.be/YPTqKIgVk-k

from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        num_cnt = collections.Counter()
        for num in nums:
            num_cnt[num] += 1
        
        cnt_num = {}
        for num in num_cnt:
            cnt = num_cnt[num]
            if cnt not in cnt_num: 
                cnt_num[cnt] = [num]
            else: 
                cnt_num[cnt].append(num)
        
        res = []
        n = max(num_cnt.values())
        for cnt in range(n, 0, -1):
            if cnt in cnt_num:
                res += cnt_num[cnt]
            if len(res) >= k: break
        
        return res[:k]  # ensure only k elements

# ================= DRIVER CODE =================
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
    print(sol.topKFrequent([1], 1))            # [1]
    print(sol.topKFrequent([4,4,4,6,6,7,7,7,7], 2)) # [7,4]

    
    
# Time: O(N)
# Space: O(N)
