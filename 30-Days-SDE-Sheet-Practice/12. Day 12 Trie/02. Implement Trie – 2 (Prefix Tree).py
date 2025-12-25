# https://www.codingninjas.com/codestudio/problems/implement-trie_1387095

# https://youtu.be/ict1UawpXMM?t=359

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWordCount = 0
        self.prefixOfWordCount = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.prefixOfWordCount += 1
        cur.endOfWordCount += 1

    def countWordsEqualTo(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.endOfWordCount

    def countWordsStartingWith(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.prefixOfWordCount

    def erase(self, word):  # Delete function
        cur = self.root
        toBeDeleted = None
        for c in word:  # as it a delete function so word is present in trie so we don't need to check if key 'c' present in children hashmap or not. 
            cur = cur.children[c]
            cur.prefixOfWordCount -= 1
            if toBeDeleted:
                toBeDeleted = None
            if cur.prefixOfWordCount == 0:
                toBeDeleted = cur
                
        if toBeDeleted:
            toBeDeleted = None
        cur.endOfWordCount -= 1


# Example / driver code 🔧
if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    trie.insert("apple")
    trie.insert("app")

    print("countWordsEqualTo('apple') ->", trie.countWordsEqualTo("apple"))  # 2
    print("countWordsEqualTo('app') ->", trie.countWordsEqualTo("app"))      # 1
    print("countWordsStartingWith('app') ->", trie.countWordsStartingWith("app"))  # 3

    trie.erase("apple")
    print("After erase('apple'): countWordsEqualTo('apple') ->", trie.countWordsEqualTo("apple"))  # 1

    trie.erase("apple")
    print("After erase('apple') again: countWordsEqualTo('apple') ->", trie.countWordsEqualTo("apple"))  # 0

    # Sanity checks
    assert trie.countWordsEqualTo("apple") == 0
    assert trie.countWordsEqualTo("app") == 1
    assert trie.countWordsStartingWith("app") == 1

    print("Driver tests passed ✅")
            cur = cur.children[c]
            cur.prefixOfWordCount -= 1
                
        cur.endOfWordCount -= 1
    # output: Driver tests passed ✅
# Example / driver code 🔧