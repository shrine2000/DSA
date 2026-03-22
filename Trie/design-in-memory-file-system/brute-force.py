from typing import List


# ---------------------------------------------------------------------------
# LeetCode 588 - Design In-Memory File System
# Approach: Brute Force (HashMap)
# ---------------------------------------------------------------------------
# Use two flat dicts:
#   dirs  : full dir path  -> set of immediate child names
#   files : full file path -> content string
#
# Every mkdir/addContentToFile walks the path splitting on '/' and registers
# each prefix in `dirs`. ls() just does a direct dict lookup.
#
# Time  Complexity: O(m) per operation  (m = number of path components)
# Space Complexity: O(N * M)            (N = total entries, M = avg path length)
# ---------------------------------------------------------------------------


class FileSystem:
    def __init__(self) -> None:
        self.dirs: dict[str, set] = {"/": set()}  # dir path -> child names
        self.files: dict[str, str] = {}           # file path -> content

    def ls(self, path: str) -> List[str]:
        if path in self.files:            # path points to a file
            return [path.split("/")[-1]]
        return sorted(self.dirs[path])   # path points to a directory

    def mkdir(self, path: str) -> None:
        parts = path.split("/")           # e.g. ['', 'a', 'b', 'c']
        cur = ""
        for part in parts[1:]:
            parent = cur if cur else "/"
            cur += "/" + part
            if cur not in self.dirs:
                self.dirs[cur] = set()
            self.dirs[parent].add(part)

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)              # create all intermediate dirs
        # mkdir registers filePath itself as a dir entry — undo that
        del self.dirs[filePath]
        parent = filePath.rsplit("/", 1)[0] or "/"
        self.dirs[parent].add(filePath.split("/")[-1])
        self.files[filePath] = self.files.get(filePath, "") + content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]


# obj = FileSystem()
# obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath, content)
# obj.readContentFromFile(filePath)
