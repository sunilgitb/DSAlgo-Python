# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        
        def dfs(root):
            # returns:
            # (isBST, sum, minValue, maxValue)
            
            if not root:
                return True, 0, float("inf"), float("-inf")
            
            lres, lsum, lmin, lmax = dfs(root.left)
            rres, rsum, rmin, rmax = dfs(root.right)
            
            if lres and rres and lmax < root.val < rmin:
                curr_sum = root.val + lsum + rsum
                self.result = max(self.result, curr_sum)
                return True, curr_sum, min(root.val, lmin), max(root.val, rmax)
            else:
                # Returning False ensures this subtree is ignored
                return False, 0, 0, 0 
               
        self.result = 0
        dfs(root)
        return self.result


# Time Complexity: O(N)
# Space Complexity: O(1)  (excluding recursion stack)
# Construct Binary Tree
#        1
#       / \
#      4   3
#     / \   \
#    2   4   5
#           / \
#          4   6

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(3)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right.right = TreeNode(5)
root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(6)

solution = Solution()
print(solution.maxSumBST(root))
# Output: 18
