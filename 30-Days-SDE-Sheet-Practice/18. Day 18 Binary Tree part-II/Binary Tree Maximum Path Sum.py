# https://www.youtube.com/watch?v=Osz-Vwer6rw&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=48
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return
        self.res = root.val  
        
        def solve(root):
            # Base case
            if not root: 
                return 0
             
            # l and r store maximum path sum going through left and right child of root respectively
            l = solve(root.left)
            r = solve(root.right)
            
            # Max path for parent call of root. This path must include at most one child of root
            temp = max(root.val + max(l, r), root.val)
            # ans  represents the sum when the node under consideration is the root of the maxSum path and no ancestor of root are there in max sum path
            ans = max(temp, root.val + l + r)
            self.res = max(self.res, ans) # max across the whole tree
            
            return temp # for considering other subtrees also
        
        solve(root)
        return self.res
    
    
# Time Complexity: O(n) where n is number of nodes in Binary Tree.

# Space Complexity: O(h) where h is height of the tree. This space is required for recursion stack.
# In case of skewed tree, space complexity can be O(n).
# Auxiliary Space: O(1)
# No extra data structure is used in the algorithm.
# Only constant space is used.
# Thus, auxiliary space is O(1).
# Example Usage:
# Constructing the binary tree:
#        -10
#        /  \
#       9   20
#          /  \
#         15   7
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print(solution.maxPathSum(root))  # Output: 42

# The maximum path sum is 15 + 20 + 7 = 42
    
    