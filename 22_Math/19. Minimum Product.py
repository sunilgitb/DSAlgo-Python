'''
https://codeforces.com/problemset/problem/1409/B

Solution: The greedy choice to is try to reduce a till x if we have enough rounds to use. Then we use the remaining rounds
to reduce b as much as we can. This gets one set of values of a and b reduced and we can get their product. We do another
round of this calculation where we prefer to reduce b first and then a. The minimum of these two products gives the minimum
possible product.  

''' 

def solve(a, b, x, y, n):
    min1 = calc_min_moves(a, b, x, y, n)  # reduce a first
    min2 = calc_min_moves(b, a, y, x, n)  # reduce b first
    return min(min1, min2)

def calc_min_moves(a, b, x, y, n):
    moves_a = min(n, a - x)
    moves_b = min(n - moves_a, b - y)
    reduced_a = a - moves_a
    reduced_b = b - moves_b
    return reduced_a * reduced_b

# ---------------- Example Usage ----------------
test_cases = [
    (10, 10, 8, 5, 3),  # a, b, x, y, n
    (12, 8, 8, 7, 4),
    (123, 456, 100, 400, 50)
]

for a, b, x, y, n in test_cases:
    print(f"Minimum product for ({a}, {b}, {x}, {y}, {n}): {solve(a, b, x, y, n)}")
