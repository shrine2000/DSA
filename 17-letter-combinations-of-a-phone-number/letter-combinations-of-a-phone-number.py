class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        result = [""]
        for digit in digits:
            temp = []
            for combination in result:
                for letter in digit_to_letters[int(digit)]:
                    temp.append(combination + letter)
            result = temp
        return result
