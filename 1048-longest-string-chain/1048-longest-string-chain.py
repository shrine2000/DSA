class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        num_words = len(words)
        graph = [[] for _ in range(num_words)]   
        longest_chain_lengths = [0] * num_words   
        word_positions = {word: position for position, word in enumerate(words)}

        def find_longest_chain(position):
            if longest_chain_lengths[position] > 0:
                return longest_chain_lengths[position]

            longest_chain_lengths[position] = 1

            for neighbor in graph[position]:
                longest_chain_lengths[position] = max(longest_chain_lengths[position], find_longest_chain(neighbor) + 1)

            return longest_chain_lengths[position]

        for current_position in range(num_words):
            current_word = words[current_position]
            for char_position in range(len(current_word)):
                potential_word = current_word[:char_position] + current_word[char_position + 1:]
                if potential_word in word_positions:
                    graph[word_positions[potential_word]].append(current_position)

        max_chain_length = 0
        for position in range(num_words):
            max_chain_length = max(max_chain_length, find_longest_chain(position))

        return max_chain_length
        