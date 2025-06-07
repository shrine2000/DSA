class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []

        def backtrack(idx, path):
            if idx == len(s):
                results.append("".join(path))
                return

            char = s[idx]
            if char.isalpha():
                path.append(char.lower())
                backtrack(idx + 1, path)
                path.pop()

                path.append(char.upper())
                backtrack(idx + 1, path)
                path.pop()
            else:
                path.append(char)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])
        return results
