"""
File: 05. Next Smallest Palindrome.py

Problem:
Given a number as a string, find the smallest palindrome
strictly greater than the given number.

GeeksForGeeks:
https://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/

LeetCode Variant:
Similar logic used in palindrome construction problems
"""

# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

def is_all_9(num: str) -> bool:
    """Check if all digits are 9"""
    return all(ch == '9' for ch in num)


def mirror_left_to_right(num: list) -> None:
    """Mirror left half to right half"""
    n = len(num)
    for i in range(n // 2):
        num[n - i - 1] = num[i]


# ------------------------------------------------------------
# Core Function
# ------------------------------------------------------------

def next_smallest_palindrome(num: str) -> str:
    n = len(num)

    # Case 1: All digits are 9 → 999 -> 1001
    if is_all_9(num):
        return "1" + ("0" * (n - 1)) + "1"

    num = list(num)
    mid = n // 2

    left_smaller = False

    # Step 1: Find first mismatch from middle
    i = mid - 1
    j = mid + 1 if n % 2 else mid

    while i >= 0 and num[i] == num[j]:
        i -= 1
        j += 1

    if i < 0 or num[i] < num[j]:
        left_smaller = True

    # Step 2: Mirror left to right
    mirror_left_to_right(num)

    # Step 3: If left side was smaller, increment middle
    if left_smaller:
        carry = 1

        # Odd length → increment middle digit
        if n % 2 == 1:
            num[mid] = str((int(num[mid]) + carry) % 10)
            carry = 1 if num[mid] == '0' else 0
            i = mid - 1
        else:
            i = mid - 1

        # Propagate carry to the left
        while i >= 0 and carry:
            num[i] = str((int(num[i]) + carry) % 10)
            carry = 1 if num[i] == '0' else 0
            num[n - i - 1] = num[i]
            i -= 1

    return "".join(num)


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        "23545",
        "999",
        "1221",
        "808",
        "2133",
        "1",
        "88",
        "12932"
    ]

    for num in test_cases:
        print(f"Next palindrome after {num} -> {next_smallest_palindrome(num)}")


"""
Output:
Next palindrome after 23545 -> 23632
Next palindrome after 999 -> 1001
Next palindrome after 1221 -> 1331
Next palindrome after 808 -> 818
Next palindrome after 2133 -> 2222
Next palindrome after 1 -> 2
Next palindrome after 88 -> 99
Next palindrome after 12932 -> 13031
"""

# ------------------------------------------------------------
# Time Complexity: O(N)
# Space Complexity: O(N)
# ------------------------------------------------------------
