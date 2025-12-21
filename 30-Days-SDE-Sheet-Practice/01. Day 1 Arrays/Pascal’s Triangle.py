# https://leetcode.com/problems/pascals-triangle/

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        for i in range(2, numRows + 1):
            tmp = [1] * i
            for j in range(1, i - 1):
                tmp[j] = arr[-1][j - 1] + arr[-1][j]
            arr.append(tmp)
        return arr


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [1, 2, 5, 7]

    for n in test_cases:
        print(f"Pascal's Triangle with {n} rows:")
        result = sol.generate(n)
        for row in result:
            print(row)
        print("-" * 30)
