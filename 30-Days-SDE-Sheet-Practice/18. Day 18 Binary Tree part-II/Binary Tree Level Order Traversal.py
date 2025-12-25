# https://leetcode.com/problems/binary-tree-level-order-traversal/

import collections
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res = []
        if not root: 
            return res
        q.append(root)
        
        while q:
            tmp = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                tmp.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            res.append(tmp)
            
        return res

# Time: O(N)
# Space: O(N)
# N is the number of nodes in the binary tree
# BFS approach using queue to traverse level by level
# For each level, we store the values of the nodes in a temporary list and append it to the result list
# If the root is None, we return an empty list
# Finally, we return the result list containing the level order traversal of the binary tree
# Example Usage:
sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]