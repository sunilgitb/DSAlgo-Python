def solve():
    arr = [1, 2, 3, 4, 1, 2]   # sample array
    n = len(arr)

    arr.sort()
    cur_size = 0
    total_size = 0

    for x in arr:
        cur_size += 1
        if cur_size == x:
            total_size += 1
            cur_size = 0

    print(total_size)


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    solve() # output 3
