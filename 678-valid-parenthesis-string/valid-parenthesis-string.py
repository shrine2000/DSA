class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(i, balance):
            if balance < 0:
                return False

            if i == len(s):
                return balance == 0

            if s[i] == "(":
                return dfs(i + 1, balance + 1)

            elif s[i] == ")":
                return dfs(i + 1, balance - 1)

            else:
                return (
                    dfs(i + 1, balance + 1)
                    or dfs(i + 1, balance - 1)
                    or dfs(i + 1, balance)
                )

        return dfs(0, 0)
