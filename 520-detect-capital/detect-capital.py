class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) <= 1:
            return True

        is_upper_first = word[0].isupper()
        is_upper_second = word[1].isupper()

        if not is_upper_first and is_upper_second:
            return False

        if is_upper_first and is_upper_second:
            for ch in word[2:]:
                if not ch.isupper():
                    return False
        else:
            for ch in word[1:]:
                if not ch.islower():
                    return False
        return True
