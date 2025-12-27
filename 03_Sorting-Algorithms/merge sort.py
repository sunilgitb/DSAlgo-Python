def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


# Alternative implementation with better variable names
def mergesort(a, l, r):
    if l < r:
        m = (l + r) // 2
        mergesort(a, l, m)
        mergesort(a, m + 1, r)
        merge(a, l, m, r)
    return a

def merge(a, l, m, r):
    i = l
    j = m + 1
    b = []
    
    while i <= m and j <= r:
        if a[i] <= a[j]:
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j += 1

    while i <= m:
        b.append(a[i])
        i += 1
    
    while j <= r:
        b.append(a[j])
        j += 1

    # Copy back from temporary list b to original array a
    for k in range(len(b)):
        a[l + k] = b[k]


# Test cases
test_cases = [
    [1, 4, 45, 66, 8, 89, 54, 0, 5, 6, 75, 675, 7, 56],
    [64, 34, 25, 12, 22, 11, 90],
    [5, 2, 8, 1, 9],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [42],
    []
]

print("Testing Merge Sort:")
print("=" * 60)

print("Method 1 (slicing):")
for i, arr in enumerate(test_cases, 1):
    original = arr.copy()
    sorted_arr = mergeSort(arr)
    print(f"Test {i}: {original} -> {sorted_arr}")

print("\n" + "=" * 60 + "\n")

print("Method 2 (index-based):")
for i, arr in enumerate(test_cases, 1):
    original = arr.copy()
    if arr:  # Only sort non-empty lists
        mergesort(arr, 0, len(arr) - 1)
    print(f"Test {i}: {original} -> {arr}")