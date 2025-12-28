# https://leetcode.com/problems/top-k-frequent-elements/
# https://youtu.be/YPTqKIgVk-k
# Bucket Sort

from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCountDict = {}  # key = num; value = count
        for num in nums:
            if num not in numCountDict: 
                numCountDict[num] = 1
            else: 
                numCountDict[num] += 1
        
        maxCount = max(numCountDict.values())
        countNumDict = {i:[] for i in range(1, maxCount+1)}
        
        for num in numCountDict:
            countNumDict[numCountDict[num]].append(num)
        
        res = []
        for count in range(maxCount, 0, -1):
            if len(res) >= k: break
            if countNumDict[count]:
                res += countNumDict[count]
        
        return res[:k]  # ensure exactly k elements

# ================= DRIVER CODE =================
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    sol = Solution()
    print(f"Top {k} frequent elements:", sol.topKFrequent(nums, k))

        
# Time: O(N)
# SPace: O(N)

