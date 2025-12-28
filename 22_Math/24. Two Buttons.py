'''
https://codeforces.com/problemset/problem/520/B
B. Two Buttons
'''
# Example values
n = 4
m = 20

count = 0

while m > n:
    if m % 2 == 0:
        m //= 2
    else:
        m += 1
    count += 1

count += n - m

print(count)  # Output: 5
