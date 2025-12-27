from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0, 0]  # [rob_this, skip_this]

            left = dfs(node.left)
            right = dfs(node.right)

            rob_this = node.val + left[1] + right[1]
            skip_this = max(left) + max(right)

            return [rob_this, skip_this]

        return max(dfs(root))


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1:
    #      3
    #     / \
    #    2   3
    #     \   \
    #      3   1
    root1 = TreeNode(3)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(1)

    print(sol.rob(root1))
    # Output: 7

    # Example 2:
    #      3
    #     / \
    #    4   5
    #   / \   \
    #  1   3   1
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(1)

    print(sol.rob(root2))
    # Output: 9
