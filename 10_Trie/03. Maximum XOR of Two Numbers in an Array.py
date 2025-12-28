# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = -1   # stores full number at leaf


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addNum(self, num: int) -> None:
        cur = self.root
        for i in range(31, -1, -1):
            bit = 1 if (num & (1 << i)) else 0
            if bit not in cur.children:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
        cur.val = num


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        
        # Insert all numbers into Trie
        for num in nums:
            trie.addNum(num)
        
        res = 0
        
        # For each number, find best possible XOR
        for num in nums:
            cur = trie.root
            for i in range(31, -1, -1):
                bit = 1 if (num & (1 << i)) else 0
                toggled_bit = 1 - bit
                
                if toggled_bit in cur.children:
                    cur = cur.children[toggled_bit]
                else:
                    cur = cur.children[bit]
            
            res = max(res, cur.val ^ num)
        
        return res

if __name__ == "__main__":
    nums = [3, 10, 5, 25, 2, 8]
    
    sol = Solution()
    result = sol.findMaximumXOR(nums)
    
    print("Maximum XOR:", result)
