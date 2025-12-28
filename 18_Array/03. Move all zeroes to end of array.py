# https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1/#
# https://www.geeksforgeeks.org/move-zeroes-end-array/

# Move all zeros to the end
# Move all zeros to the end while maintaining order
A = [5, 6, 0, 4, 6, 0, 9, 0, 8]
n = len(A)
j = 0  # position to place the next non-zero element

for i in range(n):
    if A[i] != 0:
        A[j], A[i] = A[i], A[j]  # swap non-zero element to its correct position
        j += 1

print(A)  # Output: [5, 6, 4, 6, 9, 8, 0, 0, 0]

