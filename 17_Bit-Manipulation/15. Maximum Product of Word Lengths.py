# https://leetcode.com/problems/maximum-product-of-word-lengths/

'''
class Solution:
    def maxProduct(self, words):
        wordDict = {}
        for word in words:
            wordDict[word] = [False]*26
            for w in word:
                wordDict[word][ord(w) - ord('a')] = True
        
        res = 0
        for i, w1 in enumerate(words):
            for w2 in words[i+1:]:
                flag = True
                for j in range(26):
                    if wordDict[w1][j] and wordDict[w2][j]:
                        flag = False
                if flag:
                    res = max(res, len(w1) * len(w2))
        
        return res   
'''


# Solving the above using bitmanipulation.
# instead of using a bool array in dictionary use a binary number of 26bits
# where 1 represent that letter is present and 0 means not.
# if we & of 2 word != 0 means any common bit. 
    
# https://leetcode.com/problems/maximum-product-of-word-lengths/

from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Convert each word into a 26-bit integer mask
        wordDict = {}
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            wordDict[word] = mask
        
        res = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if not wordDict[words[i]] & wordDict[words[j]]:  # no common letters
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res


# -------- Driver Code --------
solution = Solution()

print(solution.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))  # 16
print(solution.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))       # 4
print(solution.maxProduct(["a","aa","aaa","aaaa"]))                        # 0
print(solution.maxProduct(["abc","def","gh"]))                             # 9

        
# Time Complexity : O(n*(N+n))
