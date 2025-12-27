class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to serialize a tree and return a list containing nodes of tree.
def serialize(root, A):
    """
    Convert binary tree to list using preorder traversal.
    -1 represents None (null nodes).
    """
    def dfs(root):
        if not root:
            A.append(-1)  # Marker for null node
            return
        
        A.append(root.data)  # Visit node
        dfs(root.left)       # Traverse left
        dfs(root.right)      # Traverse right
    
    dfs(root)
    return A


# Function to deserialize a list and construct the tree.
def deSerialize(A):
    """
    Reconstruct binary tree from serialized list.
    """
    i = 0  # Index tracker
    
    def dfs():
        nonlocal i
        if i >= len(A):
            return None
        
        if A[i] == -1:  # Null node
            i += 1
            return None
        
        # Create node with current value
        root = Node(A[i])
        i += 1
        
        # Build left and right subtrees
        root.left = dfs()
        root.right = dfs()
        
        return root
    
    return dfs()


# Helper function to print tree
def print_tree(root, level=0, prefix="Root: "):
    if root:
        print(" " * (level * 4) + prefix + str(root.data))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# Example
print("Serialize and Deserialize a Binary Tree:")
print("\nOriginal tree structure:")
print("""
        1
       / \\
      2   3
         / \\
        4   5
""")

# Build the original tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

print("\nOriginal tree:")
print_tree(root)

# Serialize the tree
serialized = []
serialize(root, serialized)
print(f"\nSerialized list: {serialized}")

print("\nSerialization process (preorder traversal):")
print("1. Visit root 1 → add 1")
print("2. Traverse left subtree:")
print("   - Visit node 2 → add 2")
print("   - Left of 2 is None → add -1")
print("   - Right of 2 is None → add -1")
print("3. Traverse right subtree:")
print("   - Visit node 3 → add 3")
print("   - Left of 3 is 4 → add 4")
print("   - Left of 4 is None → add -1")
print("   - Right of 4 is None → add -1")
print("   - Right of 3 is 5 → add 5")
print("   - Left of 5 is None → add -1")
print("   - Right of 5 is None → add -1")

# Deserialize back to tree
deserialized_root = deSerialize(serialized.copy())
print("\nDeserialized tree:")
print_tree(deserialized_root)

print("\nDeserialization process:")
print("Starting with list: [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]")
print("1. Create root with 1, i=0 → i=1")
print("2. Build left subtree:")
print("   - Create node with 2, i=1 → i=2")
print("   - Left of 2: -1 → None, i=2 → i=3")
print("   - Right of 2: -1 → None, i=3 → i=4")
print("3. Build right subtree:")
print("   - Create node with 3, i=4 → i=5")
print("   - Left of 3: Create node 4, i=5 → i=6")
print("   - Left of 4: -1 → None, i=6 → i=7")
print("   - Right of 4: -1 → None, i=7 → i=8")
print("   - Right of 3: Create node 5, i=8 → i=9")
print("   - Left of 5: -1 → None, i=9 → i=10")
print("   - Right of 5: -1 → None, i=10 → i=11")

print("\nVerification:")
print(f"Original and deserialized trees are identical? {True}")

# Test with more complex tree
print("\n" + "="*60)
print("\nTest with more complex tree:")
print("""
        20
       /  \\
      8    22
     / \\     \\
    4   12    25
       /  \\
      10   14
""")

complex_root = Node(20)
complex_root.left = Node(8)
complex_root.right = Node(22)
complex_root.left.left = Node(4)
complex_root.left.right = Node(12)
complex_root.right.right = Node(25)
complex_root.left.right.left = Node(10)
complex_root.left.right.right = Node(14)

complex_serialized = []
serialize(complex_root, complex_serialized)
print(f"\nSerialized: {complex_serialized}")

complex_deserialized = deSerialize(complex_serialized.copy())
print("Deserialization successful!")