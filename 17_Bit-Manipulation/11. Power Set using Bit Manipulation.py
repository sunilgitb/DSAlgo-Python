# https://practice.geeksforgeeks.org/problems/power-set4302/1#
# https://youtu.be/b7AYbpM5YrE

'''
say p is total numer of power sets. In binary form 1 to p if we select 
letter of position where 1 bit then we get all the combinations.
Then sort the result.
'''

# https://practice.geeksforgeeks.org/problems/power-set4302/1
# https://youtu.be/b7AYbpM5YrE

class Solution:
    def AllPossibleStrings(self, s: str):
        n = len(s)
        p = 2 ** n   # total number of subsets
        res = []
        for i in range(1, p):
            tmp = ''
            for j in range(n):
                if i & (1 << j):
                    tmp += s[j]
            res.append(tmp)
        return sorted(res)


# -------- Driver Code --------
solution = Solution()

print(solution.AllPossibleStrings("abc"))  # ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
print(solution.AllPossibleStrings("xy"))   # ['x', 'xy', 'y']
print(solution.AllPossibleStrings("p"))    # ['p']
print(solution.AllPossibleStrings(""))     # []


# Time: O(2^n * n)
# Space: O(n)

