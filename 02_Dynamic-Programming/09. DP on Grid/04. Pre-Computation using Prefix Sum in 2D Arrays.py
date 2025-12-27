# https://youtu.be/nZe7P674xZo
# 2D Prefix Sum (Cumulative Sum) in a Matrix
# Computes the sum of all sub-matrices in O(1) time after O(n*m) preprocessing

arr = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

# Step 1: Compute prefix sum for first column (downward)
for i in range(1, len(arr)):
    arr[i][0] += arr[i - 1][0]

# Step 2: Compute prefix sum for first row (rightward)
for j in range(1, len(arr[0])):
    arr[0][j] += arr[0][j - 1]

# Step 3: Compute prefix sum for rest of the matrix
for i in range(1, len(arr)):
    for j in range(1, len(arr[0])):
        arr[i][j] = arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1] + arr[i][j]
    # print(arr[i])  # Optional: print each row after computation

# Final prefix sum matrix (each cell = sum from (0,0) to (i,j))
print("Final 2D Prefix Sum Matrix:")
for row in arr:
    print(row)

# Example queries: Sum of any sub-matrix in O(1)
# Formula: sum(x1,y1) to (x2,y2) = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

# Example: sum from (0,0) to (2,2)
x1, y1, x2, y2 = 0, 0, 2, 2
sum_rect = arr[x2][y2]
if x1 > 0: sum_rect -= arr[x1-1][y2]
if y1 > 0: sum_rect -= arr[x2][y1-1]
if x1 > 0 and y1 > 0: sum_rect += arr[x1-1][y1-1]
print(f"\nSum from (0,0) to (2,2): {sum_rect}")  # Output: 9

# Example: sum from (1,1) to (3,3)
x1, y1, x2, y2 = 1, 1, 3, 3
sum_rect = arr[x2][y2]
if x1 > 0: sum_rect -= arr[x1-1][y2]
if y1 > 0: sum_rect -= arr[x2][y1-1]
if x1 > 0 and y1 > 0: sum_rect += arr[x1-1][y1-1]
print(f"Sum from (1,1) to (3,3): {sum_rect}")  # Output: 9