class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(list(pattern)) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word and char_to_word[char] != word:
                return False

            if word in word_to_char and word_to_char[word] != char:
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True
