class Solution:
    
    # Heapify function to maintain heap property
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
    
    # Function to build a Heap from array
    def buildHeap(self, arr, n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
    
    # Function to sort an array using Heap Sort
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)


# Test cases
solution = Solution()

test_arrays = [
    [4, 1, 3, 9, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [64, 34, 25, 12, 22, 11, 90],
    [5, 4, 3, 2, 1],
    [1],
    []
]

print("Testing Heap Sort:")
print("=" * 50)

for i, arr in enumerate(test_arrays, 1):
    if arr:  # Only sort non-empty arrays
        original = arr.copy()
        solution.HeapSort(arr, len(arr))
        print(f"Test {i}: {original} -> {arr}")
    else:
        print(f"Test {i}: [] -> [] (empty array)")