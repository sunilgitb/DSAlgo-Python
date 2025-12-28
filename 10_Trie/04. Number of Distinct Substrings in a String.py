# https://www.codingninjas.com/codestudio/problems/count-distinct-substrings_985292

class TrieNode:
    def __init__(self):
        self.children = {}

def countDistinctSubstrings(s: str) -> int:
    root = TrieNode()
    res = 0
    
    for i in range(len(s)):
        cur = root
        for j in range(i, len(s)):
            if s[j] not in cur.children:
                cur.children[s[j]] = TrieNode()
                res += 1
            cur = cur.children[s[j]]
    
    # +1 to include empty substring ""
    return res + 1


# ---------------- DRIVER CODE ----------------

s = "ababa"
ans = countDistinctSubstrings(s)
print(ans)
