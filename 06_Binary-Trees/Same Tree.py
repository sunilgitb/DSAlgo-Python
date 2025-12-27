from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are identical.
        
        Two binary trees are considered the same if they are structurally identical
        and the nodes have the same value.
        """
        # Both trees are empty
        if not p and not q:
            return True
        
        # One tree is empty, other is not
        if not p or not q:
            return False
        
        # Check current node values and recursively check subtrees
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

# Example
print("Check if Two Binary Trees are Identical:")
print("\nTree 1 and Tree 2 (identical):")
print("""
    Tree 1:      Tree 2:
        1            1
       / \\          / \\
      2   3        2   3
""")

# Build identical trees
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

solution = Solution()
result1 = solution.isSameTree(p, q)

print(f"\nAre Tree 1 and Tree 2 identical? {result1}")

print("\nComparison process:")
print("1. Compare root nodes: 1 == 1 ✓")
print("2. Compare left subtrees:")
print("   - Compare root: 2 == 2 ✓")
print("   - Compare left children: None == None ✓")
print("   - Compare right children: None == None ✓")
print("3. Compare right subtrees:")
print("   - Compare root: 3 == 3 ✓")
print("   - Compare left children: None == None ✓")
print("   - Compare right children: None == None ✓")
print("All comparisons pass → Trees are identical")

print("\n" + "="*50)
print("\nTree 3 and Tree 4 (different values):")
print("""
    Tree 3:      Tree 4:
        1            1
       / \\          / \\
      2   3        2   4
""")

# Build trees with different values
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)

s = TreeNode(1)
s.left = TreeNode(2)
s.right = TreeNode(4)  # Different value

result2 = solution.isSameTree(r, s)
print(f"\nAre Tree 3 and Tree 4 identical? {result2}")

print("\nComparison process:")
print("1. Compare root nodes: 1 == 1 ✓")
print("2. Compare left subtrees: 2 == 2 ✓")
print("3. Compare right subtrees: 3 == 4 ✗")
print("Value mismatch → Trees are not identical")

print("\n" + "="*50)
print("\nTree 5 and Tree 6 (different structure):")
print("""
    Tree 5:      Tree 6:
        1            1
       /            / \\
      2            2   3
""")

# Build trees with different structure
t = TreeNode(1)
t.left = TreeNode(2)

u = TreeNode(1)
u.left = TreeNode(2)
u.right = TreeNode(3)

result3 = solution.isSameTree(t, u)
print(f"\nAre Tree 5 and Tree 6 identical? {result3}")

print("\nComparison process:")
print("1. Compare root nodes: 1 == 1 ✓")
print("2. Compare left subtrees: 2 == 2 ✓")
print("3. Compare right subtrees: None vs TreeNode(3)")
print("   One is None, other is not → Trees are not identical")