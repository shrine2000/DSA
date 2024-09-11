class Solution:
    def reorganizeString(self, s: str) -> str:
        char_freq = Counter(s)
        heap = []
        for char, freq in char_freq.items():
            heapq.heappush(heap, (-freq, char))
        prev_char, prev_freq = "", 0
        result_str = []
        while heap:
            freq, char = heapq.heappop(heap)
            result_str.append(char)

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            prev_char = char
            prev_freq = freq + 1
        res = "".join(result_str)
        if len(res) == len(s):
            return res
        return ""
