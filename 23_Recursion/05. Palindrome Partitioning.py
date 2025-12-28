# https://leetcode.com/problems/palindrome-partitioning/
''' 
Traverse through the string and check whether left part of the iterator palindrom or not.
if palindrom call the function 
'''
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def solve(s, path):
            if not s:
                res.append(path)
                return
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1]:  # check palindrome
                    solve(s[i+1:], path + [s[:i+1]])
        
        solve(s, [])
        return res

# ----------------- Driver Code -----------------
test_cases = ["aab", "a", "racecar"]

solver = Solution()
for s in test_cases:
    print(f"Input: {s}")
    print(f"Palindrome partitions: {solver.partition(s)}\n")


''' 
Time Complexity: O( (2^n) *k*(n/2) )
Reason: O(2^n) to generate every substring and O(n/2) to check if the substring generated is a palindrome.
        O(k) is for inserting the palindromes in another data structure, where k  is the average length of the palindrome list.


Space Complexity: O(k * x)
Reason: The space complexity can vary depending upon the length of the answer. 
        k is the average length of the list of palindromes and if we have x such list of palindromes in our final answer. 
        The depth of the recursion tree is n, so the auxiliary space required is equal to the O(n).

'''