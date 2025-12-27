from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closest_k_values(self, root: TreeNode, target: float, k: int) -> List[int]:
        q = deque()
        
        def inorder_dfs(node):
            if not node: 
                return
            
            # Traverse left subtree
            inorder_dfs(node.left)
            
            # Process current node
            if len(q) < k:
                # If we haven't collected k values yet, just add
                q.append(node.val)
            else:
                # If we have k values, check if current node is closer than farthest in queue
                if abs(q[0] - target) > abs(node.val - target):
                    # Current node is closer, remove farthest and add current
                    q.popleft()
                    q.append(node.val)
                else:
                    # Since inorder gives sorted values, if current node is farther,
                    # all remaining nodes will be even farther
                    return
            
            # Traverse right subtree
            inorder_dfs(node.right)
        
        inorder_dfs(root)
        return list(q)

# Example
print("Find K Closest Values in BST:")
print("Target: 3.8, k: 2")
print("\nTree structure:")
print("""
        4
       / \\
      2   5
     / \\
    1   3
""")

# Build the tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
result = solution.closest_k_values(root, target=3.8, k=2)

print(f"\n{k} closest values to {target}: {result}")

print("\nExplanation:")
print("Inorder traversal gives sorted values: [1, 2, 3, 4, 5]")
print("Distances to target 3.8:")
print("1: |3.8 - 1| = 2.8")
print("2: |3.8 - 2| = 1.8")
print("3: |3.8 - 3| = 0.8  ← closest")
print("4: |3.8 - 4| = 0.2  ← closest")
print("5: |3.8 - 5| = 1.2")
print(f"\n2 closest values: {result}")