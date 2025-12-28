# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(cur, idx):
            if idx == len(word):
                return cur.isWord

            c = word[idx]
            if c == '.':
                for child in cur.children.values():
                    if dfs(child, idx + 1):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                return dfs(cur.children[c], idx + 1)

        return dfs(self.root, 0)


# ---------------- DRIVER CODE ----------------

wd = WordDictionary()

wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")

print(wd.search("pad"))  # False
print(wd.search("bad"))  # True
print(wd.search(".ad"))  # True
print(wd.search("b.."))  # True
print(wd.search("ba."))  # True
print(wd.search("b.d"))  # True
print(wd.search("b"))    # False
