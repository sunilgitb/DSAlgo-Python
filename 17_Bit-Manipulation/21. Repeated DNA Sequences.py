# https://leetcode.com/problems/repeated-dna-sequences/description/

# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        dic = {'A':0, 'C':1, 'G':2, 'T':3}
        n = len(s)
        if n < 10: 
            return []
        
        initial_val = 0
        seen = set()
        ans = set()
        
        for i in range(n - 9):
            if i == 0:
                for j in range(10):
                    initial_val <<= 2
                    initial_val |= dic[s[j]]
            else:
                initial_val &= (1 << 18) - 1  # keep last 18 bits
                initial_val <<= 2
                initial_val |= dic[s[i+9]]
            
            if initial_val in seen:
                ans.add(s[i:i+10])
            else:
                seen.add(initial_val)
        
        return list(ans)


# -------- Driver Code --------
solution = Solution()

s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(solution.findRepeatedDnaSequences(s1))  
# Output: ['AAAAACCCCC', 'CCCCCAAAAA']

s2 = "AAAAAAAAAAAA"
print(solution.findRepeatedDnaSequences(s2))  
# Output: ['AAAAAAAAAA']
