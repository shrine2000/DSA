class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_valid(substring):
            return substring == substring[::-1]

        def backtrack(start, path, result):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_valid(substring):
                    path.append(substring)
                    backtrack(end, path, result)
                    path.pop()

        result = []
        backtrack(0, [], result)
        return result
