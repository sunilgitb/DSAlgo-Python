class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def convertToDLL(root):
    # return the head of the DLL and remove those node from the tree as well.
    notLeaves = set()
    
    def isLeaves(root):
        if not root.left and not root.right and root not in notLeaves: 
            return True
        return False
    
    def addToDDL(node):
        nonlocal cur
        cur.right = node
        node.left = cur
        cur = cur.right

    dummy = Node(-1)
    cur = dummy
    
    def dfs(root):
        nonlocal cur
        if not root: 
            return
        
        dfs(root.left)
        
        # Check left child
        if root.left and isLeaves(root.left):
            node = root.left
            root.left = None  # Remove from tree
            addToDDL(node)    # Add to DLL
            notLeaves.add(root)
        
        # Check right child
        if root.right and isLeaves(root.right):
            node = root.right
            root.right = None  # Remove from tree
            addToDDL(node)     # Add to DLL
            notLeaves.add(root)
        
        dfs(root.right)
    
    dfs(root)
    
    # Extract the actual DLL from dummy node
    res = dummy.right
    if res:
        res.left = None
    dummy.right = None
    
    return res

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

# Helper function to print DLL
def print_dll(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.right
    return result

# Example
print("Extract leaves from binary tree to DLL:")
print("Original tree structure:")
print("""
        1
       / \\
      2   3
     / \\   \\
    4   5   6
   / \\
  7   8
""")

# Build the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(8)

print("\nOriginal tree:")
print_tree(root)

print("\nExtracting leaves to DLL...")
dll_head = convertToDLL(root)

print(f"\nDoubly Linked List of leaves: {print_dll(dll_head)}")

print("\nTree after removing leaves:")
print_tree(root)

print("\nExplanation:")
print("1. Leaves extracted: 7, 8, 5, 6")
print("2. Tree after removal: Only nodes 1, 2, 3, 4 remain")
print("3. DLL created: 7 <-> 8 <-> 5 <-> 6")