# https://leetcode.com/problems/balanced-binary-tree/

'''
class Solution:
    def isBalanced(self, root):
        if not root: return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))

# Time: O(N^2)
# Space: O(1)
'''


# https://youtu.be/QfJsau0ItOY

class Solution:
    def isBalanced(self, root):
        
        def dfs(root):
            if not root: 
                return True, 0  
            
            lb, lh = dfs(root.left)      
            rb, rh = dfs(root.right)
            
            b = abs(lh - rh) <= 1 and lb and rb

            return b, 1 + max(lh, rh)
        
        b, h = dfs(root)
        return b
    
# Time: O(N)
# Space: O(1)

# Example usage
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    # Balanced tree:       1
    #                     /   \
    #                    2     3
    root_bal = TreeNode(1, TreeNode(2), TreeNode(3))

    # Unbalanced tree:    1
    #                      \
    #                       2
    #                        \
    #                         3
    root_unbal = TreeNode(1, TreeNode(2, TreeNode(3)))

    sol = Solution()
    print("Balanced tree:", sol.isBalanced(root_bal))   # True
    print("Unbalanced tree:", sol.isBalanced(root_unbal)) # False