# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        cur = root
        while True:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
            else:
                break
        return ans


# Example usage:
# Constructing a binary tree:
#       1
#        \
#         2
#        / \
#       3   4
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
solution = Solution()
print(solution.inorderTraversal(root))  # Output: [1, 3, 2, 4]
