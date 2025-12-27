class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    """
    Returns all three tree traversals: [inorder, preorder, postorder]
    """
    result = []
    
    # 1. Inorder Traversal (Left → Root → Right)
    inorder_result = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        inorder_result.append(root.data)
        inorder(root.right)
    inorder(root)
    result.append(inorder_result)
    
    # 2. Preorder Traversal (Root → Left → Right)
    preorder_result = []
    def preorder(root):
        if not root:
            return
        preorder_result.append(root.data)
        preorder(root.left)
        preorder(root.right)
    preorder(root)
    result.append(preorder_result)
    
    # 3. Postorder Traversal (Left → Right → Root)
    postorder_result = []
    def postorder(root):
        if not root:
            return
        postorder(root.left)
        postorder(root.right)
        postorder_result.append(root.data)
    postorder(root)
    result.append(postorder_result)
    
    return result

# Example
print("Tree Traversals (Inorder, Preorder, Postorder):")
print("\nTree structure:")
print("""
        1
       / \\
      2   3
     / \\
    4   5
""")

# Build the tree
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

# Get all traversals
traversals = getTreeTraversal(root)
inorder_traversal, preorder_traversal, postorder_traversal = traversals

print(f"\nInorder traversal (Left → Root → Right): {inorder_traversal}")
print(f"Preorder traversal (Root → Left → Right): {preorder_traversal}")
print(f"Postorder traversal (Left → Right → Root): {postorder_traversal}")

print("\nStep-by-step explanations:")

print("\n1. Inorder Traversal (Left → Root → Right):")
print("   - Start at root 1")
print("   - Traverse left subtree (2, 4, 5)")
print("   - Visit 4 (leftmost)")
print("   - Visit 2 (root of left subtree)")
print("   - Visit 5 (right of 2)")
print("   - Visit 1 (main root)")
print("   - Traverse right subtree (3)")
print("   - Visit 3")
print("   Result: 4 → 2 → 5 → 1 → 3")

print("\n2. Preorder Traversal (Root → Left → Right):")
print("   - Visit root 1 first")
print("   - Traverse left subtree: visit 2, then 4, then 5")
print("   - Traverse right subtree: visit 3")
print("   Result: 1 → 2 → 4 → 5 → 3")

print("\n3. Postorder Traversal (Left → Right → Root):")
print("   - Traverse left subtree: visit 4, then 5, then 2")
print("   - Traverse right subtree: visit 3")
print("   - Visit root 1 last")
print("   Result: 4 → 5 → 2 → 3 → 1")

print("\nMemory aid:")
print("  IN-order:   Traverse IN between left and right")
print("  PRE-order:  Process node PRE (before) children")
print("  POST-order: Process node POST (after) children")

print("\nCommon uses:")
print("  • Inorder:   BST gives sorted order")
print("  • Preorder:  Used for copying trees, prefix expressions")
print("  • Postorder: Used for deleting trees, postfix expressions")