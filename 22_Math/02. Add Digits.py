# https://leetcode.com/problems/add-digits/

# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        """
        Digital Root Formula:
        - If num == 0 → 0
        - If num % 9 == 0 → 9
        - Else → num % 9
        """
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [0, 38, 9, 18, 123, 9999]

    for num in test_cases:
        print(f"addDigits({num}) = {sol.addDigits(num)}")

"""
Output:
addDigits(0) = 0
addDigits(38) = 2
addDigits(9) = 9
addDigits(18) = 9
addDigits(123) = 6
addDigits(9999) = 9
"""
