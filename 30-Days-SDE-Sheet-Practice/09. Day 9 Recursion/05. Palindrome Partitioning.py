# https://leetcode.com/problems/palindrome-partitioning/
''' 
Traverse through the string and check whether left part of the iterator palindrom or not.
if palindrom call the function 
'''
# https://leetcode.com/problems/palindrome-partitioning/
'''
Traverse through the string and check whether the left substring is palindrome or not.
If palindrome, recurse for the remaining string.
'''

class Solution:
    def partition(self, s):
        res = []

        def solve(s, path):
            if not s:
                res.append(path)
                return

            for i in range(len(s)):
                # check if prefix is palindrome
                if s[:i+1] == s[:i+1][::-1]:
                    solve(s[i+1:], path + [s[:i+1]])

        solve(s, [])
        return res


# -------- DRIVER CODE --------
sol = Solution()

print(sol.partition("aab"))
# Expected Output: [['a', 'a', 'b'], ['aa', 'b']]

print(sol.partition("a"))
# Expected Output: [['a']]

print(sol.partition("aba"))
# Expected Output: [['a', 'b', 'a'], ['aba']]

print(sol.partition("nitin"))
# Expected Output: [['n', 'i', 't', 'i', 'n'], ['n', 'iti', 'n'], ['nitin']]

''' 
Time Complexity: O( (2^n) *k*(n/2) )
Reason: O(2^n) to generate every substring and O(n/2) to check if the substring generated is a palindrome.
        O(k) is for inserting the palindromes in another data structure, where k  is the average length of the palindrome list.


Space Complexity: O(k * x)
Reason: The space complexity can vary depending upon the length of the answer. 
        k is the average length of the list of palindromes and if we have x such list of palindromes in our final answer. 
        The depth of the recursion tree is n, so the auxiliary space required is equal to the O(n).

'''