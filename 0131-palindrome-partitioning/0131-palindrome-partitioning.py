class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(idx, ns, path, res):
            if idx == len(ns):
                res.append(path[:])
                return

            for i in range(idx, len(ns)):
                if isPalin(ns, idx, i):
                    path.append(ns[idx : i + 1])
                    backtrack(i + 1, ns, path, res)
                    path.pop()

        def isPalin(s, start, end):
            return s[start : end + 1] == s[start : end + 1][::-1]

        res = []
        path = []

        backtrack(0, s, path, res)

        return res
