class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # initialize variables
        length = 0
        last_word_length = 0

        # loop through the string character by character
        for i in range(len(s)):
            # if the current character is a space and the length is not zero,
            # update the last word length to the current length and reset the length
            if s[i] == ' ':
                if length != 0:
                    last_word_length = length
                length = 0
            # if the current character is not a space, increment the length
            else:
                length += 1

        # if the last character is not a space, update the last word length to the current length
        if length != 0:
            last_word_length = length

        # return the last word length
        return last_word_length