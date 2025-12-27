# INSERTION SORT Algorithm

a = [1, 4, 45, 66, 8, 89, 54, 0, 5, 6, 75, 675, 7, 56]

print("Original list:")
print(a)
print()

# First method
print("Method 1 (using insert and pop):")
b = a.copy()
for i in range(1, len(b)):
    for j in range(i):
        if b[j] > b[i]:
            b.insert(j, b[i])
            b.pop(i + 1)
            break
print(b)
print()

# Second method (standard insertion sort)
print("Method 2 (standard insertion sort):")
c = a.copy()

def insertionsort(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        position = i
        while current_element < arr[position - 1] and position > 0:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_element
    return arr

insertionsort(c)
print(c)
print()

# Test if both methods produce the same result
print("Both methods give same result:", b == c)