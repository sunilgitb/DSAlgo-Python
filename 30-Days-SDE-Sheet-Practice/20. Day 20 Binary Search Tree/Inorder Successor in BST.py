# https://www.lintcode.com/problem/448/description
# https://leetcode.com/problems/inorder-successor-in-bst/   (Premium)
from typing import Optional
class Solution:
    def inorderSuccessor(self, root, p):
        res = None
        while root:
            if root.val > p.val:
                res = root  # current root is greater so it can be a successor. 
                root = root.left  # check if lesser root exit or not
            else:
                root = root.right  # current root is lesser than p try for greater roots

        return res

# Time: O(log(N))
# Space: O(1)


if __name__ == "__main__":
    # Local TreeNode definition for example (matches LeetCode TreeNode)
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # Build example BST:
    #        5
    #       / \
    #      3   7
    #     / \   \
    #    2   4   8
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n2, n4)
    n8 = TreeNode(8)
    n7 = TreeNode(7, None, n8)
    n5 = TreeNode(5, n3, n7)

    # Example: successor of node with val 4 is 5
    p = n4
    succ = Solution().inorderSuccessor(n5, p)
    print(f"Inorder successor of {p.val}:", succ.val if succ else None)

    # Another example: successor of node 7 is 8
    p2 = n7
    succ2 = Solution().inorderSuccessor(n5, p2)
    print(f"Inorder successor of {p2.val}:", succ2.val if succ2 else None)

