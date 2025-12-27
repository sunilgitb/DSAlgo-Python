class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        elif self.key < data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
        elif self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)

    def search(self, data):
        if self.key == data:
            return True
        elif self.key < data:
            if self.rchild:
                return self.rchild.search(data)
            else:
                return False
        else:  # self.key > data
            if self.lchild:
                return self.lchild.search(data)
            else:
                return False
    
    def preorder(self):
        print(self.key, end=", ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def delete(self, data):
        if self.key is None:
            print("Tree is Empty!")
            return self
            
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
        else:
            # Node found
            if self.lchild is None and self.rchild is None:
                return None
            elif self.lchild is None:
                return self.rchild
            elif self.rchild is None:
                return self.lchild
            else:
                # Node with two children
                successor = self.rchild
                while successor.lchild:
                    successor = successor.lchild
                self.key = successor.key
                self.rchild = self.rchild.delete(successor.key)
        
        return self


# Example 1: Basic BST operations
print("EXAMPLE 1: Basic BST Operations")
print("-" * 40)
root = BST(10)
values = [5, 15, 3, 7, 12, 18]
for i in values:
    root.insert(i)

print("Preorder traversal:")
root.preorder()  # Output: 10, 5, 3, 7, 15, 12, 18,

print("\n\nSearch for 7:", "Found" if root.search(7) else "Not Found")
print("Search for 20:", "Found" if root.search(20) else "Not Found")

# Example 2: Delete operations
print("\n\nEXAMPLE 2: Delete Operations")
print("-" * 40)
root2 = BST(50)
values2 = [30, 70, 20, 40, 60, 80]
for i in values2:
    root2.insert(i)

print("Before deletion - Preorder:")
root2.preorder()  # Output: 50, 30, 20, 40, 70, 60, 80,

root2 = root2.delete(20)  # Delete leaf node
print("\n\nAfter deleting 20 (leaf) - Preorder:")
root2.preorder()  # Output: 50, 30, 40, 70, 60, 80,

root2 = root2.delete(30)  # Delete node with one child
print("\n\nAfter deleting 30 (node with one child) - Preorder:")
root2.preorder()  # Output: 50, 40, 70, 60, 80,