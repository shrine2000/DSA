from typing import List
from collections import deque


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.word: str = ""


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def search(self, word: str) -> bool:
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node: TrieNode = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def search_prefix(self, prefix: str) -> str:
        node: TrieNode = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
            if node.is_end_of_word:
                return node.word
        return None

    @staticmethod
    def replaceWords(dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        trie.print_trie()

        def replace(word: str) -> str:
            for i in range(len(word)):
                prefix = word[: i + 1]
                root = trie.search_prefix(prefix)
                if root:
                    return root
            return word

        replace_sentence: List[str] = [replace(word) for word in sentence.split()]
        return " ".join(replace_sentence)

    def longestWord(self):
        longest_word = ""
        queue = deque([(self.root, "")])
        while queue:
            node, current_word = queue.popleft()
            if node.is_end_of_word:
                if len(current_word) > len(longest_word):
                    longest_word = current_word
            for char, child_node in node.children.items():
                queue.append((child_node, current_word + char))

        return longest_word

    def _print_trie(self, node: TrieNode, level: int = 0) -> None:
        if node is None:
            return
        for char, child in node.children.items():
            print(" " * level + f"Index {char}: Character '{char}'")
            print(" " * (level + 1) + f"Child Node: {child}")
            print(" " * (level + 1) + f"Is End of Word: {child.is_end_of_word}")
            print(
                " " * (level + 1)
                + f"Children: {list(child.children.keys()) if child.children else 'None'}"
            )
            print()
            self._print_trie(child, level + 1)

    def print_trie(self) -> None:
        self._print_trie(self.root)


if __name__ == "__main__":
    # Test cases
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    replaced_sentence = Trie.replaceWords(dictionary, sentence)
    print(replaced_sentence)  # Output: "the cat was rat by the bat"

    # Test Trie functionality
    trie: Trie = Trie()
    words_to_insert = ["apple", "banana", "orange", "app", "ban", "application"]
    for word in words_to_insert:
        trie.insert(word)

    assert trie.search("apple") == True
    assert trie.search("banana") == True
    assert trie.search("orange") == True
    assert trie.search("app") == True
    assert trie.search("ban") == True
    assert trie.search("grape") == False

    assert trie.startsWith("app") == True
    assert trie.startsWith("or") == True
    assert trie.startsWith("gr") == False

    trie: Trie = Trie()
    words = ["w", "wo", "wor", "worl", "world", "word", "abc"]
    for word in words:
        trie.insert(word)

    print(trie.longestWord())

    trie.print_trie()
