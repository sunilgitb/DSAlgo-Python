def partition(arr, l, r):
    p = l
    while l <= r:
        while l < r and arr[l] <= arr[p]:
            l += 1
        while r > l and arr[r] >= arr[p]:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    arr[p], arr[r] = arr[r], arr[p]
    return r

def quicksort(arr, l, r):
    if l >= r:
        return
    j = partition(arr, l, r)
    quicksort(arr, l, j - 1)
    quicksort(arr, j + 1, r)


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

print("Testing Quick Sort:")
print("=" * 50)

for i, arr in enumerate(test_cases, 1):
    original = arr.copy()
    if arr:  # Only sort non-empty lists
        quicksort(arr, 0, len(arr) - 1)
    print(f"Test {i}: {original} -> {arr}")