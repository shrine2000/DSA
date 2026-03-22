from typing import List


# ---------------------------------------------------------------------------
# LeetCode 588 - Design In-Memory File System
# Approach: Optimal (Trie / Prefix Tree)
# ---------------------------------------------------------------------------
# Each TrieNode represents one path component (directory or file).
# - children : maps name -> TrieNode for subdirs / nested files
# - is_file  : True when this node is a file (not a directory)
# - content  : accumulated file content (empty string for directories)
#
# A single _traverse() helper walks (and lazily creates) nodes along a path,
# keeping all four public methods to a clean one-liner body.
#
# Time  Complexity:
#   ls                  -> O(m + n log n)  m = path depth, n = child count
#   mkdir               -> O(m)
#   addContentToFile    -> O(m)
#   readContentFromFile -> O(m)
# Space Complexity: O(N * M)  N = total nodes, M = average component length
# ---------------------------------------------------------------------------


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_file: bool = False
        self.content: str = ""


class FileSystem:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def _traverse(self, path: str) -> TrieNode:
        """Walk to the node at `path`, creating missing nodes along the way."""
        node = self.root
        if path == "/":
            return node
        for part in path.split("/")[1:]:   # skip the leading empty string
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        return node

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)
        if node.is_file:                   # return just the file's own name
            return [path.split("/")[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path)               # side-effect: creates nodes

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._traverse(filePath)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self._traverse(filePath).content


# obj = FileSystem()
# obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath, content)
# obj.readContentFromFile(filePath)
