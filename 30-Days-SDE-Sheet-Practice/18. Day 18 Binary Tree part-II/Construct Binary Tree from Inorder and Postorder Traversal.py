# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        inorderIndexDict = {ch : i for i, ch in enumerate(inorder)}
        self.rootIndex = len(postorder) - 1
        
        def solve(l, r):
            if l > r: 
                return None
            
            root = TreeNode(postorder[self.rootIndex]) 
            self.rootIndex -= 1
            
            i = inorderIndexDict[root.val]
            
            # As we a approaching from end and all right side nodes of i in inorder are
            # from right sub-tree so first call solve for right then left.
            root.right = solve(i+1, r)
            root.left =  solve(l, i-1)
            
            return root
        
        return solve(0, len(inorder)-1)
    
    
# Time: O(N)
# Space: O(1)
# Where N is number of nodes in the tree.
# We are using hashmap to store inorder indices so that we can get index in O(1) time.
# The recursive stack space is not considered in space complexity.
# This code constructs a binary tree from its inorder and postorder traversal lists.
# It uses a recursive approach to build the tree by identifying the root node from the postorder list
# and partitioning the inorder list into left and right subtrees.
# The function returns the root of the constructed binary tree.
# Example usage:
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# sol = Solution()
# tree_root = sol.buildTree(inorder, postorder)
# The constructed binary tree will have the structure:
#       3
#      / \
#     9  20
#       /  \
#      15   7
# Example usage:
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
sol = Solution()
tree_root = sol.buildTree(inorder, postorder)
print(tree_root.val)  # Output: 3
print(tree_root.left.val)  # Output: 9
print(tree_root.right.val)  # Output: 20
print(tree_root.right.left.val)  # Output: 15
print(tree_root.right.right.val)  # Output: 7

