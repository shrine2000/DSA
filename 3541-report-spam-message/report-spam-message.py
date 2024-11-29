class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        node = Trie()
        count = 0
        for words in bannedWords:
            node.insert(words)

        for msg in message:
            if node.search(msg):
                count += 1
                if count >= 2:
                    return True
        return False
