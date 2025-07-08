class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        result = []

        def is_valid(string):
            if not string:
                return False
            return string.lower() == string.lower()[::-1]

        def backtrack(start, path):
            if start == N:
                result.append(path[:])
                return
            for end in range(start + 1, N + 1):
                substring = s[start:end]
                if is_valid(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result
