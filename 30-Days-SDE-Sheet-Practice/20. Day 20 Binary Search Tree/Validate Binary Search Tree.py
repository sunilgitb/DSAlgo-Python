# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        
        def check(mini, node, maxi):
            if not node:
                return True
            
            return (
                mini < node.val < maxi and
                check(mini, node.left, node.val) and
                check(node.val, node.right, maxi)
            )
        
        return check(-2**31 - 1, root, 2**31)

solution = Solution()

# Example 1: Valid BST
#        2
#       / \
#      1   3

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print(solution.isValidBST(root1))  # Output: True


# Example 2: Invalid BST
#        5
#       / \
#      1   4
#         / \
#        3   6

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print(solution.isValidBST(root2))  # Output: False
