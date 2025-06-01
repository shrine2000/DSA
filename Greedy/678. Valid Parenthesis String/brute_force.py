from functools import lru_cache
from typing import List


class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache
        def dfs(idx, count):
            if idx == len(s):
                return count == 0

            if count < 0:
                return False

            char = s[idx]
            if char == "(":
                return dfs(idx + 1, count + 1)
            elif char == ")":
                return dfs(idx + 1, count - 1)
            else:
                return (
                    dfs(idx + 1, count + 1)
                    or dfs(idx + 1, count - 1)
                    or dfs(idx + 1, count)
                )

        return dfs(0, 0)


if __name__ == "__main__":
    pass
