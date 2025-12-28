
'''
https://codeforces.com/problemset/problem/1206/B

Solution: Convert all the positives into 1, negatives as -1 and zeroes as is.
Now we need to check if we have odd number of negatives. If so, we if have some
zeroes, we take one of those and make it -1 so that even number of -1s multiply
to make +1. If not, we make one of the -1s as +1 using 2 moves. No we have -1s
and +1s multiplying to make +1. What's remaining is zeroes if left any. Convert
all of them as +1s for ease using that much of moves. The total of all these moves
is the final answer.
''' 
def solve(n, arr):
    moves = 0
    negatives = 0
    zeroes = 0

    for i in range(n):
        if arr[i] > 0:
            # convert positive to 1
            moves += arr[i] - 1
        elif arr[i] < 0:
            # convert negative to -1
            moves += -1 - arr[i]
            negatives += 1
        else:
            # count zeros
            zeroes += 1

    # if odd number of negatives, adjust
    if negatives % 2 == 1:
        if zeroes > 0:
            # use a zero to balance negative count
            moves += 1
            zeroes -= 1
        else:
            # flip one -1 to 1 using 2 moves
            moves += 2
            negatives -= 1

    # convert remaining zeros to 1
    moves += zeroes

    return moves

# ---------------- Example Usage ----------------
n = 5
arr = [-2, 4, 0, -3, 1]
print("Minimum moves to make product 1:", solve(n, arr))
