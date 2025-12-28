'''
https://codeforces.com/problemset/problem/1475/B
B. New Year's Number
'''
 

# Function to check New Year's Number
def is_new_year_number(n):
    if n < 2020:
        return "NO"
    else:
        if n % 2020 <= n // 2020:
            return "YES"
        else:
            return "NO"

# ---------------- Example Usage ----------------
test_cases = [2020, 4041, 8081, 2019, 8080]

for n in test_cases:
    print(f"{n}: {is_new_year_number(n)}")
