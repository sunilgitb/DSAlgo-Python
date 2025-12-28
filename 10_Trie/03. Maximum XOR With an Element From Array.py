from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def addNum(self, num):
        cur = self.root
        for i in range(31, -1, -1):
            bit = 1 if num & (1 << i) else 0
            if bit not in cur.children:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
        cur.val = num
        
    def getMax(self, x):
        cur = self.root
        for i in range(31, -1, -1):
            bit = 1 if x & (1 << i) else 0  
            if bit == 1:
                if 0 in cur.children:
                    cur = cur.children[0]
                elif 1 in cur.children:
                    cur = cur.children[1]
                else:
                    return -1
            else:
                if 1 in cur.children:
                    cur = cur.children[1]
                elif 0 in cur.children:
                    cur = cur.children[0]
                else:
                    return -1
        return cur.val ^ x
        
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        res = [-1] * len(queries)
        
        # attach original index
        for i in range(len(queries)):
            queries[i].append(i)
        
        # sort by mi
        queries.sort(key=lambda x: x[1])
        
        n = 0
        for x, m, idx in queries:
            while n < len(nums) and nums[n] <= m:
                self.addNum(nums[n])
                n += 1
            res[idx] = self.getMax(x)
        
        return res


# ---------------- DRIVER CODE ----------------

nums = [0, 1, 2, 3, 4]
queries = [[3, 1], [1, 3], [5, 6]]

sol = Solution()
output = sol.maximizeXor(nums, queries)
print(output)
