from typing import List

# LeetCode 588. Design In-Memory File System
# Problem Link: https://leetcode.com/problems/design-in-memory-file-system/


# ---------------------------------------------------------------------------
# Approach 1: Brute Force (HashMap)
# ---------------------------------------------------------------------------
# Use two flat dicts:
#   - `dirs`  : path -> set of immediate children names
#   - `files` : path -> file content string
#
# Every mkdir/addContentToFile walks the path and registers every prefix in
# `dirs`.  ls checks whether the path is a file (in `files`) or a directory
# (in `dirs`) and returns the appropriate result.
#
# Time  Complexity: O(m) per operation where m = path length
# Space Complexity: O(N * M) where N = number of entries, M = avg path length
# ---------------------------------------------------------------------------


class FileSystemBruteForce:
    def __init__(self) -> None:
        self.dirs: dict[str, set] = {'/': set()}   # dir path -> child names
        self.files: dict[str, str] = {}            # file path -> content

    def ls(self, path: str) -> List[str]:
        if path in self.files:                     # it's a file
            return [path.split('/')[-1]]
        return sorted(self.dirs[path])             # it's a directory

    def mkdir(self, path: str) -> None:
        parts = path.split('/')                    # ['', 'a', 'b', 'c']
        cur = ''
        for part in parts[1:]:
            parent = cur if cur else '/'
            cur += '/' + part
            if cur not in self.dirs:
                self.dirs[cur] = set()
            self.dirs[parent].add(part)

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)                       # ensure parent dirs exist
        # mkdir creates a dir node for filePath itself; remove it and mark as file
        del self.dirs[filePath]
        parent = filePath.rsplit('/', 1)[0] or '/'
        self.dirs[parent].add(filePath.split('/')[-1])
        self.files[filePath] = self.files.get(filePath, '') + content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]


# ---------------------------------------------------------------------------
# Approach 2: Optimal (Trie)
# ---------------------------------------------------------------------------


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_file: bool = False
        self.content: str = ""


class FileSystem:
    """
    LeetCode 588 - Design In-Memory File System
    Difficulty: Hard

    Approach: Trie (Prefix Tree)
    - Each node in the trie represents a directory or a file.
    - `is_file` flag differentiates files from directories.
    - `content` stores file content (empty for directories).
    - Directory children are stored in a dict keyed by name.

    Time Complexity:
        ls             -> O(m + n log n)  m = path length, n = number of entries
        mkdir          -> O(m)            m = path length
        addContentToFile -> O(m)
        readContentFromFile -> O(m)

    Space Complexity: O(N * M)  N = total nodes, M = average name length
    """

    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def _traverse(self, path: str) -> TrieNode:
        """Walk the trie to the node at `path`, creating nodes as needed."""
        node = self.root
        if path == "/":
            return node
        for part in path.split("/")[1:]:  # skip leading empty string from split
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        return node

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)
        # If the path points to a file, return just its name
        if node.is_file:
            return [path.split("/")[-1]]
        # Otherwise return sorted directory contents
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path)  # creates intermediate nodes automatically

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._traverse(filePath)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._traverse(filePath)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath, content)
# param_4 = obj.readContentFromFile(filePath)
