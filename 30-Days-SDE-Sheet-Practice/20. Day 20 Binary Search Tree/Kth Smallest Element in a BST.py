# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional

class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = root.val
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.k -= 1
            if self.k == 0: 
                self.res = root.val
            inorder(root.right)
        
        inorder(root)
        return self.res

# Time: O(N)
# Space: O(1)


if __name__ == "__main__":
    # Local TreeNode definition for example (matches LeetCode TreeNode)
    

    def inorder(root, out):
        if not root: return
        inorder(root.left, out)
        out.append(root.val)
        inorder(root.right, out)

    # Example tree:
    #    3
    #   / \
    #  1   4
    #   \
    #    2
    n2 = TreeNode(2)
    n1 = TreeNode(1, None, n2)
    n4 = TreeNode(4)
    root = TreeNode(3, n1, n4)

    sol = Solution()
    for k in [1, 2, 3, 4]:
        print(f"k={k} ->", sol.kthSmallest(root, k))

    # Expected:
    # k=1 -> 1
    # k=2 -> 2
    # k=3 -> 3
    # k=4 -> 4

# 