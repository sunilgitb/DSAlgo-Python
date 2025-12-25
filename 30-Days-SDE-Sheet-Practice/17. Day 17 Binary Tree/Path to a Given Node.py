# https://www.interviewbit.com/problems/path-to-given-node/

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self, A, B):
        self.res = []

        def preorder(root, target, path):
            if not root: 
                return
            if root.val == target:
                path += [root.val]
                self.res = path
                return
            preorder(root.left, target, path + [root.val])
            preorder(root.right, target, path + [root.val])
        
        preorder(A, B, [])
        return self.res

# Time: O(N)
# Space: O(1)

# Example usage:
# Constructing the binary tree:
#         1
#        / \
#       2   3
#      / \   \
#     4    5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
solution = Solution()
print(solution.solve(root, 5))  # Output: [1, 2, 5]

