class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        result = []

        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(idx, value):
            if idx == len(digits):
                result.append(''.join(value))
                return 

            letters = char_map[digits[idx]]

            for letter in letters:
                value.append(letter)
                backtrack(idx + 1, value)
                value.pop()

        backtrack(0, [])
        return result
