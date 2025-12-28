# https://practice.geeksforgeeks.org/problems/sort-a-stack/1#
# Sort a Stack using Recursion without using any loop

# https://practice.geeksforgeeks.org/problems/sort-a-stack/1#
# Sort a Stack using Recursion without using any loop

class Solution:
    def sorted(self, stack):   # Main Sort Function
        if not stack: 
            return stack
        tmp = stack.pop()
        self.sorted(stack)
        self.insertInSortedStack(stack, tmp)
        return stack
    
    def insertInSortedStack(self, stack, tmp):  # Helper function to insert element in sorted stack 
        if not stack or tmp >= stack[-1]:
            stack.append(tmp)
            return
        else:
            top = stack.pop()
            self.insertInSortedStack(stack, tmp)
            stack.append(top)
            return

# Time Complexity: O(n²)
# Auxiliary Space: O(N) for recursion stack


# Driver Code
if __name__ == '__main__':
    test_cases = [
        [3, 2, 1],
        [11, 2, 32, 3, 41],
        [1],
        [],
        [5, 1, 4, 2, 3],
        [10, 20, 30, 40, 50],
        [50, 40, 30, 20, 10],
        [3, 6, 1, 8, 4, 9, 2]
    ]
    
    print("Testing Stack Sort using Recursion")
    print("=" * 50)
    
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input stack (top to bottom): {arr}")
        
        # Create a copy since sorting modifies the list
        stack_copy = arr.copy()
        sol = Solution()
        sorted_stack = sol.sorted(stack_copy)
        
        print(f"Sorted stack (top to bottom): {sorted_stack}")
        
        # Print in GeeksforGeeks format (popping from top)
        print("Output (popping from top):", end=" ")
        temp = sorted_stack.copy()
        while temp:
            print(temp.pop(), end=" ")
        print()
    
    print("\n" + "=" * 50)
    print("Complexity Analysis:")
    print("- Time Complexity: O(n²)")
    print("- Auxiliary Space: O(n) for recursion stack")
    
    # Example walkthrough
    print("\n" + "=" * 50)
    print("Example Walkthrough - Sorting [3, 2, 1]:")
    print("-" * 50)
    
        
# Time Complexity: O(n2)
# Auxiliary Space: O(N)
        
        
        


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends