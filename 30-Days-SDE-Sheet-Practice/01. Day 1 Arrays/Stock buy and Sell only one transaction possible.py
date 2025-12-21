# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
''' 
only one transaction posible.
find difference of right max and left min
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        res = 0
        
        for price in prices:
            curMin = min(curMin, price)
            res = max(res, price - curMin)
        
        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [1, 2],
        [2, 4, 1],
        [3, 3, 5, 0, 0, 3, 1, 4]
    ]

    for i, prices in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        print("Prices:", prices)
        print("Max Profit:", sol.maxProfit(prices))
        print("-" * 30)
