# https://leetcode.com/problems/beautiful-arrangement-ii/

from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        numset = {i for i in range(2, n+1)}
        i = 1
        res = [1]
        while k > 1:
            a = i - k
            b = i + k
            if a in numset:
                res.append(a)
                i = a
            else:
                res.append(b)
                i = b
            numset.remove(i)
            k -= 1
        return res + list(numset)

# ---------------- Example Usage ----------------
sol = Solution()

test_cases = [
    (3, 1),
    (3, 2),
    (7, 3)
]

for n, k in test_cases:
    result = sol.constructArray(n, k)
    print(f"n={n}, k={k} -> {result}")

# Time: O(K)
# Space: O(N)
