# https://leetcode.com/problems/search-in-a-binary-search-tree/

from typing import Optional

# Local TreeNode definition for example (matches LeetCode TreeNode)
class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: 
            return 
        elif root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return root


if __name__ == "__main__":
    

    # Build example BST:
    #      4
    #     / \
    #    2   7
    #   / \
    #  1   3
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n1, n3)
    n7 = TreeNode(7)
    root = TreeNode(4, n2, n7)

    sol = Solution()
    # Search for existing value
    res = sol.searchBST(root, 2)
    print(f"Search 2 ->", res.val if res else None)
    # Search for non-existing value
    res2 = sol.searchBST(root, 5)
    print(f"Search 5 ->", res2.val if res2 else None)