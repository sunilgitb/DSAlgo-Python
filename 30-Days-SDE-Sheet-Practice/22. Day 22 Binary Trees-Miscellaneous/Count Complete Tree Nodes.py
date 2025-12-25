# https://leetcode.com/problems/count-complete-tree-nodes/
# https://youtu.be/u-yWemKGWO0
''' 
Only traversing along the left and right boundary. 
If both left and right height are equal then
the bottom level would be full from left to right and total no. of nodes in that subtree
is 2^h - 1. 

If left and right height are not equal then add +1 for current root and go to left child 
and right child. 
'''

# https://leetcode.com/problems/count-complete-tree-nodes/
# https://youtu.be/u-yWemKGWO0

class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        
        leftHeight = self.getLeftHeight(root)
        rightHeight = self.getRightHeight(root)
        
        if leftHeight == rightHeight:
            return 2 ** leftHeight - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def getLeftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def getRightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height


# Height = H = log(n)
# Time: O(log² n)
# Space: O(log n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Construct Complete Binary Tree
#        1
#       / \
#      2   3
#     / \  /
#    4  5 6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

solution = Solution()
print(solution.countNodes(root))
# Expected Output: 6

    
# Height = H = log(n) where n = total number of nodes
# Time: O(H * H) = O(log(n)^2) = O(Log^2 n)
# Auxiliary Space: O(H) = O(log(n))
    