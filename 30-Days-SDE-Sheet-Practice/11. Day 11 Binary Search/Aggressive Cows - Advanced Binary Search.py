# https://www.codingninjas.com/codestudio/problems/aggressive-cows_1082559
# https://youtu.be/YTTdLgyqOLY?t=2626

'''
Binary Search on Answer

We try to maximize the minimum distance between cows.
Use binary search on distance and check feasibility using greedy placement.
'''

def aggressiveCows(stalls, k):

    def isValid(mid):
        count = 1                  # first cow placed
        lastPosition = stalls[0]   # position of last placed cow

        for i in range(1, len(stalls)):
            if stalls[i] - lastPosition >= mid:
                count += 1
                lastPosition = stalls[i]
                if count == k:
                    return True
        return False

    stalls.sort()
    low = 0
    high = max(stalls)
    ans = 0

    while low <= high:
        mid = low + (high - low) // 2
        if isValid(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


# -------- DRIVER CODE --------

print(aggressiveCows([1, 2, 4, 8, 9], 3))
# Expected Output: 3

print(aggressiveCows([10, 1, 2, 7, 5], 3))
# Expected Output: 4

print(aggressiveCows([4, 2, 1, 3, 6], 2))
# Expected Output: 5

print(aggressiveCows([1, 2, 8, 4, 9], 3))
# Expected Output: 3
