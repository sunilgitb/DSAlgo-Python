from typing import List

# Approach 1: Backtracking/DFS
class Solution1:
    def verify_preorder(self, preorder: List[int]) -> bool:
        i = 0
        
        def dfs(min_val, max_val):
            nonlocal i
            if i == len(preorder):
                return
            if preorder[i] < min_val or preorder[i] > max_val:
                return
            
            val = preorder[i]
            i += 1
            dfs(min_val, val)      # left subtree
            dfs(val, max_val)      # right subtree
        
        dfs(float('-inf'), float('inf'))
        return i == len(preorder)

# Approach 2: Stack
class Solution2:
    def verify_preorder(self, preorder: List[int]) -> bool:
        low = float('-inf')
        stack = []
        
        for p in preorder:
            if p < low:
                return False
            while stack and stack[-1] < p:
                low = stack.pop()
            stack.append(p)
        
        return True

# Example
print("Verify Preorder Sequence in BST:")
print("\nTest sequence: [5, 2, 1, 3, 6]")

preorder_sequence = [5, 2, 1, 3, 6]

print("\nApproach 1 (Backtracking/DFS) Result:")
sol1 = Solution1()
result1 = sol1.verify_preorder(preorder_sequence)
print(f"Is valid preorder? {result1}")

print("\nApproach 2 (Stack) Result:")
sol2 = Solution2()
result2 = sol2.verify_preorder(preorder_sequence)
print(f"Is valid preorder? {result2}")

print("\nTree representation of valid preorder [5, 2, 1, 3, 6]:")
print("""
        5
       / \\
      2   6
     / \\
    1   3
""")

print("\nExplanation of preorder [5, 2, 1, 3, 6]:")
print("1. Root: 5")
print("2. Left subtree of 5: [2, 1, 3]")
print("   - Root: 2")
print("   - Left of 2: 1")
print("   - Right of 2: 3")
print("3. Right subtree of 5: [6]")
print("   - Root: 6")
print("Preorder traversal matches: 5 → 2 → 1 → 3 → 6 ✓")