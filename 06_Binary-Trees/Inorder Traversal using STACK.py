from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        
        while True:
            # Reach the leftmost node of the current node
            if current:
                stack.append(current)
                current = current.left
            
            # Backtrack from the empty subtree and visit the node
            elif stack:
                current = stack.pop()
                result.append(current.val)  # Visit the node
                current = current.right      # Move to right subtree
            
            # Done
            else:
                break
        
        return result

# Example
print("Binary Tree Inorder Traversal (Iterative):")
print("\nTree structure:")
print("""
        1
         \\
          2
         /
        3
""")

# Build the tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
result = solution.inorderTraversal(root)

print(f"\nInorder traversal: {result}")

print("\nStep-by-step execution:")
print("1. Start at root (1)")
print("2. Go left from 1 → None, pop from stack")
print("3. Visit node 1, append to result: [1]")
print("4. Go right from 1 to node 2")
print("5. Go left from 2 to node 3, push 2 to stack, then 3 to stack")
print("6. Go left from 3 → None, pop from stack")
print("7. Visit node 3, append to result: [1, 3]")
print("8. Go right from 3 → None, pop from stack")
print("9. Visit node 2, append to result: [1, 3, 2]")
print("10. Go right from 2 → None, stack empty → Done")

print("\nVisual traversal order:")
print("""
    1
     \\
      2
     /
    3
    
Traversal: 1 → 3 → 2
""")