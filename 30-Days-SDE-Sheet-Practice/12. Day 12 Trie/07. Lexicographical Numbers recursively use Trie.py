# https://leetcode.com/problems/lexicographical-numbers/
''' 
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Basice idea: think about Trie. we append digits to the specific suffix until we reach the target number.
'''
from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # recursively use Trie
        res = []
        if n < 10:
            return list(range(1, n+1))
        for i in range(1, 10):
            res += [i]
            res += self.helper(i, n)
        return res
    
    def helper(self, start, n):
        res = []
        for aux in range(10):
            newStart = start*10+aux
            if newStart > n:
                break
            res += [newStart]
            res += self.helper(newStart, n)
        return res
    
# Time: O(n)
# Space: O(1)


# Example / driver code 🔧
if __name__ == "__main__":
    sol = Solution()

    print("n=13 ->", sol.lexicalOrder(13))  # [1,10,11,12,13,2,3,4,5,6,7,8,9]
    print("n=2 ->", sol.lexicalOrder(2))    # [1,2]

    # Sanity checks
    assert sol.lexicalOrder(13) == [1,10,11,12,13,2,3,4,5,6,7,8,9]
    assert sol.lexicalOrder(2) == [1,2]
    assert sol.lexicalOrder(1) == [1]

    print("Driver tests passed ✅")