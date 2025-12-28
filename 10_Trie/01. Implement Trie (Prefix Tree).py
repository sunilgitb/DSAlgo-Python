# BASICS of TRIES
# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = {}       # hashmap for children
        self.endOfWord = False   # marks end of a word


class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    trie.insert("app")

    print("Search 'apple':", trie.search("apple"))     # True
    print("Search 'app':", trie.search("app"))         # True
    print("Search 'appl':", trie.search("appl"))       # False
    print("StartsWith 'ap':", trie.startsWith("ap"))   # True
    print("StartsWith 'bat':", trie.startsWith("bat")) # False
