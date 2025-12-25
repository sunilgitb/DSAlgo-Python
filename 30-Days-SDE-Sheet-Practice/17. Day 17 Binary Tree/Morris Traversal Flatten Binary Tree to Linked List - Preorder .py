# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Morris Traversal Flatten Binary Tree to Linked List - Preorder 

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur.right
                    cur.right = cur.left
                    cur.left = None
                    cur = cur.right
                else:
                    cur = cur.right

                    
# Time: O(N)
# Space: O(1) ; as we have not used any extra space only changed the links b/w nodes
# N = number of nodes in the binary tree
# Approach: Morris Traversal
# 1. Initialize cur as root
# 2. While cur is not None:
#    a. If cur.left is None, move to cur.right
#    b. Else, find the predecessor (pre) of cur in the left subtree
#       i. If pre.right is None, set pre.right to cur.right, move cur.left to cur.right, set cur.left to None, and move cur to cur.right
#       ii. Else, move cur to cur.right
# 3. The tree is now flattened 
# Example Usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
sol = Solution()
sol.flatten(root)
print(root.right.val)  # Output: 2
print(root.right.right.val)  # Output: 3
print(root.right.right.right.val)  # Output: 4  print(root.right.right.right.right.val)  # Output: 5
print(root.right.right.right.right.right.val)  # Output: 6

# The tree is now flattened to a linked list in preorder traversal order

