class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(current_str, open_count, closed_count):
            if len(current_str) == (2 * n):
                res.append(current_str)
                return

            if open_count < n:
                dfs(current_str + "(", open_count + 1, closed_count)

            if closed_count < open_count:
                dfs(current_str + ")", open_count, closed_count + 1)

        dfs("", 0, 0)
        return res
