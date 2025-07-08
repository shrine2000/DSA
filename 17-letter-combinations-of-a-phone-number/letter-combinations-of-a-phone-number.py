class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mappings = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        res = []

        def backtrack(idx, path):
            if idx == len(digits):
                res.append("".join(path))
                return
            current_digit = digits[idx]
            for char in mappings[int(current_digit)]:
                path.append(char)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])
        return res
