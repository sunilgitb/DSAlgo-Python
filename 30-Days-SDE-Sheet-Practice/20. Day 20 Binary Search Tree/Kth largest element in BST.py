# https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1#

class Solution:
    def kthLargest(self,root, k):
        #your code here
        self.k = k
        self.res = root.data
        def reverseInorder(root):
            if not root: 
                return
            reverseInorder(root.right)
            self.k -= 1
            if self.k == 0:
                self.res = root.data
            reverseInorder(root.left)
        
        reverseInorder(root)
        return self.res

# Time: O(N)
# Space: O(1)

if __name__ == "__main__":
    # Local Node definition for example (GeeksforGeeks style uses 'data')
    class Node:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    # Build example BST:
    #        6
    #       / \
    #      4   8
    #     / \  / \
    #    3  5 7  9
    n3 = Node(3)
    n5 = Node(5)
    n4 = Node(4, n3, n5)
    n7 = Node(7)
    n9 = Node(9)
    n8 = Node(8, n7, n9)
    root = Node(6, n4, n8)

    sol = Solution()
    for k in [1, 3, 5, 7]:
        print(f"k={k} ->", sol.kthLargest(root, k))

    # Expected:
    # k=1 -> 9 (largest)
    # k=3 -> 7
    # k=5 -> 5
    # k=7 -> 3

# Space: O(1)