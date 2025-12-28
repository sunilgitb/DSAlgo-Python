# https://leetcode.com/problems/search-suggestions-system/

# Method 1: Sorting + Prefix Filtering
class Solution1:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        for i, c in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == c]
            res.append(products[:3])
        return res

# Method 2: Trie (Efficient insertion + pre-stored suggestions)
class Node:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
            # Add word to suggestions if we still have space
            if len(cur.suggestions) < 3:
                cur.suggestions.append(word)
    
    def getSuggestions(self, searchWord):
        cur = self.root
        res = []
        for c in searchWord:
            if c in cur.children:
                cur = cur.children[c]
                res.append(cur.suggestions[:])  # copy list
            else:
                break
        # Pad with empty lists if searchWord is longer than matched prefix
        res += [[] for _ in range(len(searchWord) - len(res))]
        return res

class Solution2:
    def suggestedProducts(self, products, searchWord):
        products.sort()  # ensures lexicographical order
        trie = Trie()
        for word in products:
            trie.addWord(word)
        return trie.getSuggestions(searchWord)

# Method 3: Trie + DFS (Alternative approach)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.val = ""

class Solution3:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.val = c
        cur.isWord = True
    
    def suggestedProducts(self, products, searchWord):
        products.sort()
        for product in products:
            self.addWord(product)
        
        def dfs(node, arr, tmp):
            if len(arr) == 3 or not node:
                return
            if node.isWord:
                arr.append(tmp)
            for child in sorted(node.children.values(), key=lambda x: x.val):
                dfs(child, arr, tmp + child.val)
        
        cur = self.root
        res = []
        prefix = ""
        for i, c in enumerate(searchWord):
            if c not in cur.children:
                break
            cur = cur.children[c]
            prefix += c
            arr = []
            dfs(cur, arr, "")
            # Prepend current prefix to each suggestion
            res.append([prefix + s for s in arr])
        
        # Pad remaining positions with empty lists
        res += [[] for _ in range(len(searchWord) - len(res))]
        return res

# Driver Code
def run_test(products, searchWord):
    print(f"\nProducts: {products}")
    print(f"Search word: {searchWord}")
    
    sol1 = Solution1()
    sol2 = Solution2()
    sol3 = Solution3()
    
    result1 = sol1.suggestedProducts(products[:], searchWord)  # copy list
    result2 = sol2.suggestedProducts(products[:], searchWord)
    result3 = sol3.suggestedProducts(products[:], searchWord)
    
    print("Method 1 (Sorting):")
    for i, c in enumerate(searchWord):
        print(f"  After '{searchWord[:i+1]}': {result1[i]}")
    
    print("\nMethod 2 (Trie with pre-stored suggestions):")
    for i, c in enumerate(searchWord):
        print(f"  After '{searchWord[:i+1]}': {result2[i]}")
    
    print("\nMethod 3 (Trie + DFS):")
    for i, c in enumerate(searchWord):
        print(f"  After '{searchWord[:i+1]}': {result3[i]}")
    print("-" * 60)

# Test cases
if __name__ == "__main__":
    test_cases = [
        (
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "mouse"
        ),
        (
            ["havana"],
            "havana"
        ),
        (
            ["bags", "baggage", "banner", "basket", "bats"],
            "ba"
        ),
        (
            ["abcd", "abcde", "abcdef"],
            "abcdefg"  # longer than any product
        ),
    ]
    
    for products, searchWord in test_cases:
        run_test(products, searchWord)