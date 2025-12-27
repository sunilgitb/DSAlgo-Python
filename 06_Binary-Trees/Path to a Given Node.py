from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self, root: Optional[TreeNode], target: int) -> List[int]:
        self.result = []
        
        def preorder(node: Optional[TreeNode], target: int, path: List[int]) -> bool:
            """
            Returns True if target found in subtree rooted at node.
            Builds path from root to target if found.
            """
            if not node:
                return False
            
            # Add current node to path
            path.append(node.val)
            
            # If target found, store path and return
            if node.val == target:
                self.result = path.copy()
                return True
            
            # Search in left subtree
            if preorder(node.left, target, path):
                return True
            
            # Search in right subtree
            if preorder(node.right, target, path):
                return True
            
            # Target not found in this subtree, backtrack
            path.pop()
            return False
        
        preorder(root, target, [])
        return self.result

# Example
print("Find Path from Root to Target Node:")
print("\nTree structure:")
print("""
        1
       / \\
      2   3
     / \\   \\
    4   5   6
   /
  7
""")

# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)

solution = Solution()

# Test 1: Target exists
target1 = 5
result1 = solution.solve(root, target1)
print(f"\nTarget node: {target1}")
print(f"Path from root to target: {result1}")

print("\nExplanation:")
print("1. Start at root 1 → add to path: [1]")
print("2. Go left to node 2 → add to path: [1, 2]")
print("3. Go left to node 4 → add to path: [1, 2, 4]")
print("4. Go left to node 7 → add to path: [1, 2, 4, 7]")
print("5. Backtrack (7 is not target, pop 7)")
print("6. Backtrack (4's left done, check right → None)")
print("7. Backtrack to node 2, go right to node 5 → add to path: [1, 2, 5]")
print("8. Found target! Store path: [1, 2, 5]")

# Test 2: Another target
print("\n" + "="*50)
target2 = 6
result2 = solution.solve(root, target2)
print(f"\nTarget node: {target2}")
print(f"Path from root to target: {result2}")

print("\nExplanation:")
print("1. Start at root 1 → [1]")
print("2. Go left to 2 → [1, 2]")
print("3. Explore left subtree (4, 7) → not found, backtrack")
print("4. Explore right subtree (5) → not found, backtrack")
print("5. Backtrack to root, go right to 3 → [1, 3]")
print("6. Go right to 6 → [1, 3, 6]")
print("7. Found target! Store path: [1, 3, 6]")

# Test 3: Target doesn't exist
print("\n" + "="*50)
target3 = 8
result3 = solution.solve(root, target3)
print(f"\nTarget node: {target3}")
print(f"Path from root to target: {result3}")
print("(Empty list since target not found)")