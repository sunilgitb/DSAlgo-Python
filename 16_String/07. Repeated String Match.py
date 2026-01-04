# https://leetcode.com/problems/repeated-string-match/

# Method 1 ---------------------------------------  
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Handle edge cases
        if not b:  # b is empty string
            return 0
        if not a:  # a is empty but b is not (b is non-empty from above check)
            return -1
        
        res = 1
        tmp = a
        # Repeat a until it's at least as long as b
        while len(a) < len(b):
            a += tmp
            res += 1
        
        # Check if b is substring of a
        if self.subStr(a, b):
            return res
        
        # Check if b is substring of a + one more repetition
        if self.subStr(a + tmp, b):
            return res + 1
        
        return -1
    
    def subStr(self, a: str, b: str) -> bool:
        """Check if b is a substring of a"""
        # Quick checks
        if not b:
            return True
        if len(b) > len(a):
            return False
        
        for i in range(len(a) - len(b) + 1):
            if a[i] == b[0] and a[i:i+len(b)] == b:
                return True
        return False    ``

# Method 2 ---------------------------------------  
class Solution2:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Handle edge cases
        if not b:
            return 0
        if not a:
            return -1
        
        # Calculate minimum repetitions needed
        n = (len(b) - 1) // len(a) + 1  # Ceiling division
        
        # Check n, n+1, n+2 repetitions
        for i in range(3):
            repeated = a * (n + i)
            if self.subStr(repeated, b):
                return n + i
        return -1
    
    def subStr(self, a: str, b: str) -> bool:
        """Check if b is a substring of a"""
        # Quick checks
        if not b:
            return True
        if len(b) > len(a):
            return False
        
        # Built-in method (faster)
        return b in a


# Alternative using KMP for better performance
class SolutionKMP:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not b:
            return 0
        if not a:
            return -1
        
        # Build KMP table for pattern b
        def build_kmp_table(pattern):
            table = [0] * len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = table[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                table[i] = j
            return table
        
        def kmp_search(text, pattern):
            if not pattern:
                return 0
            table = build_kmp_table(pattern)
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = table[j-1]
                if text[i] == pattern[j]:
                    j += 1
                if j == len(pattern):
                    return i - j + 1
            return -1
        
        # Determine minimum repetitions needed
        min_reps = (len(b) + len(a) - 1) // len(a)
        
        # Try min_reps, min_reps+1, min_reps+2
        for reps in range(min_reps, min_reps + 3):
            repeated = a * reps
            if kmp_search(repeated, b) != -1:
                return reps
        
        return -1


solution = Solution()
solution2 = Solution2()
solutionKMP = SolutionKMP()

a = "abcd"
b = "cdabcdab"
print(solution.repeatedStringMatch(a, b))     # 3
print(solution2.repeatedStringMatch(a, b))    # 3
print(solutionKMP.repeatedStringMatch(a, b))  # 3

a = "a"
b = "aa"
print(solution.repeatedStringMatch(a, b))     # 2

a = "abc"
b = "def"
print(solution.repeatedStringMatch(a, b))     # -1

a = "abab"
b = "ba"
print(solution.repeatedStringMatch(a, b))     # 2

a = "abcd"
b = "da"
print(solution.repeatedStringMatch(a, b))     # 2
