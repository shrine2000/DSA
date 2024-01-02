class Solution:
    def __init__(self):
        self.num_words = 0
        self.memoization_table = [[-1] * 1001 for _ in range(1001)]

    # The predecessor function checks if one word can be formed by adding a single character to the other word.
    def is_predecessor(self, word1, word2):
        # Checks if word1 is a predecessor of word2 by comparing character sequences.
        len_word1, len_word2 = len(word1), len(word2)

        # Word2 should be one character longer than word1.
        if len_word2 - len_word1 != 1:
            return False

        i, j = 0, 0
        while i < len_word1 and j < len_word2:
            if word1[i] == word2[j]:
                i += 1
            j += 1
        return i == len_word1

    def find_longest_chain(self, words, prev_word_index, current_word_index):
        # Calculates the length of the longest string chain starting from the current word.
        if current_word_index == self.num_words:
            return 0

        if (
            prev_word_index != -1
            and self.memoization_table[prev_word_index][current_word_index] != -1
        ):
            return self.memoization_table[prev_word_index][current_word_index]

        # Try including the current word in the chain.
        taken = 0
        if prev_word_index == -1 or self.is_predecessor(
            words[prev_word_index], words[current_word_index]
        ):
            taken = 1 + self.find_longest_chain(
                words, current_word_index, current_word_index + 1
            )

        # Try excluding the current word from the chain.
        not_taken = self.find_longest_chain(
            words, prev_word_index, current_word_index + 1
        )

        if prev_word_index != -1:
            self.memoization_table[prev_word_index][current_word_index] = max(
                taken, not_taken
            )

        return max(taken, not_taken)

    def longest_string_chain(self, words):
        for i in range(1000):
            for j in range(1000):
                self.memoization_table[i][j] = -1

        self.num_words = len(words)
        words.sort(key=lambda x: len(x))  # Sort words by length in ascending order.

        # Start the chain with an empty previous word and the first word in the list.
        return self.find_longest_chain(words, -1, 0)


if __name__ == "__main__":
    words1 = ["a", "b", "ba", "bca", "bda", "bdca"]
    sol = Solution()
    output1 = sol.longest_string_chain(words1)
    print("Example 1 Output:", output1)  # Output should be 4

    words2 = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    output2 = sol.longest_string_chain(words2)
    print("Example 2 Output:", output2)  # Output should be 5

    words3 = ["abcd", "dbqca"]
    output3 = sol.longest_string_chain(words3)
    print("Example 3 Output:", output3)  # Output should be 1
