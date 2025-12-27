# Selection Sort Algorithm

def selection_sort(arr):
    for i in range(len(arr)):
        mi = i   # index of minimum element in arr[i:]
        for j in range(i + 1, len(arr)):
            if arr[mi] > arr[j]:
                mi = j
        # Swap the found minimum element with the first element   
        arr[i], arr[mi] = arr[mi], arr[i]
    return arr


# Test cases
test_cases = [
    [10, 16, 8, 12, 15, 3, 9, 5],
    [64, 34, 25, 12, 22, 11, 90],
    [5, 2, 8, 1, 9],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [42],
    []
]

print("Testing Selection Sort:")
print("=" * 50)

for i, arr in enumerate(test_cases, 1):
    original = arr.copy()
    if arr:  # Only sort non-empty lists
        selection_sort(arr)
    print(f"Test {i}: {original} -> {arr}")