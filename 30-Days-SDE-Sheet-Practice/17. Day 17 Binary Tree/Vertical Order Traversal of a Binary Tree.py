# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# https://youtu.be/q_a6lpbKJdw
'''
If some nodes of same horizontal level comes in same vertical level then we should only sort those nodes.
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = {}
        def solve(root, d, l):  # (root, horizontal distance form middle, level)
            if not root: return
            
            if d not in self.dic:
                self.dic[d] = [(l, root.val)]
            else:
                self.dic[d].append((l, root.val))
                
            solve(root.left, d-1, l+1)
            solve(root.right, d+1, l+1)
        
        solve(root, 0, 0)
        keys = sorted(list(self.dic.keys()))
        
        res = []
        for key in keys:
            values = self.dic[key]
            values.sort()  # sorting is done based on level then for same level nodes based on values
            res.append([r[1] for r in values])  # r = (level, root.val)
            
        return res

# Time: O(N)  ; as in a horizontal level of a specific vertical level key, can has at most log(n) - 1 nodes so sorting time is still less than O(N)
# Space: O(N)

# Example Usage
# Constructing the binary tree:
#         3
#        / \
#       9   20
#          /  \
#         15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print(solution.verticalTraversal(root))  # Output: [[9], [3, 15], [20], [7]]
