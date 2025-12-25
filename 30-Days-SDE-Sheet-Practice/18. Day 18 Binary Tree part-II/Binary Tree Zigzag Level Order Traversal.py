# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if not root: 
            return res
        zigzag = True
        q = collections.deque() # queue for BFS
        q.append(root)
        
        while q:
            n = len(q)
            nodesOfThisLevel = []
            
            for i in range(n):
                node = q.popleft()
                nodesOfThisLevel.append(node.val)
                
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
                    
            if zigzag:
                res.append(nodesOfThisLevel)
                zigzag = False
            else:
                res.append(nodesOfThisLevel[::-1])
                zigzag = True
        
        return res
    
# Time: O(N)
# Space: O(N)

# Example usage:
# Constructing the binary tree:
#         3
#        / \
#       9  20
#          /  \
#         15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print(solution.zigzagLevelOrder(root))  # Output: [[3], [20, 9], [15, 7]]
