# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def buildTree(self, preorder, inorder):
        # Map value -> index in inorder for O(1) lookup
        inorderIndexDict = {val: idx for idx, val in enumerate(inorder)}
        self.rootIndex = 0  # pointer for preorder traversal
        
        def solve(l, r):
            if l > r:
                return None
            
            # Pick current root from preorder
            root = TreeNode(preorder[self.rootIndex])
            self.rootIndex += 1
            
            # Find root position in inorder
            mid = inorderIndexDict[root.val]
            
            # Build left subtree first (important!)
            root.left = solve(l, mid - 1)
            root.right = solve(mid + 1, r)
            
            return root
        
        return solve(0, len(inorder) - 1)
    

# ---------------- DRIVER CODE ----------------

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

solution = Solution()
tree = solution.buildTree(preorder, inorder)

# Preorder print of constructed tree
def print_tree(node):
    if not node:
        return
    print(node.val, end=' ')
    print_tree(node.left)
    print_tree(node.right)

print_tree(tree)
# Expected Output: 3 9 20 15 7
