class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    # Method 1: O(N^2) approach
    def largestBst_method1(self, root):
        def isBST(root, min_val, max_val):
            if not root:
                return True
            if root.data <= min_val or root.data >= max_val:
                return False
            return (isBST(root.left, min_val, root.data) and 
                    isBST(root.right, root.data, max_val))
        
        def sizeOfBST(root):
            if not root:
                return 0
            return sizeOfBST(root.left) + 1 + sizeOfBST(root.right)
        
        if isBST(root, float("-inf"), float("inf")):
            return sizeOfBST(root)
        return max(self.largestBst_method1(root.left), 
                   self.largestBst_method1(root.right))
    
    # Method 2: O(N) approach
    def largestBst(self, root):
        def solveLargestBST(root):
            if not root:
                return (float("-inf"), float("inf"), 0, True)
            if not root.left and not root.right:
                return (root.data, root.data, 1, True)
            
            l = solveLargestBST(root.left)
            r = solveLargestBST(root.right)
            
            if l[3] and r[3] and l[1] < root.data < r[0]:
                return (max(root.data, r[0]), min(root.data, l[1]), 1 + l[2] + r[2], True)
            else:
                return (0, 0, max(l[2], r[2]), False)
        
        ans = solveLargestBST(root)
        return ans[2]


# Test cases
solution = Solution()

# Test case 1: Simple BST
print("Test case 1: Simple BST")
root1 = Node(10)
root1.left = Node(5)
root1.right = Node(15)
root1.left.left = Node(1)
root1.left.right = Node(8)
root1.right.right = Node(7)  # This breaks the BST property

print(f"Method 1 result: {solution.largestBst_method1(root1)}")
print(f"Method 2 result: {solution.largestBst(root1)}")
print()

# Test case 2: Perfect BST
print("Test case 2: Perfect BST")
root2 = Node(20)
root2.left = Node(10)
root2.right = Node(30)
root2.left.left = Node(5)
root2.left.right = Node(15)
root2.right.left = Node(25)
root2.right.right = Node(35)

print(f"Method 1 result: {solution.largestBst_method1(root2)}")
print(f"Method 2 result: {solution.largestBst(root2)}")
print()

# Test case 3: Complex tree
print("Test case 3: Complex tree")
root3 = Node(50)
root3.left = Node(30)
root3.right = Node(60)
root3.left.left = Node(5)
root3.left.right = Node(20)
root3.right.left = Node(45)
root3.right.right = Node(70)
root3.right.right.left = Node(65)
root3.right.right.right = Node(80)

print(f"Method 1 result: {solution.largestBst_method1(root3)}")
print(f"Method 2 result: {solution.largestBst(root3)}")
print()

# Test case 4: Single node
print("Test case 4: Single node")
root4 = Node(100)
print(f"Method 1 result: {solution.largestBst_method1(root4)}")
print(f"Method 2 result: {solution.largestBst(root4)}")
print()

# Test case 5: Empty tree
print("Test case 5: Empty tree")
root5 = None
print(f"Method 1 result: {solution.largestBst_method1(root5)}")
print(f"Method 2 result: {solution.largestBst(root5)}")