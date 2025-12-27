from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Method 1: Most Efficient using dictionary
class Solution1:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        preInd = {v:i for i, v in enumerate(preorder)}
        def solve(l, r, postorder):
            if l == r: return None
            if r-l == 1: return TreeNode(postorder.pop())
            root = TreeNode(postorder.pop())
            i = preInd[postorder[-1]]
            root.right = solve(i, r, postorder)
            root.left = solve(l+1, i, postorder)
            return root
        
        return solve(0, len(preorder), postorder)

# Method 2: Using index tracking
class Solution2:
    def constructFromPrePost(self, preorder, postorder):
        self.preIndex = 0
        def dfs(postStart, postEnd):
            if postStart > postEnd or self.preIndex >= len(preorder): 
                return None
            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1
            if postStart == postEnd or self.preIndex >= len(preorder): 
                return root
            postIndex = postorder.index(preorder[self.preIndex])
            root.left = dfs(postStart, postIndex)
            root.right = dfs(postIndex+1, postEnd-1)
            return root
        
        return dfs(0, len(preorder)-1)

# Method 3: Direct list manipulation
class Solution3:
    def constructFromPrePost(self, preorder, postorder):
        def dfs(preorder, postorder):
            if postorder:
                if len(postorder) == 1:
                    return TreeNode(preorder.pop(0))
                root = TreeNode(preorder.pop(0))
                i = postorder.index(preorder[0])
                root.left = dfs(preorder, postorder[:i+1])
                root.right = dfs(preorder, postorder[i+1:-1])
                return root
        return dfs(preorder, postorder)

# Helper function for traversals
def preorder_traversal(root):
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

def postorder_traversal(root):
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val] if root else []

# Test data
preorder = [1, 2, 4, 5, 3, 6, 7]
postorder1 = [4, 5, 2, 6, 7, 3, 1]
postorder2 = [4, 5, 2, 6, 7, 3, 1]
postorder3 = [4, 5, 2, 6, 7, 3, 1]

# Method 1 Output
print("Method 1 Output (Most Efficient):")
print("-" * 40)
sol1 = Solution1()
tree1 = sol1.constructFromPrePost(preorder, postorder1.copy())
print(f"Reconstructed tree preorder: {preorder_traversal(tree1)}")
print(f"Matches original: {preorder_traversal(tree1) == preorder}")
print()

# Method 2 Output
print("Method 2 Output (Index Tracking):")
print("-" * 40)
sol2 = Solution2()
tree2 = sol2.constructFromPrePost(preorder, postorder2)
print(f"Reconstructed tree preorder: {preorder_traversal(tree2)}")
print(f"Matches original: {preorder_traversal(tree2) == preorder}")
print()

# Method 3 Output
print("Method 3 Output (Direct List Manipulation):")
print("-" * 40)
sol3 = Solution3()
tree3 = sol3.constructFromPrePost(preorder.copy(), postorder3)
print(f"Reconstructed tree preorder: {preorder_traversal(tree3)}")
print(f"Matches original: {preorder_traversal(tree3) == preorder}")