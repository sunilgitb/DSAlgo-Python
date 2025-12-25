# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1/
# https://youtu.be/0ca1nvR0be4

class Solution:
    def printBoundaryView(self, root):
        
        def addLeftBoundary(root, res):
            ans = []
            cur = root
            while cur:
                ans.append(cur.data)
                if cur.left: 
                    cur = cur.left
                else: 
                    cur = cur.right
            res += ans[:-1]

        def addLeafNodes(root, res):
            if not root: 
                return
            if not root.left and not root.right: 
                res.append(root.data)
            addLeafNodes(root.left, res)
            addLeafNodes(root.right, res)

        def addRightBoundary(root, res):
            ans = []
            cur = root
            while cur:
                ans.append(cur.data)
                if cur.right: 
                    cur = cur.right
                else: 
                    cur = cur.left
            res += ans[:-1][::-1]
            
        res = []
        if not root: return res
        res.append(root.data)
        if not root.left and not root.right: return res
        addLeftBoundary(root.left, res)
        addLeafNodes(root, res)
        addRightBoundary(root.right, res)
        return res
        
        
# Time: O(N)
# Space: O(N)

# Example usage
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    # Example tree:
    #           1
    #         /   \
    #        2     3
    #       / \   / \
    #      4  5  6   7
    root = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(5)),
                    TreeNode(3, TreeNode(6), TreeNode(7)))

    sol = Solution()
    print("Boundary traversal:", sol.printBoundaryView(root))  # [1, 2, 4, 5, 6, 7, 3]

    # Single node
    single = TreeNode(1)
    print("Single node boundary:", sol.printBoundaryView(single))  # [1]
