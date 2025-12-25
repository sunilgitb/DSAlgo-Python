# Morris Traversal Inorder
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        res = []
        cur = root
        
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if pre.right == None:
                    pre.right = cur
                    cur = cur.left
                else:
                    res.append(cur.val)
                    cur = cur.right
                
        return res
    
# Time: O(N)
# Space: O(1)

# Example Usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
sol = Solution()
print(sol.inorderTraversal(root))  # Output: [1, 3, 2]


# Morris Traversal Preorder
# https://leetcode.com/problems/binary-tree-preorder-traversal/
class Solution:
    def preorderTraversal(self, root):
        res = []
        cur = root
        
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if pre.right == None:
                    pre.right = cur
                    res.append(cur.val)
                    cur = cur.left
                else:
                    cur = cur.right
                
        return res
    
# Time: O(N)
# Space: O(1)
# Example 2 Usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
sol = Solution()
print(sol.preorderTraversal(root))  # Output: [1, 2, 3]
