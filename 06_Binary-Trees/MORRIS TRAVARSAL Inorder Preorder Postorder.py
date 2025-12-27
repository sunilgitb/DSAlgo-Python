from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. Morris Inorder Traversal
class SolutionInorder:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = root
        
        while current:
            if not current.left:
                # No left child, visit current node
                result.append(current.val)
                current = current.right
            else:
                # Find the inorder predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    # Create temporary link to current
                    predecessor.right = current
                    current = current.left
                else:
                    # Remove temporary link and visit current
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right
        
        return result

# 2. Morris Preorder Traversal
class SolutionPreorder:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = root
        
        while current:
            if not current.left:
                # No left child, visit current node
                result.append(current.val)
                current = current.right
            else:
                # Find the inorder predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    # Create temporary link and visit current node
                    predecessor.right = current
                    result.append(current.val)
                    current = current.left
                else:
                    # Remove temporary link
                    predecessor.right = None
                    current = current.right
        
        return result

# 3. Morris Postorder Traversal
class SolutionPostorder:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = root
        
        while current:
            if not current.right:
                # No right child, visit current node
                result.append(current.val)
                current = current.left
            else:
                # Find the inorder successor in right subtree
                successor = current.right
                while successor.left and successor.left != current:
                    successor = successor.left
                
                if not successor.left:
                    # Create temporary link and visit current node
                    successor.left = current
                    result.append(current.val)
                    current = current.right
                else:
                    # Remove temporary link
                    successor.left = None
                    current = current.left
        
        # Reverse the result to get postorder
        result.reverse()
        return result

# Example tree
print("Morris Traversal Examples:")
print("\nTree structure:")
print("""
        1
       / \\
      2   3
     / \\
    4   5
""")

# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 1. Inorder Traversal
print("\n1. Morris Inorder Traversal:")
inorder_solution = SolutionInorder()
inorder_result = inorder_solution.inorderTraversal(root)
print(f"Result: {inorder_result}")
print("Expected: [4, 2, 5, 1, 3] (Left → Root → Right)")
print(f"Correct: {inorder_result == [4, 2, 5, 1, 3]}")

# 2. Preorder Traversal
print("\n2. Morris Preorder Traversal:")
preorder_solution = SolutionPreorder()
preorder_result = preorder_solution.preorderTraversal(root)
print(f"Result: {preorder_result}")
print("Expected: [1, 2, 4, 5, 3] (Root → Left → Right)")
print(f"Correct: {preorder_result == [1, 2, 4, 5, 3]}")

# 3. Postorder Traversal
print("\n3. Morris Postorder Traversal:")
postorder_solution = SolutionPostorder()
postorder_result = postorder_solution.postorderTraversal(root)
print(f"Result: {postorder_result}")
print("Expected: [4, 5, 2, 3, 1] (Left → Right → Root)")
print(f"Correct: {postorder_result == [4, 5, 2, 3, 1]}")

print("\nKey Morris Traversal Concepts:")
print("1. Uses threaded binary trees (temporary links)")
print("2. O(1) extra space (no stack/recursion)")
print("3. O(N) time complexity (visits each node 2-3 times)")
print("4. Modifies tree structure temporarily, restores it")
print("\nVisual of temporary links (for inorder):")
print("""
        1
       / \\
      2   3
     / \\
    4   5
     \\
      1 (temporary link from 4 to 1)
""")