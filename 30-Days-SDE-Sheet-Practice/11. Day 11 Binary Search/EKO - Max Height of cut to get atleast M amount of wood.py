# https://www.spoj.com/problems/EKO/
# Problem: Wood Cutting (Binary Search on Answer)

'''
We need to find the maximum height H such that
cutting all trees taller than H gives at least M wood.
'''

def isValid(arr, M, mid):
    wood = 0
    for h in arr:
        if h > mid:
            wood += h - mid
    return wood >= M


def maxSawHeight(arr, M):
    low = 0
    high = max(arr)
    ans = 0

    while low <= high:
        mid = low + (high - low) // 2
        if isValid(arr, M, mid):
            ans = mid          # valid height, try higher
            low = mid + 1
        else:
            high = mid - 1     # not enough wood, decrease height

    return ans


# -------- DRIVER CODE --------

trees = [20, 15, 10, 17]
M = 7
print(maxSawHeight(trees, M))
# Expected Output: 15


trees = [4, 42, 40, 26, 46]
M = 20
print(maxSawHeight(trees, M))
# Expected Output: 36


trees = [100, 200, 300, 400]
M = 250
print(maxSawHeight(trees, M))
# Expected Output: 250
