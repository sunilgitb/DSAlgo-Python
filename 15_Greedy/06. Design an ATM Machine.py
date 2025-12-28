# https://leetcode.com/problems/design-an-atm-machine/
# Design an ATM Machine
# Implement an ATM that supports deposit and withdraw operations
# Withdraw should give the maximum number of banknotes possible
# and prefer larger denominations first

from typing import List

class ATM:
    def __init__(self):
        # Denominations in descending order (greedy choice)
        self.denom = [20, 50, 100, 200, 500]
        # Count of each denomination available
        self.count = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        """
        Deposit banknotes into the ATM.
        banknotesCount[i] = number of notes of denomination denom[i]
        """
        for i in range(5):
            self.count[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        """
        Withdraw the requested amount using the largest denominations first.
        Returns the count of each denomination used, or [-1] if impossible.
        """
        # Work on a copy to avoid modifying counts if withdrawal fails
        temp_count = self.count[:]
        result = [0] * 5

        # Try to use largest denominations first (greedy)
        for i in range(4, -1, -1):
            # How many notes of this denomination can we use?
            can_use = min(amount // self.denom[i], temp_count[i])
            result[i] = can_use
            amount -= can_use * self.denom[i]
            temp_count[i] -= can_use

        # If we couldn't make exact amount, return [-1]
        if amount != 0:
            return [-1]

        # Withdrawal successful → update actual counts
        self.count = temp_count
        return result


# Driver Code with test cases
def run_tests():
    print("Testing ATM Design\n" + "="*40)
    
    atm = ATM()
    
    # Example from LeetCode
    operations = [
        ("deposit", [0,0,1,2,1]),   # deposit 100, 200×2, 500
        ("withdraw", 600),          # Expected: [0,0,1,0,1] (100 + 500)
        ("withdraw", 500),          # Expected: [-1] (not enough)
        ("withdraw", 200),          # Expected: [0,0,0,1,0]
        ("withdraw", 100),          # Expected: [-1]
        ("deposit", [0,0,0,0,1]),   # deposit another 500
        ("withdraw", 1000),         # Expected: [0,0,0,0,2]
    ]
    
    expected = [
        None,
        [0, 0, 1, 0, 1],
        [-1],
        [0, 0, 0, 1, 0],
        [-1],
        None,
        [0, 0, 0, 0, 2]
    ]
    
    results = []
    for op, arg in operations:
        if op == "deposit":
            atm.deposit(arg)
            results.append(None)
        else:
            res = atm.withdraw(arg)
            results.append(res)
    
    print("Operations:", [op for op, _ in operations])
    print("Results:   ", results)
    print("Expected:  ", expected)
    print("Status:    ", "✓ PASS" if results == expected else "✗ FAIL")


if __name__ == "__main__":
    run_tests()