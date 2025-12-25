# https://leetcode.com/problems/maximum-width-of-binary-tree/

import collections
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append((root, 0))
        
        res = 0
        if not root: 
            return res
        # Draw the Full Binary Tree and place given tree's nodes. We see that  
        # current node's index is parent node's_index * 2  
        while q:
            # q[0] is left-most and q[-1] is right-most node of current level
            res = max(res, q[-1][1] - q[0][1] + 1)
            n = len(q)
            for i in range(n):
                tmp = q.popleft()
                node = tmp[0]
                dist = tmp[1]
                if node.left: 
                    q.append((node.left, 2*dist-1))
                if node.right: 
                    q.append((node.right, 2*dist))
        
        return res
    
# Time: O(N)
# Space: O(N)
# N is number of nodes in the binary tree
# Approach: BFS + Indexing
# We perform a level order traversal using BFS.
# For each node, we assign an index based on its position in a full binary tree.
# The left child of a node at index i is assigned index 2*i - 1
# and the right child is assigned index 2*i.
# At each level, we calculate the width as the difference between the maximum
# and minimum indices of nodes at that level plus one.
# We keep track of the maximum width encountered during the traversal and return it at the end.
# Example Usage:
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
print(sol.widthOfBinaryTree(root))  # Output: 4
