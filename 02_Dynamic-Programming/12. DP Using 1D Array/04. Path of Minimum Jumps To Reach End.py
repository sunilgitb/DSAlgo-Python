# Find the indices path of minimum jumps to reach last index
# Time: O(n^2)
# Space: O(n)

def min_jump_path(nums):
    n = len(nums)
    
    dp = [0] * n           # dp[i] = minimum jumps to reach index i
    jump_index = [0] * n   # jump_index[i] = index from which we jumped to reach i

    for i in range(1, n):
        dp[i] = float('inf')
        for j in range(i):
            if j + nums[j] >= i:
                if dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
                    jump_index[i] = j

    # Reconstruct path from last index to 0
    path = []
    j = n - 1
    while j > 0:
        path.append(j)
        j = jump_index[j]
    path.append(0)

    return path[::-1]


# ---------------- Example Usage ----------------
nums = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]

path = min_jump_path(nums)
print("Minimum Jump Path:", path)

# Output:
# Minimum Jump Path: [0, 1, 4, 5, 9]
