class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)
    def dfs(self, word, index, node):
        if index == len(word):
            return node.is_end
        ch = word[index]
        if ch == '.':
            for child in node.children.values():
                if self.dfs(word, index + 1, child):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self.dfs(word, index + 1, node.children[ch])