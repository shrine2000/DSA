class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        left, right = 0, len(s) - 1
        char = list(s)

        while left <= right:
            while left < right and char[left].lower() not in vowels:
                left += 1
            while left < right and char[right].lower() not in vowels:
                right -= 1
            char[left], char[right] = char[right], char[left]
            left += 1
            right -= 1
        return "".join(char)
